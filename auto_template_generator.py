#!/usr/bin/env python3
"""
Auto-generate solution templates from existing solutions.
Extracts method signatures + I/O handling, strips implementation details.

Usage:
    python auto_template_generator.py <category> [--dry-run]
    
Example:
    python auto_template_generator.py AdvancedGraphs
    python auto_template_generator.py TreesDP --dry-run
"""

import re
import os
import sys
from pathlib import Path

BASE_DIR = Path("/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems")

def get_java_default_return(ret_type: str) -> str:
    """Get default return statement for Java type."""
    defaults = {
        'void': '',
        'int': 'return 0;',
        'long': 'return 0;',
        'boolean': 'return false;',
        'double': 'return 0.0;',
        'int[]': 'return new int[0];',
        'long[]': 'return new long[0];',
        'double[]': 'return new double[0];',
        'int[][]': 'return new int[0][0];',
        'long[][]': 'return new long[0][0];',
        'String': 'return "";',
        'String[]': 'return new String[0];',
    }
    if ret_type in defaults:
        return defaults[ret_type]
    if ret_type.startswith('List<') or ret_type.startswith('Set<'):
        return 'return new ArrayList<>();'
    if ret_type.endswith('[]'):
        return f'return new {ret_type[:-2]}[0];'
    return 'return null;'

def get_python_default_return(func_def: str) -> str:
    """Get default return for Python function."""
    if '-> None' in func_def or '-> void' in func_def:
        return 'pass'
    if '-> bool' in func_def:
        return 'return False'
    if '-> int' in func_def or '-> float' in func_def:
        return 'return 0'
    if '-> str' in func_def:
        return 'return ""'
    if '-> list' in func_def or '-> List' in func_def:
        return 'return []'
    if '-> tuple' in func_def or '-> Tuple' in func_def:
        return 'return ()'
    if '-> dict' in func_def or '-> Dict' in func_def:
        return 'return {}'
    return 'return None'

def extract_java_template(filepath: Path) -> str | None:
    """Extract Java template from solution file."""
    try:
        content = filepath.read_text()
    except:
        return None
    
    # Extract imports
    imports = re.findall(r'^import [^;]+;', content, re.MULTILINE)
    imports_str = '\n'.join(imports) if imports else 'import java.util.*;'
    
    # Pattern 1: class Solution exists
    solution_match = re.search(r'class Solution \{(.*?)^\}', content, re.MULTILINE | re.DOTALL)
    if solution_match:
        # Extract the first public method signature
        pub_method = re.search(r'(public \w+(?:<[^>]+>)?(?:\[\])* \w+\([^)]*\))\s*\{', solution_match.group(1))
        if pub_method:
            method_sig = pub_method.group(1).strip()
            ret_match = re.match(r'public (\w+(?:<[^>]+>)?(?:\[\])*)', method_sig)
            ret_type = ret_match.group(1) if ret_match else 'void'
            default_return = get_java_default_return(ret_type)
            
            # Extract Main class
            main_match = re.search(r'(class Main \{.*?^\})', content, re.MULTILINE | re.DOTALL)
            if main_match:
                return_stmt = f'\n        {default_return}' if default_return else ''
                return f'''```java
{imports_str}

class Solution {{
    {method_sig} {{
        // Implementation here{return_stmt}
    }}
}}

{main_match.group(1)}
```'''
    
    # Pattern 2: Only class Main (no Solution class) - create Solution class from Main's logic
    main_match = re.search(r'class Main \{.*?public static void main\(String\[\] args\)\s*\{(.*?)^\s*\}', content, re.MULTILINE | re.DOTALL)
    if main_match:
        # Find the expected method call pattern to infer signature
        main_body = main_match.group(1)
        
        # Look for a pattern like "solution.methodName" or just extract first non-standard method
        static_method = re.search(r'static (\w+(?:<[^>]+>)?(?:\[\])* \w+\([^)]*\))\s*\{', content)
        if static_method:
            method_sig = static_method.group(1).replace('static ', '')
            # Convert to instance method
            method_sig = 'public ' + method_sig
            ret_match = re.match(r'(\w+)', method_sig.split()[1])
            ret_type = ret_match.group(1) if ret_match else 'void'
            default_return = get_java_default_return(ret_type)
            
            return_stmt = f'\n        {default_return}' if default_return else ''
            
            # Reconstruct with Solution class
            full_main = re.search(r'(class Main \{.*?^\})', content, re.MULTILINE | re.DOTALL)
            return f'''```java
{imports_str}

class Solution {{
    {method_sig} {{
        // Implementation here{return_stmt}
    }}
}}

{full_main.group(1) if full_main else 'class Main { }'}
```'''
    
    return None

