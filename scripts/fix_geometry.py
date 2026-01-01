import os
import re

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
SOLUTIONS_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Geometry", "solutions")

# Problem Metadata
# func: name of the function/method in the solution file (if identifiable)
# type: input format type
METADATA = {
    "GEO-001": {"type": "triplet", "cpp_func": "orientation", "js_func": "orientation"},
    "GEO-002": {"type": "poly_query", "cpp_func": "pointInPolygon", "js_func": "pointInPolygon"},
    "GEO-003": {"type": "segments", "cpp_func": "countIntersections", "js_func": "countIntersections"},
    "GEO-004": {"type": "points_ret_int", "cpp_func": "closestPair", "js_func": "closestPair"},
    "GEO-005": {"type": "points_theta", "cpp_func": "cappedHull", "js_func": "cappedHull"},
    "GEO-006": {"type": "points_ret_int", "cpp_func": "polygonArea", "js_func": "polygonArea"},
    "GEO-007": {"type": "points_ret_int", "cpp_func": "diameter", "js_func": "diameter"},
    "GEO-008": {"type": "points_ret_circle", "cpp_func": "minEnclosingCircle", "js_func": "minEnclosingCircle"},
    "GEO-009": {"type": "halfplanes", "cpp_func": "halfPlaneIntersection", "js_func": "halfPlaneIntersection"},
    "GEO-010": {"type": "rects_weighted", "cpp_func": "weightedArea", "js_func": "weightedArea"},
    "GEO-011": {"type": "rects", "cpp_func": "maxOverlap", "js_func": "maxOverlap"},
    "GEO-012": {"type": "rect_points", "cpp_func": "largestEmptyCircle", "js_func": "largestEmptyCircle"},
    "GEO-013": {"type": "seg_point", "cpp_func": "distance", "js_func": "distance"},
    "GEO-014": {"type": "points_ret_points", "cpp_func": "sortByAngle", "js_func": "sortByAngle"},
    # GEO-015 Skipped (already working)
    "GEO-016": {"type": "points_ret_int", "cpp_func": "manhattanMST", "js_func": "manhattanMST"},
}

