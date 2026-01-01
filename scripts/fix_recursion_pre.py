import os
import re

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
REC_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Recursion", "solutions")

def fix_cpp_driver(content, problem_id):
    if "int main()" in content:
        return content
    
    # Generic driver logic based on problem inputs
    # This is a simplified approach; might need customization per problem
    # But let's try to infer from Python or just add a basic template if possible.
    # Actually, the best way is to look at Python solution to parse input? 
    # Or just add a generic scanner.
    
    # For now, let's just log which files are missing main to manual fix or 
    # use a smarter generation if we can read the python driver style.
    
    # Let's try to reuse the 'fix_geometry.py' approach if adaptable, 
    # but that was complex. 
    
    # Simpler: Many of these recursion problems take N, K type inputs or grids.
    # REC-001: Dorm Room Paths (Grid paths?)
    # REC-002: Lab ID Permutations
    
    # I'll just flag them for now or try to append a generic "read everything" block 
    # if I can verify signatures.
    
    # Better yet, let's just fix the JS syntax error first as it's trivial.
    return content

def fix_js_syntax(content):
    # Fix: const key = ``idx,`{remainingK}`; -> const key = `${idx},${remainingK}`;
    # The error showed: const key = ``idx,`{remainingK}`;
    # It likely meant to be template literal.
    
    # Regex to fix specific pattern seen in REC-004
    content = re.sub(r'const key = ``idx,`\{remainingK\}\`;', 'const key = `${idx},${remainingK}`;', content)
    # Generic fix for bad template strings if any other
    return content

def main():
    # Fix JS
    js_dir = os.path.join(REC_DIR, "javascript")
    for f in os.listdir(js_dir):
        if not f.endswith(".js"): continue
        path = os.path.join(js_dir, f)
        with open(path, 'r') as file:
            content = file.read()
        
        new_content = fix_js_syntax(content)
        
        if content != new_content:
            print(f"Fixing JS: {f}")
            with open(path, 'w') as file:
                file.write(new_content)

if __name__ == "__main__":
    main()