def extract_python_template(filepath: Path) -> str | None:
    """Extract Python template from solution file."""
    try:
        content = filepath.read_text()
    except:
        return None
    
    # Find imports at top
    imports = []
    for line in content.split('\n'):
        if line.startswith('import ') or line.startswith('from '):
            imports.append(line)
        elif line.strip() and not line.startswith('#'):
            break
    imports_str = '\n'.join(imports) if imports else 'import sys'
    
    # Pattern 1: class Solution exists
    class_match = re.search(r'^class Solution:', content, re.MULTILINE)
    if class_match:
        # Find the first non-dunder method
        method_match = re.search(r'^    def (?!__)\w+\(self[^)]*\)[^:]*:', content, re.MULTILINE)
        if method_match:
            method_def = method_match.group(0).strip()
            default_return = get_python_default_return(method_def)
            
            # Extract main function
            main_match = re.search(r'^(def main\(\):.*?)(?=\n\nif __name__|$)', content, re.MULTILINE | re.DOTALL)
            main_body = main_match.group(1).rstrip() if main_match else 'def main():\n    pass'
            
            return f'''```python
{imports_str}

class Solution:
    {method_def}
        # Implementation here
        {default_return}

{main_body}

if __name__ == "__main__":
    main()
```'''
    
    # Pattern 2: Standalone function (no class)
    func_match = re.search(r'^(def (?!main|_)[a-z_]+\([^)]*\)[^:]*:)', content, re.MULTILINE)
    if func_match:
        func_def = func_match.group(1)
        default_return = get_python_default_return(func_def)
        
        # Extract main function
        main_match = re.search(r'^(def main\(\):.*?)(?=\n\nif __name__|$)', content, re.MULTILINE | re.DOTALL)
        if main_match:
            main_body = main_match.group(1).rstrip()
            return f'''```python
{imports_str}

{func_def}
    # Implementation here
    {default_return}

{main_body}

if __name__ == "__main__":
    main()
```'''
    
    return None

def extract_cpp_template(filepath: Path) -> str | None:
    """Extract C++ template from solution file."""
    try:
        content = filepath.read_text()
    except:
        return None
    
    # Extract includes
    includes = re.findall(r'^#include <[^>]+>', content, re.MULTILINE)
    includes_str = '\n'.join(includes[:5]) if includes else '#include <iostream>\n#include <vector>'
    
    # Find class Solution with public method
    class_match = re.search(r'class Solution \{.*?^public:(.*?)^\};', content, re.MULTILINE | re.DOTALL)
    if not class_match:
        # Try without explicit public
        class_match = re.search(r'class Solution \{(.*?)^\};', content, re.MULTILINE | re.DOTALL)
    
    if not class_match:
        return None
    
    # Find first public method
    pub_method = re.search(r'(\w+(?:<[^>]+>)?(?:\s*&)?\s+\w+\([^)]*\))\s*\{', class_match.group(1))
    if not pub_method:
        return None
    
    method_sig = pub_method.group(1).strip()
    
    # Extract main function
    main_match = re.search(r'^(int main\(\).*?)^}', content, re.MULTILINE | re.DOTALL)
    if not main_match:
        return None
    
    template = f'''```cpp
{includes_str}

using namespace std;

class Solution {{
public:
    {method_sig} {{
        // Implementation here
        return {{}};
    }}
}};

{main_match.group(1)}}}
```'''
    return template