def get_java_main(ptype, problem_id):
    # Generates the inside of main(String[] args) for Java
    code = ""
    code += "        Scanner sc = new Scanner(System.in);\n"
    code += "        if (!sc.hasNext()) return;\n"
    
    if ptype == "triplet":
        code += "        long x1 = sc.nextLong(); long y1 = sc.nextLong();\n"
        code += "        long x2 = sc.nextLong(); long y2 = sc.nextLong();\n"
        code += "        long x3 = sc.nextLong(); long y3 = sc.nextLong();\n"
        code += "        System.out.println(new Solution().orientation(x1, y1, x2, y2, x3, y3));\n"
        
    elif ptype == "poly_query":
        # Check specific Java file for method name if needed, assuming standard naming
        code += "        int n = sc.nextInt();\n"
        code += "        long[] xs = new long[n];\n"
        code += "        long[] ys = new long[n];\n"
        code += "        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }\n"
        code += "        long qx = sc.nextLong(); long qy = sc.nextLong();\n"
        # Need to verify method name logic here. 
        # Typically "pointInPolygon" or similar.
        # I'll rely on reading the file content for method name? No, safer to assume single public method or standard solution class structure.
        # Let's assume the method name is "solve" or derived from problem.
        # But wait, GEO-001 was "orientation". 
        # I'll instantiate Solution and call the first non-Standard method?
        # Or Just hardcode heavily based on typical names.
        code += "        System.out.println(new Solution().pointInPolygon(n, xs, ys, qx, qy));\n"
        
    elif ptype == "segments":
        code += "        int m = sc.nextInt();\n"
        code += "        long[] x1 = new long[m]; long[] y1 = new long[m];\n"
        code += "        long[] x2 = new long[m]; long[] y2 = new long[m];\n"
        code += "        for(int i=0; i<m; i++) {\n"
        code += "            x1[i] = sc.nextLong(); y1[i] = sc.nextLong();\n"
        code += "            x2[i] = sc.nextLong(); y2[i] = sc.nextLong();\n"
        code += "        }\n"
        code += "        System.out.println(new Solution().countIntersections(x1, y1, x2, y2));\n"

    elif ptype == "points_ret_int" or ptype == "points_ret_points" or ptype == "points_ret_circle":
        code += "        int n = sc.nextInt();\n"
        code += "        long[] xs = new long[n];\n"
        code += "        long[] ys = new long[n];\n"
        code += "        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }\n"
        
        if ptype == "points_ret_int":
            method = "closestPair" if "004" in problem_id else "polygonArea" if "006" in problem_id else "diameter" if "007" in problem_id else "manhattanMST"
            code += f"        System.out.println(new Solution().{method}(xs, ys));\n"
        elif ptype == "points_ret_points":
            code += "        List<long[]> res = new Solution().sortByAngle(xs, ys);\n" # GEO-014
            code += "        for(long[] p : res) System.out.println(p[0] + \" \" + p[1]);\n"
        elif ptype == "points_ret_circle":
            code += "        double[] res = new Solution().minEnclosingCircle(xs, ys);\n"
            code += "        System.out.printf(\"%.6f\\n%.6f\\n%.6f\\n\", res[0], res[1], res[2]);\n"

    elif ptype == "points_theta":
        code += "        int n = sc.nextInt();\n"
        code += "        long[] xs = new long[n];\n"
        code += "        long[] ys = new long[n];\n"
        code += "        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }\n"
        code += "        int theta = sc.nextInt();\n"
        code += "        List<long[]> res = new Solution().cappedHull(xs, ys, theta);\n"
        code += "        System.out.println(res.size());\n"
        code += "        for(long[] p : res) System.out.println(p[0] + \" \" + p[1]);\n"
        
    elif ptype == "halfplanes":
        code += "        int m = sc.nextInt();\n"
        code += "        long[] A = new long[m]; long[] B = new long[m]; long[] C = new long[m];\n"
        code += "        for(int i=0; i<m; i++) { A[i] = sc.nextLong(); B[i] = sc.nextLong(); C[i] = sc.nextLong(); }\n"
        code += "        List<double[]> res = new Solution().halfPlaneIntersection(A, B, C);\n"
        code += "        if(res.isEmpty()) System.out.println(\"EMPTY\");\n"
        code += "        else {\n"
        code += "            System.out.println(res.size());\n"
        code += "            for(double[] p : res) System.out.printf(\"%.6f %.6f\\n\", p[0], p[1]);\n"
        code += "        }\n"

    elif ptype == "rects_weighted":
        code += "        int m = sc.nextInt();\n"
        code += "        int W = sc.nextInt();\n"
        code += "        long[] x1 = new long[m]; long[] y1 = new long[m];\n"
        code += "        long[] x2 = new long[m]; long[] y2 = new long[m]; long[] w = new long[m];\n"
        code += "        for(int i=0; i<m; i++) {\n"
        code += "            x1[i] = sc.nextLong(); y1[i] = sc.nextLong();\n"
        code += "            x2[i] = sc.nextLong(); y2[i] = sc.nextLong(); w[i] = sc.nextLong();\n"
        code += "        }\n"
        code += "        System.out.println(new Solution().weightedArea(x1, y1, x2, y2, w, W));\n"
        
    elif ptype == "rects":
        code += "        int m = sc.nextInt();\n"
        code += "        long[] x1 = new long[m]; long[] y1 = new long[m];\n"
        code += "        long[] x2 = new long[m]; long[] y2 = new long[m];\n"
        code += "        for(int i=0; i<m; i++) {\n"
        code += "            x1[i] = sc.nextLong(); y1[i] = sc.nextLong();\n"
        code += "            x2[i] = sc.nextLong(); y2[i] = sc.nextLong();\n"
        code += "        }\n"
        code += "        System.out.println(new Solution().maxOverlap(x1, y1, x2, y2));\n"

    elif ptype == "rect_points":
        code += "        long xL = sc.nextLong(); long yB = sc.nextLong();\n"
        code += "        long xR = sc.nextLong(); long yT = sc.nextLong();\n"
        code += "        int n = sc.nextInt();\n"
        code += "        long[] xs = new long[n]; long[] ys = new long[n];\n"
        code += "        for(int i=0; i<n; i++) { xs[i] = sc.nextLong(); ys[i] = sc.nextLong(); }\n"
        code += "        System.out.printf(\"%.6f\\n\", new Solution().largestEmptyCircle(xL, yB, xR, yT, xs, ys));\n"

    elif ptype == "seg_point":
        code += "        long x1 = sc.nextLong(); long y1 = sc.nextLong();\n"
        code += "        long x2 = sc.nextLong(); long y2 = sc.nextLong();\n"
        code += "        long px = sc.nextLong(); long py = sc.nextLong();\n"
        code += "        System.out.printf(\"%.6f\\n\", new Solution().distance(x1, y1, x2, y2, px, py));\n"

    return code

