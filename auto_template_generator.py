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
            
            # Extract main function - capture everything until if __name__
            main_match = re.search(r'^(def main\(\):.+?)(?=^if __name__)', content, re.MULTILINE | re.DOTALL)
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
        
        # Extract main function - capture everything until if __name__
        main_match = re.search(r'^(def main\(\):.+?)(?=^if __name__)', content, re.MULTILINE | re.DOTALL)
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
    
    # Pattern 1: class Solution exists
    class_match = re.search(r'class Solution \{.*?^public:(.*?)^\};', content, re.MULTILINE | re.DOTALL)
    if not class_match:
        class_match = re.search(r'class Solution \{(.*?)^\};', content, re.MULTILINE | re.DOTALL)
    
    if class_match:
        # Find first public method
        pub_method = re.search(r'(\w+(?:<[^>]+>)?(?:\s*&)?\s+\w+\([^)]*\))\s*\{', class_match.group(1))
        if pub_method:
            method_sig = pub_method.group(1).strip()
            
            # Extract main function
            main_match = re.search(r'^(int main\(\).*?)^}', content, re.MULTILINE | re.DOTALL)
            main_body = main_match.group(1) + '}' if main_match else 'int main() {\n    return 0;\n}'
            
            return f'''```cpp
{includes_str}

using namespace std;

class Solution {{
public:
    {method_sig} {{
        // Implementation here
        return {{}};
    }}
}};

{main_body}
```'''

    # Pattern 2: Standalone function
    # Find the function called in main or the first non-main function
    main_match = re.search(r'^(int main\(\).*?)^}', content, re.MULTILINE | re.DOTALL)
    if main_match:
        main_body = main_match.group(1) + '}'
        
        # Look for the function call in main to identify the solution function
        # e.g. cout << minCost(n, k, s) << ...
        # limiting search to simple function calls
        pass # To be implemented if we want strict call matching, but simpler is to find the function definition
    else:
        main_body = 'int main() {\n    return 0;\n}'

    # Find the standalone function definition
    # Matching pattern: Type Name(Args) {
    # We use a regex that matches start of line (possibly indented), checks for return type, then name
    # We explicitly exclude control structures (if, for, while, etc) in loop
    
    # Regex breakdown:
    # ^[\t ]* : Start of line, optional indentation
    # ([a-zA-Z0-9_<>:*&]+(?:[\s*&]+[a-zA-Z0-9_<>:*&]+)*) : Return type (words, symbols like < > : * &, separated by space/symbols)
    # \s+ : separator
    # (\w+) : Function name
    # \s*\( : Opening paren
    # ([^)]*) : Args
    # \)\s*\{ : Closing paren and opening brace
    regex = r'^[\t ]*([a-zA-Z0-9_<>:*&]+(?:[\s*&]+[a-zA-Z0-9_<>:*&]+)*)\s+(\w+)\s*\(([^)]*)\)\s*\{'
    
    keywords = {'if', 'while', 'for', 'switch', 'catch', 'else'}
    
    matches = re.finditer(regex, content, re.MULTILINE)
    for m in matches:
        ret_type = m.group(1).strip()
        func_name = m.group(2)
        args_str = m.group(3)
        
        if func_name in keywords or func_name == 'main':
            continue
            
        # Found a potential solution function
        method_sig = f"{ret_type} {func_name}({args_str})"
        
        return f'''```cpp
{includes_str}

using namespace std;

class Solution {{
public:
    {method_sig} {{
        // Implementation here
        return {{}};
    }}
}};

{main_body}
```'''
    
    return None

