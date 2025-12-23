import os
import re

def fix_latex_content(content):
    # Map of LaTeX commands to text/code equivalents
    replacements = [
        (r'\\leq', '<='),
        (r'\\geq', '>='),
        (r'\\le', '<='),
        (r'\\ge', '>='),
        (r'\\cdot', '*'),
        (r'\\times', 'x'),
        (r'\\approx', '~='),
        (r'\\ne', '!='),
        (r'\\rightarrow', '->'),
        (r'\\leftarrow', '<-'),
        (r'\\to', '->'),
        (r'\\infty', 'infinity'),
        (r'\\pm', '+/-'),
        (r'\\sum', 'sum'),
        (r'\\theta', 'theta'),
        (r'\\in', 'in'),
        (r'\\alpha', 'alpha'),
        (r'\\beta', 'beta'),
        (r'\\pi', 'pi'),
        (r'\\phi', 'phi'),
        (r'\\Delta', 'Delta'),
        (r'\\text\{([^}]*)\}', r'\1'), # Remove \text{} wrapper
        (r'\\mathbf\{([^}]*)\}', r'\1'), # Remove \mathbf{} wrapper
        (r'\{', ''), # Remove braces often used in LaTeX grouping
        (r'\}', ''), 
    ]
    
    # 1. Handle Display Math $$ ... $$
    # Convert to single lines wrapped in backticks
    def replace_display_math(match):
        inner = match.group(1)
        for lat, rep in replacements:
            inner = re.sub(lat, rep, inner)
        
        # Handle powers/indices
        inner = re.sub(r'\^(\w+)', r'^\1', inner) # x^2 -> x^2 (no change needed mostly, but remove braces if any)
        
        inner = inner.strip()
        return f"\n`{inner}`\n"

    content = re.sub(r'\$\$(.*?)\$\$', replace_display_math, content, flags=re.DOTALL)

    # 2. Handle Inline Math $ ... $
    def replace_inline_math(match):
        inner = match.group(1)
        # Apply replacements
        for lat, rep in replacements:
            inner = re.sub(lat, rep, inner)
        
        # Strip braces that might remain
        inner = inner.replace('{', '').replace('}', '')
        inner = inner.replace('\\', '') # Remove remaining backslashes
        
        # Handle 10^x explicitly if needed, but the simple replacement usually works
        
        return f"`{inner.strip()}`"

    content = re.sub(r'\$([^\$\n]+)\$', replace_inline_math, content)
    
    return content

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '$' not in content:
        return False
        
    new_content = fix_latex_content(content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    base_dir = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"
    updated_count = 0
    
    # Walk through ALL directories
    for root, dirs, files in os.walk(base_dir):
        # Filter for relevant folders if we want to be safe, or just do all
        # We want problems and editorials primarily
        if "problems" in root or "editorials" in root:
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    if process_file(path):
                        print(f"Fixed: {file}")
                        updated_count += 1
                        
    print(f"Total files updated: {updated_count}")

if __name__ == "__main__":
    main()