def fix_file(id, lang, fpath):
    if not os.path.exists(fpath):
        return
    with open(fpath, 'r') as f:
        content = f.read()

    meta = METADATA.get(id)
    if not meta: return

    if lang == "java":
        if "public class Main" in content: return # Already fixed?
        content = content.replace("package ", "// package ")
        content = re.sub(r'public class \w+', 'static class Solution', content)
        content = content.replace("class Solution", "static class Solution")
        
        main_body = get_java_main(meta["type"], id)
        
        new_content = "import java.util.*;\nimport java.io.*;\n\n"
        new_content += "public class Main {\n"
        new_content += content + "\n"
        new_content += "    public static void main(String[] args) throws IOException {\n"
        new_content += main_body
        new_content += "    }\n"
        new_content += "}\n"
        
        with open(fpath, 'w') as f:
            f.write(new_content)

    elif lang == "cpp":
        if "int main()" in content: return
        content = content.replace("#include <bits/stdc++.h>", "")
        
        headers = "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <cmath>\n#include <iomanip>\n#include <string>\nusing namespace std;\n\n"
        
        # We need to construct main based on function call.
        # This is harder for C++ without knowing signature.
        # I'll rely on the fact that I can just append main if I know the function name.
        func = meta.get("cpp_func", "solve")
        
        main_code = "int main() {\n    ios::sync_with_stdio(false); cin.tie(nullptr);\n"
        ptype = meta["type"]
        
        if ptype == "triplet":
            main_code += "    long long x1,y1,x2,y2,x3,y3;\n"
            main_code += "    if(cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3) cout << " + func + "(x1,y1,x2,y2,x3,y3) << endl;\n"
        elif ptype == "poly_query": # GEO-002
            main_code += "    int n; cin >> n;\n    vector<long long> xs(n), ys(n);\n"
            main_code += "    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];\n"
            main_code += "    long long qx, qy; cin >> qx >> qy;\n"
            main_code += "    cout << " + func + "(n, xs, ys, qx, qy) << endl;\n"
        elif ptype == "segments":
            main_code += "    int m; cin >> m;\n    vector<long long> x1(m), y1(m), x2(m), y2(m);\n"
            main_code += "    for(int i=0; i<m; i++) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];\n"
            main_code += "    cout << " + func + "(x1, y1, x2, y2) << endl;\n"
        elif ptype.startswith("points"):
            main_code += "    int n; cin >> n;\n    vector<long long> xs(n), ys(n);\n"
            main_code += "    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];\n"
            if ptype == "points_theta":
                main_code += "    int theta; cin >> theta;\n"
                main_code += "    auto res = " + func + "(xs, ys, theta);\n"
                main_code += "    cout << res.size() << endl;\n"
                main_code += "    for(auto p : res) cout << p.first << \" \" << p.second << endl;\n"
            elif ptype == "points_ret_points": # GEO-014
                main_code += "    auto res = " + func + "(xs, ys);\n"
                main_code += "    for(auto p : res) cout << p.first << \" \" << p.second << endl;\n"
            elif ptype == "points_ret_circle": # GEO-008
                main_code += "    auto res = " + func + "(xs, ys);\n"
                main_code += "    cout << fixed << setprecision(6) << res[0] << endl << res[1] << endl << res[2] << endl;\n"
            else:
                 main_code += "    cout << " + func + "(xs, ys) << endl;\n"
        elif ptype == "halfplanes":
            main_code += "    int m; cin >> m;\n    vector<long long> A(m), B(m), C(m);\n"
            main_code += "    for(int i=0; i<m; i++) cin >> A[i] >> B[i] >> C[i];\n"
            main_code += "    auto res = " + func + "(A, B, C);\n"
            main_code += "    if(res.empty()) cout << \"EMPTY\" << endl;\n"
            main_code += "    else {\n        cout << res.size() << endl;\n        cout << fixed << setprecision(6);\n"
            main_code += "        for(auto p : res) cout << p.first << \" \" << p.second << endl;\n    }\n"
        elif ptype == "rects_weighted":
             main_code += "    int m, W; cin >> m >> W;\n"
             main_code += "    vector<long long> x1(m), y1(m), x2(m), y2(m), w(m);\n"
             main_code += "    for(int i=0; i<m; i++) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i] >> w[i];\n"
             main_code += "    cout << " + func + "(x1, y1, x2, y2, w, W) << endl;\n"
        elif ptype == "rects":
             main_code += "    int m; cin >> m;\n"
             main_code += "    vector<long long> x1(m), y1(m), x2(m), y2(m);\n"
             main_code += "    for(int i=0; i<m; i++) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];\n"
             main_code += "    cout << " + func + "(x1, y1, x2, y2) << endl;\n"
        elif ptype == "rect_points":
             main_code += "    long long xL, yB, xR, yT; cin >> xL >> yB >> xR >> yT;\n"
             main_code += "    int n; cin >> n; vector<long long> xs(n), ys(n);\n"
             main_code += "    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];\n"
             main_code += "    cout << fixed << setprecision(6) << " + func + "(xL, yB, xR, yT, xs, ys) << endl;\n"
        elif ptype == "seg_point":
             main_code += "    long long x1, y1, x2, y2, px, py; cin >> x1 >> y1 >> x2 >> y2 >> px >> py;\n"
             main_code += "    cout << fixed << setprecision(6) << " + func + "(x1, y1, x2, y2, px, py) << endl;\n"

        main_code += "    return 0;\n}\n"
        
        with open(fpath, 'w') as f:
            f.write(headers + content + "\n" + main_code)

    elif lang == "javascript":
        if "readline" in content or "process.stdin" in content: return
        
        func = meta.get("js_func", "solve")
        ptype = meta["type"]
        
        wrapper = "const readline = require('readline');\n\n"
        wrapper += content + "\n\n"
        wrapper += "const rl = readline.createInterface({ input: process.stdin, output: process.stdout });\n"
        wrapper += "let lines = [];\n"
        wrapper += "rl.on('line', (line) => { lines.push(...line.trim().split(/\s+/)); });\n"
        wrapper += "rl.on('close', () => {\n"
        wrapper += "    if (lines.length === 0) return;\n"
        wrapper += "    let idx = 0;\n"
        wrapper += "    const next = () => lines[idx++];\n    const nextInt = () => parseInt(next());\n    const nextFloat = () => parseFloat(next());\n" # Using number parse
        
        # JS parsing logic
        if ptype == "triplet":
            wrapper += f"    console.log({func}(nextInt(), nextInt(), nextInt(), nextInt(), nextInt(), nextInt()));\n"
        elif ptype == "poly_query":
            wrapper += "    let n = nextInt();\n    let xs = [], ys = [];\n"
            wrapper += "    for(let i=0; i<n; i++) { xs.push(nextInt()); ys.push(nextInt()); }\n"
            wrapper += f"    console.log({func}(n, xs, ys, nextInt(), nextInt()));\n"
        elif ptype == "segments":
            wrapper += "    let m = nextInt();\n    let x1=[], y1=[], x2=[], y2=[];\n"
            wrapper += "    for(let i=0; i<m; i++) { x1.push(nextInt()); y1.push(nextInt()); x2.push(nextInt()); y2.push(nextInt()); }\n"
            wrapper += f"    console.log({func}(x1, y1, x2, y2));\n"
        elif ptype.startswith("points"):
            wrapper += "    let n = nextInt();\n    let xs = [], ys = [];\n"
            wrapper += "    for(let i=0; i<n; i++) { xs.push(nextInt()); ys.push(nextInt()); }\n"
            if ptype == "points_theta":
                wrapper += f"    let res = {func}(xs, ys, nextInt());\n"
                wrapper += "    console.log(res.length);\n    res.forEach(p => console.log(p.join(' ')));\n"
            elif ptype == "points_ret_points":
                wrapper += f"    let res = {func}(xs, ys);\n    res.forEach(p => console.log(p.join(' ')));\n"
            elif ptype == "points_ret_circle":
                wrapper += f"    let res = {func}(xs, ys);\n    console.log(res[0].toFixed(6)); console.log(res[1].toFixed(6)); console.log(res[2].toFixed(6));\n"
            else:
                wrapper += f"    console.log({func}(xs, ys));\n"
        elif ptype == "halfplanes":
            wrapper += "    let m = nextInt();\n    let A=[], B=[], C=[];\n"
            wrapper += "    for(let i=0; i<m; i++) { A.push(nextInt()); B.push(nextInt()); C.push(nextInt()); }\n"
            wrapper += f"    let res = {func}(A, B, C);\n"
            wrapper += "    if(!res || res.length === 0) console.log('EMPTY');\n"
            wrapper += "    else { console.log(res.length); res.forEach(p => console.log(p[0].toFixed(6) + ' ' + p[1].toFixed(6))); }\n"
        elif ptype == "rects_weighted":
            wrapper += "    let m = nextInt(), W = nextInt();\n"
            wrapper += "    let x1=[], y1=[], x2=[], y2=[], w=[];\n"
            wrapper += "    for(let i=0; i<m; i++) { x1.push(nextInt()); y1.push(nextInt()); x2.push(nextInt()); y2.push(nextInt()); w.push(nextInt()); }\n"
            wrapper += f"    console.log({func}(x1, y1, x2, y2, w, W));\n"
        elif ptype == "rects":
            wrapper += "    let m = nextInt();\n"
            wrapper += "    let x1=[], y1=[], x2=[], y2=[];\n"
            wrapper += "    for(let i=0; i<m; i++) { x1.push(nextInt()); y1.push(nextInt()); x2.push(nextInt()); y2.push(nextInt()); }\n"
            wrapper += f"    console.log({func}(x1, y1, x2, y2));\n"
        elif ptype == "rect_points":
            wrapper += "    let xL=nextInt(), yB=nextInt(), xR=nextInt(), yT=nextInt();\n"
            wrapper += "    let n = nextInt();\n    let xs = [], ys = [];\n"
            wrapper += "    for(let i=0; i<n; i++) { xs.push(nextInt()); ys.push(nextInt()); }\n"
            wrapper += f"    console.log({func}(xL, yB, xR, yT, xs, ys).toFixed(6));\n"
        elif ptype == "seg_point":
            wrapper += f"    console.log({func}(nextInt(), nextInt(), nextInt(), nextInt(), nextInt(), nextInt()).toFixed(6));\n"

        wrapper += "});\n"
        
        with open(fpath, 'w') as f:
            f.write(wrapper)

def main():
    for pid in METADATA:
        # if pid == "GEO-015": continue
        print(f"Fixing {pid}...")
        fix_file(pid, "java", os.path.join(SOLUTIONS_DIR, "java", f"{pid}*.java"))
        # Wildcard expansion needed? Yes, but simple path join won't work with *.
        # Use glob.
        import glob
        
        for lang in ["java", "cpp", "javascript"]:
             ext = "py" if lang=="python" else "js" if lang=="javascript" else lang
             pattern = os.path.join(SOLUTIONS_DIR, lang, f"{pid}*.{ext}")
             files = glob.glob(pattern)
             if files:
                 fix_file(pid, lang, files[0])
             else:
                 print(f"Warning: No file found for {pid} in {lang}")

if __name__ == "__main__":
    main()
