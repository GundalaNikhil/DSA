import os
import re

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
JAVA_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Stacks", "solutions", "java")

def fix_java_classes():
    if not os.path.exists(JAVA_DIR):
        print(f"Directory not found: {JAVA_DIR}")
        return

    for filename in os.listdir(JAVA_DIR):
        if filename.endswith(".java"):
            filepath = os.path.join(JAVA_DIR, filename)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Remove 'public' from 'public class Main'
            # Regex to match 'public class Main' possibly with whitespace
            new_content = re.sub(r'public\s+class\s+Main', 'class Main', content)
            
            if new_content != content:
                print(f"Fixing {filename}")
                with open(filepath, 'w') as f:
                    f.write(new_content)

if __name__ == "__main__":
    fix_java_classes()
