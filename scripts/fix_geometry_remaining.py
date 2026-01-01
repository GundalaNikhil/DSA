#!/usr/bin/env python3
import os
import re
import glob

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
SOLUTIONS_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Geometry", "solutions")

def fix_geo_015_java():
    """GEO-015 Java needs Main wrapper"""
    path = os.path.join(SOLUTIONS_DIR, "java", "GEO-015-segment-rectangle-intersection.java")
    with open(path, 'r') as f:
        content = f.read()
    
    if "class Main" in content:
        return  # Already fixed
    
    new_content = """import java.util.*;
import java.io.*;

class Main {
""" + content + """
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        long xL = sc.nextLong(); long yB = sc.nextLong();
        long xR = sc.nextLong(); long yT = sc.nextLong();
        long x1 = sc.nextLong(); long y1 = sc.nextLong();
        long x2 = sc.nextLong(); long y2 = sc.nextLong();
        System.out.println(new Solution().intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false");
    }
}
"""
    
    with open(path, 'w') as f:
        f.write(new_content)
    print("Fixed GEO-015 Java")

def fix_javascript_files():
    """Fix JavaScript files with wrong function names and template literal issues"""
    
    fixes = {
        "GEO-002": ("classifyPoint", "classifyPoint"),  # Function name mismatch
        "GEO-005": None,  # Check for template literal issues
        "GEO-006": None,
        "GEO-007": None,
        "GEO-008": None,
        "GEO-009": None,
        "GEO-012": None,
        "GEO-013": None,
    }
    
    for pid, fix_info in fixes.items():
        pattern = os.path.join(SOLUTIONS_DIR, "javascript", f"{pid}*.js")
        files = glob.glob(pattern)
        if not files:
            continue
        
        path = files[0]
        with open(path, 'r') as f:
            content = f.read()
        
        original_content = content
        
        # Fix GEO-002 specifically - wrong function name
        if pid == "GEO-002":
            content = content.replace("console.log(pointInPolygon(n, xs, ys, nextInt(), nextInt()));",
                                     "console.log(classifyPoint(xs, ys, nextInt(), nextInt()));")
        
        # Fix template literal issues (backticks in console.log)
        # Pattern: console.log(`...${...}...`)
        # These should be: console.log(... + " " + ...)
        
        # Common pattern: console.log(`${x.toFixed(6)} ${y.toFixed(6)}`)
        content = re.sub(r'console\.log\(`\$\{([^}]+)\} \$\{([^}]+)\}`\)', 
                        r'console.log(\1 + " " + \2)', content)
        
        # Pattern: console.log(`${res[0].toFixed(6)} ${res[1].toFixed(6)} ${res[2].toFixed(6)}`)
        content = re.sub(r'console\.log\(`\$\{([^}]+)\} \$\{([^}]+)\} \$\{([^}]+)\}`\)',
                        r'console.log(\1 + " " + \2 + " " + \3)', content)
        
        # Pattern: console.log(`${p.x.toFixed(6)} ${p.y.toFixed(6)}`)
        content = re.sub(r'console\.log\(`\$\{p\.x\.toFixed\(6\)\} \$\{p\.y\.toFixed\(6\)\}`\)',
                        r'console.log(p.x.toFixed(6) + " " + p.y.toFixed(6))', content)
        
        # Pattern: console.log(`${p[0]} ${p[1]}`)
        content = re.sub(r'console\.log\(`\$\{p\[0\]\} \$\{p\[1\]\}`\)',
                        r'console.log(p[0] + " " + p[1])', content)
        
        if content != original_content:
            with open(path, 'w') as f:
                f.write(content)
            print(f"Fixed {pid} JavaScript")

def fix_cpp_files():
    """Fix C++ files with return type and signature issues"""
    
    # GEO-005: cappedHull should return vector<pair<long long, long long>>
    path = os.path.join(SOLUTIONS_DIR, "cpp", "GEO-005-convex-hull-capped.cpp")
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
        
        # Check if function signature needs fixing
        if "vector<pair<int,int>>" in content:
            content = content.replace("vector<pair<int,int>>", "vector<pair<long long,long long>>")
            with open(path, 'w') as f:
                f.write(content)
            print("Fixed GEO-005 C++ return type")
    
    # GEO-008: minEnclosingCircle should return vector<double> with 3 elements
    path = os.path.join(SOLUTIONS_DIR, "cpp", "GEO-008-minimum-enclosing-circle.cpp")
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
        
        # Check if return type needs fixing
        if "tuple<double,double,double>" in content:
            content = content.replace("tuple<double,double,double>", "vector<double>")
            content = content.replace("make_tuple(", "vector<double>{")
            content = content.replace("return {", "return vector<double>{")
            with open(path, 'w') as f:
                f.write(content)
            print("Fixed GEO-008 C++ return type")
    
    # GEO-009: halfPlaneIntersection should return vector<pair<double,double>>
    path = os.path.join(SOLUTIONS_DIR, "cpp", "GEO-009-half-plane-intersection.cpp")
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
        
        if "vector<Point>" in content and "struct Point" not in content:
            # Need to change to pair
            content = content.replace("vector<Point>", "vector<pair<double,double>>")
            content = content.replace("Point{", "make_pair(")
            content = content.replace("Point(", "make_pair(")
            with open(path, 'w') as f:
                f.write(content)
            print("Fixed GEO-009 C++ return type")

def main():
    print("Fixing remaining Geometry issues...")
    fix_geo_015_java()
    fix_javascript_files()
    fix_cpp_files()
    print("Done!")

if __name__ == "__main__":
    main()