def extract_js_template(filepath: Path) -> str | None:
    """Extract JavaScript template from solution file."""
    try:
        content = filepath.read_text()
    except:
        return None
    
    # Find class Solution with method
    class_match = re.search(r'class Solution \{(.*?)\n\}', content, re.DOTALL)
    if not class_match:
        return None
    
    # Find first method
    method_match = re.search(r'(\w+\([^)]*\))\s*\{', class_match.group(1))
    if not method_match:
        return None
    
    method_sig = method_match.group(1).strip()
    
    # Extract I/O handling (everything after class definition)
    io_match = re.search(r'^const rl = readline\.createInterface.*', content, re.MULTILINE | re.DOTALL)
    if not io_match:
        return None
    
    template = f'''```javascript
const readline = require("readline");

class Solution {{
  {method_sig} {{
    // Implementation here
    return null;
  }}
}}

{io_match.group(0).strip()}
```'''
    return template

def update_markdown_file(md_path: Path, templates: dict) -> bool:
    """Update the markdown file with new templates."""
    try:
        content = md_path.read_text()
    except:
        return False
    
    # Find Solution Template section
    section_match = re.search(r'(## Solution Template\n)', content)
    if not section_match:
        return False
    
    # Build new template section
    new_section = "## Solution Template\n\n"
    
    for lang in ['java', 'python', 'cpp', 'javascript']:
        lang_title = {'java': 'Java', 'python': 'Python', 'cpp': 'C++', 'javascript': 'JavaScript'}[lang]
        new_section += f"### {lang_title}\n\n"
        if lang in templates and templates[lang]:
            new_section += templates[lang] + "\n\n"
        else:
            new_section += "```\n// No template available\n```\n\n"
    
    # Replace everything after "## Solution Template" until end of file
    new_content = content[:section_match.start()] + new_section.rstrip() + "\n"
    
    md_path.write_text(new_content)
    return True

def process_category(category: str, dry_run: bool = False):
    """Process all problems in a category."""
    cat_dir = BASE_DIR / category
    problems_dir = cat_dir / "problems"
    solutions_dir = cat_dir / "solutions"
    
    if not problems_dir.exists():
        print(f"Error: {problems_dir} not found")
        return
    
    problems = sorted(problems_dir.glob("*.md"))
    print(f"Found {len(problems)} problems in {category}")
    
    for md_file in problems:
        problem_id = md_file.stem
        print(f"\n{'[DRY-RUN] ' if dry_run else ''}Processing {problem_id}...")
        
        templates = {}
        
        # Try each language
        for lang, ext in [('java', '.java'), ('python', '.py'), ('cpp', '.cpp'), ('javascript', '.js')]:
            sol_file = solutions_dir / lang / f"{problem_id}{ext}"
            if sol_file.exists():
                if lang == 'java':
                    templates[lang] = extract_java_template(sol_file)
                elif lang == 'python':
                    templates[lang] = extract_python_template(sol_file)
                elif lang == 'cpp':
                    templates[lang] = extract_cpp_template(sol_file)
                elif lang == 'javascript':
                    templates[lang] = extract_js_template(sol_file)
                
                status = "✓" if templates.get(lang) else "✗ (parse failed)"
                print(f"  {lang}: {status}")
        
        if not dry_run and templates:
            if update_markdown_file(md_file, templates):
                print(f"  Updated {md_file.name}")
            else:
                print(f"  Failed to update {md_file.name}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python auto_template_generator.py <category> [--dry-run]")
        print("\nAvailable categories:")
        for d in sorted(BASE_DIR.iterdir()):
            if d.is_dir() and (d / "problems").exists():
                count = len(list((d / "problems").glob("*.md")))
                print(f"  - {d.name} ({count} problems)")
        return
    
    category = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    
    process_category(category, dry_run)
    print("\nDone!")

if __name__ == "__main__":
    main()
