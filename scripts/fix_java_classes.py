import os
import re

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
JAVA_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Tries", "solutions", "java")

def fix_java_classes():
    if not os.path.exists(JAVA_DIR):
        print(f"Directory not found: {JAVA_DIR}")
        return

    for filename in os.listdir(JAVA_DIR):
        if filename.endswith(".java"):
            filepath = os.path.join(JAVA_DIR, filename)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Regex to match 'public class Name' or 'class Name' and change to 'class Main'
            # First, check if 'class Main' exists. If not, rename the public class.
            new_content = content
            if 'class Main' not in content:
                new_content = re.sub(r'(public\s+)?class\s+(\w+)', r'class Main', content, count=1)
            
            if new_content != content:
                print(f"Fixing {filename}")
                with open(filepath, 'w') as f:
                    f.write(new_content)

if __name__ == "__main__":
    fix_java_classes()