def extract_js_template(filepath: Path) -> str | None:
    """Extract JavaScript template from solution file."""
    try:
        content = filepath.read_text()
    except:
        return None
    
    # Extract I/O handling
    # We want everything AFTER the Solution class, usually starting with input handling
    # If we find class Solution, we take everything after it
    
    class_match = re.search(r'class Solution \{(.*?)\n\}', content, re.DOTALL)
    
    # Pattern 1: class Solution exists
    if class_match:
        # Find first method
        method_match = re.search(r'(\w+\([^)]*\))\s*\{', class_match.group(1))
        
        if method_match:
            method_sig = method_match.group(1).strip()
            
            # Determine I/O block location
            # Check after class first
            io_block_after = content[class_match.end():].strip()
            # Check before class if after is empty/insufficient
            io_block_before = content[:class_match.start()].strip()
            
            # Heuristic: verify which block actually has I/O logic
            io_block = ''
            if 'createInterface' in io_block_after or 'process.stdin' in io_block_after or 'fs.read' in io_block_after:
                io_block = io_block_after
            elif 'createInterface' in io_block_before or 'process.stdin' in io_block_before or 'fs.read' in io_block_before:
                io_block = io_block_before
            
            # Clean up require statement if it was in the block to avoid duplication
            io_block = io_block.replace('const readline = require("readline");', '').strip()
            io_block = io_block.replace("const readline = require('readline');", '').strip()
            io_block = io_block.replace('const fs = require("fs");', '').strip()
            
            # Add fs require if needed and not present in fixed imports
            extra_imports = ""
            if 'fs.read' in io_block and 'require("fs")' not in io_block and 'require(\'fs\')' not in io_block:
                extra_imports = 'const fs = require("fs");\n'

            return f'''```javascript
const readline = require("readline");
{extra_imports}
class Solution {{
  {method_sig} {{
    // Implementation here
    return null;
  }}
}}

{io_block}
```'''

    # Pattern 2: Standalone function

    # Pattern 2: Standalone function
    # e.g. function minCost(n, k, s) { ... }
    func_match = re.search(r'^function (\w+)\(([^)]*)\)\s*\{', content, re.MULTILINE)
    if func_match:
        func_name = func_match.group(1)
        args = func_match.group(2)
        
        # We need to adapt the main I/O code if it calls the function directly
        # But for template generation, we keep the main logic and just ensure the user instantiates Solution
        # So we wrap the standalone function into Solution class
        
        # Find I/O block for standalone function
        # Since there is no class, we look for where I/O starts (e.g. readline or fs)
        io_start_match = re.search(r'(const (readline|rl|fs) =|require\()', content)
        
        # This is tricky because the require might be at the top. 
        # We usually want everything EXCEPT the function definition.
        # Simplest approach: Remove the function definition from content and use the rest as I/O
        
        # Remove the function block
        # We need to match the function body properly. 
        # Assuming function body ends at last } or we can try to simplistic removal
        
        # Better: Search for specific I/O markers
        # If imports are at top, we keep them.
        
        # Let's take the whole content and remove the function definition part?
        # A bit risky. 
        
        # Let's try finding the function end.
        # This is hard with regex.
        
        # Fallback: Just grab everything that looks like I/O code.
        # Most standalone solutions have imports at top, function, then I/O at bottom.
        
        # Let's try to identify the I/O block by looking for the I/O start (readline or fs) that is NOT at the very top (start of file).
        # Actually usually:
        # const fs = require('fs');
        # function solve() { ... }
        # const input = fs...
        
        # So we can look for the part that has 'createInterface' or 'fs.read' or 'process.stdin'
        
        # Let's just reuse the "io_block" logic from before but adapted
        
        # Search for `createInterface` or `fs.read` or `process.stdin`
        io_markers = ['createInterface', 'process.stdin', 'fs.read', 'fs.readFileSync']
        io_start_idx = -1
        for marker in io_markers:
            idx = content.find(marker)
            if idx != -1:
                # Find the start of that line
                line_start = content.rfind('\n', 0, idx)
                if line_start != -1:
                    # We found a line with I/O.
                    # This is likely inside the I/O block.
                    # But we need the whole block.
                    pass
        
        # Alternative: Just assume everything except the function is I/O.
        # We construct the I/O block by taking the original content and replacing the function definition with empty string.
        # But we need to fuzzy match the function definition.
        
        # If regex matched `func_match`, we know where it starts.
        # We don't know where it ends.
        
        # Let's just use a fallback I/O block if we can't find it clearly?
        # WAit, the error is `io_block.replace`.
        # I need `io_block` variable defined.
        
        # For now, let's just grep "const readline" or "const fs"
        
        io_block = ""
        # Try to find the standard readline block
        rl_match = re.search(r'const rl = readline\.createInterface.*', content, re.DOTALL)
        if rl_match:
             io_block = rl_match.group(0)
        else:
             # Try fs block
             fs_match = re.search(r'const input = fs\.read.*', content, re.DOTALL)
             if fs_match:
                 io_block = "const fs = require('fs');\n" + fs_match.group(0)
             else:
                 # Last resort: look for anything after the function if we can guess end
                 pass

        if not io_block:
             # Just use a dummy I/O if we can't extract
             io_block = "// I/O handling"

        updated_io = io_block.replace('const readline = require("readline");', '').strip()
        updated_io = re.sub(fr'{func_name}\(', f'new Solution().{func_name}(', updated_io)
        
        return f'''```javascript
const readline = require("readline");

class Solution {{
  {func_name}({args}) {{
    // Implementation here
    return null;
  }}
}}

{updated_io}
```'''

    return None

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
