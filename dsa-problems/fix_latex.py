import os
import re

def fix_latex_content(content):
    # Map of LaTeX commands to text/code equivalents
    replacements = [
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
        (r'\\text\{([^}]*)\}', r'\1'), # Remove \text{} wrapper
        (r'\\mathbf\{([^}]*)\}', r'\1'), # Remove \mathbf{} wrapper
        (r'\{', ''), # Remove stray braces often used in LaTeX grouping
        (r'\}', ''), 
    ]
    
    # 1. Handle Display Math $$ ... $$
    # Replace with plain lines or code blocks. Let's make them singular backtick lines or just text.
    # Often display math works well as indented text or just standalone lines.
    # We will strip $$ and wrap in backticks? No, multi-line backticks are code blocks.
    
    def replace_display_math(match):
        inner = match.group(1)
        for lat, rep in replacements:
            inner = re.sub(lat, rep, inner)
        inner = inner.strip()
        return f"\n`{inner}`\n"

    # Regex for $$ ... $$ (dotall)
    content = re.sub(r'\$\$(.*?)\$\$', replace_display_math, content, flags=re.DOTALL)

    # 2. Handle Inline Math $ ... $
    def replace_inline_math(match):
        inner = match.group(1)
        # Apply replacements
        for lat, rep in replacements:
            inner = re.sub(lat, rep, inner)
        
        # Strip braces that might remain from simple grouping like ^{2} -> ^2
        inner = inner.replace('{', '').replace('}', '')
        inner = inner.replace('\\', '') # Remove remaining backslashes (like \, or \!)
        
        return f"`{inner.strip()}`"

    # Regex for $ ... $
    # Be careful not to match across newlines excessively, usually inline math is on one line.
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
    
    for root, dirs, files in os.walk(base_dir):
        if "editorials" in root:
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)
                    if process_file(path):
                        print(f"Fixed: {file}")
                        updated_count += 1
                        
    print(f"Total files updated: {updated_count}")

if __name__ == "__main__":
    main()
