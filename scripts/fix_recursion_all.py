import os
import re

SKIP_PROBLEMS = ["REC-003", "REC-006", "REC-005", "REC-011", "REC-008", "REC-007", "REC-004", "REC-009", "REC-012", "REC-013", "REC-014", "REC-015"]

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
REC_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Recursion", "solutions")

def parse_cpp_signature(content):
    # Heuristic: Find method in Solution class
    # Regex for method: type name(args)
    # We look for public: ... or just indentation in Solution
    
    # We want to capture return type, method name, and args list
    # e.g. long long countPaths(int r, int c)
    # vector<string> generatePermutations(string s)
    
    match = re.search(r'public:\s+([\w<>: ]+)\s+(\w+)\s*\(([^)]*)\)', content, re.MULTILINE | re.DOTALL)
    if not match:
        match = re.search(r'class Solution\s*\{.*?(?:public:)?\s*([\w<>: ]+)\s+(\w+)\s*\(([^)]*)\)', content, re.MULTILINE | re.DOTALL)
    
    if not match: return None
    
    ret_type = match.group(1).strip()
    method_name = match.group(2).strip()
    args_str = match.group(3).strip()
    
    args = []
    if args_str:
        # Split by comma but respect brackets
        parts = []
        depth = 0
        current = ""
        for char in args_str:
            if char == '<': depth += 1
            elif char == '>': depth -= 1
            elif char == ',' and depth == 0:
                parts.append(current)
                current = ""
                continue
            current += char
        if current: parts.append(current)
        
        for p in parts:
            p = p.strip()
            if not p: continue
            # type name
            # last word is name
            # handle 'const string& s' -> type='string', name='s' roughly
            # regex: (.*?)[\s&*]+(\w+)$
            arg_match = re.search(r'(.*?)[\s&*]+(\w+)$', p)
            if arg_match:
                base_type = arg_match.group(1).strip()
                name = arg_match.group(2).strip()
                # Clean const
                base_type = base_type.replace('const', '').strip()
                args.append((base_type, name))
    
    return {
        'ret_type': ret_type,
        'method_name': method_name,
        'args': args
    }

def generate_cpp_main(info):
    code = "\nint main() {\n    ios::sync_with_stdio(false); cin.tie(nullptr);\n"
    call_args = []
    
    for atype, aname in info['args']:
        if atype == "int":
            code += f"    int {aname}; cin >> {aname};\n"
        elif atype == "long long":
            code += f"    long long {aname}; cin >> {aname};\n"
        elif atype == "string":
            code += f"    string {aname}; cin >> {aname};\n"
        elif "vector<vector<int>>" in atype: # e.g. vector<vector<int>> grid
             code += f"    int {aname}_r, {aname}_c; cin >> {aname}_r >> {aname}_c; vector<vector<int>> {aname}({aname}_r, vector<int>({aname}_c)); for(int i=0; i<{aname}_r; i++) for(int j=0; j<{aname}_c; j++) cin >> {aname}[i][j];\n"
        elif "vector<pair<int" in atype: 
             # Assume vector<pair<int,int>>
             code += f"    int {aname}_n; cin >> {aname}_n; vector<pair<int,int>> {aname}({aname}_n); for(int i=0; i<{aname}_n; i++) cin >> {aname}[i].first >> {aname}[i].second;\n"
        elif "vector<int>" in atype:
            code += f"    int {aname}_n; cin >> {aname}_n; vector<int> {aname}({aname}_n); for(int i=0; i<{aname}_n; i++) cin >> {aname}[i];\n"
        elif "vector<string>" in atype:
            code += f"    int {aname}_n; cin >> {aname}_n; vector<string> {aname}({aname}_n); for(int i=0; i<{aname}_n; i++) cin >> {aname}[i];\n"
        call_args.append(aname)
        
    call_expr = f"sol.{info['method_name']}({', '.join(call_args)})"
    
    ret = info['ret_type']
    printer = ""
    # Check complex first
    if "vector<vector<string>>" in ret:
         printer = f"vector<vector<string>> res = {call_expr}; for(const auto& row : res) {{ for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?\"\":\" \"); cout << endl; }}"
    elif "vector<vector<int>>" in ret:
        printer = f"vector<vector<int>> res = {call_expr}; for(const auto& row : res) {{ for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?\"\":\" \"); cout << endl; }}"
    elif "vector<string>" in ret:
        printer = f"vector<string> res = {call_expr}; for(const string& s : res) cout << s << endl; if(res.empty()) cout << \"NONE\" << endl;"
    elif "vector<pair<int" in ret:
        printer = f"vector<pair<int,int>> res = {call_expr}; for(const auto& p : res) cout << p.first << \" \" << p.second << endl; if(res.empty()) cout << \"NONE\" << endl;"
    elif "vector<int>" in ret:
        printer = f"vector<int> res = {call_expr}; for(size_t i=0; i<res.size(); i++) cout << res[i] << (i==res.size()-1?\"\":\" \"); cout << endl;"
    elif ret == "bool":
        printer = f"cout << ({call_expr} ? \"true\" : \"false\") << endl;"
    else:
        printer = f"cout << {call_expr} << endl;"
        
    code += f"    Solution sol;\n    {printer}\n    return 0;\n}}\n"
    return code

def generate_java_main(info):
    code = "\nclass Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n"
    call_args = []
    
    for atype, aname in info['args']:
        if atype == "int":
            code += f"        int {aname} = sc.nextInt();\n"
        elif atype == "long long":
            code += f"        long {aname} = sc.nextLong();\n"
        elif atype == "string":
            code += f"        String {aname} = sc.next();\n"
        elif "vector<vector<int>>" in atype: # unlikely in input? but for grid
             code += f"        int {aname}_r = sc.nextInt();\n        int {aname}_c = sc.nextInt();\n        int[][] {aname} = new int[{aname}_r][{aname}_c];\n        for(int i=0; i<{aname}_r; i++) for(int j=0; j<{aname}_c; j++) {aname}[i][j] = sc.nextInt();\n"
             # Wait, Java solution usually expects int[][] or List<List<Integer>> for Grid.
             # REC-005 Java likely expects int[][]. My generator assumes List for Vector.
             # But Solution arg type in Java file matches. if I just pass int[][], and Solution expects int[][], good.
             # The problem is my Java parsing logic inferred from C++ 'vector<vector<int>>'.
             # I should probably inspect Java file to confirm types but assuming int[][] for grid is standard.
        elif "vector<pair<int" in atype:
             # Edges list? List<int[]> or int[][]? 
             # REC-011 Java expects 'int[][] edges'? or List<int[]>?
             # Usually int[][] edges.
             code += f"        int {aname}_n = sc.nextInt();\n        int[][] {aname} = new int[{aname}_n][2];\n        for(int i=0; i<{aname}_n; i++) {{ {aname}[i][0] = sc.nextInt(); {aname}[i][1] = sc.nextInt(); }}\n"
        elif "vector<int>" in atype:
            code += f"        int {aname}_n = sc.nextInt();\n        List<Integer> {aname} = new ArrayList<>();\n        for(int i=0; i<{aname}_n; i++) {aname}.add(sc.nextInt());\n"
        elif "vector<string>" in atype:
             code += f"        int {aname}_n = sc.nextInt();\n        List<String> {aname} = new ArrayList<>();\n        for(int i=0; i<{aname}_n; i++) {aname}.add(sc.next());\n"
        
        # Adding to call args.
        call_args.append(aname)

    # Make call
    # Need to instantiate Solution
    code += "        Solution sol = new Solution();\n"
    
    # Return printing
    ret = info['ret_type']
    call = f"sol.{info['method_name']}({', '.join(call_args)})"
    
    # Check if return type likely maps to List or Array
    if "vector<vector<string>>" in ret:
         code += f"        List<List<String>> res = {call};\n"
         code += f"        for(List<String> row : res) {{ for(int i=0; i<row.size(); i++) System.out.print(row.get(i) + (i==row.size()-1?\"\":\" \")); System.out.println(); }}\n"
    elif "vector<vector<int>>" in ret: 
        code += f"        List<List<Integer>> res = {call};\n"
        code += f"        for(List<Integer> row : res) {{ for(int i=0; i<row.size(); i++) System.out.print(row.get(i) + (i==row.size()-1?\"\":\" \")); System.out.println(); }}\n"
    elif "vector<string>" in ret:
        code += f"        List<String> res = {call};\n        for(String out_s : res) System.out.println(out_s);\n        if(res.isEmpty()) System.out.println(\"NONE\");\n"
    elif "vector<int>" in ret:
        code += f"        List<Integer> res = {call};\n        for(int i=0; i<res.size(); i++) System.out.print(res.get(i) + (i==res.size()-1?\"\":\" \")); System.out.println();\n"
    else:
         # Fallback
        code += f"        System.out.println({call});\n"
        
    code += "        sc.close();\n    }\n}\n"
    return code

def generate_js_main(info):
    code = "\n\nconst readline = require('readline');\nconst rl = readline.createInterface({ input: process.stdin, output: process.stdout });\nlet tokens = [];\nrl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });\nrl.on('close', () => {\n    if(tokens.length===0) return;\n    let ptr = 0;\n"
    
    call_args = []
    
    for atype, aname in info['args']:
        if atype == "int":
            code += f"    const {aname} = parseInt(tokens[ptr++]);\n"
        elif atype == "long long":
            code += f"    const {aname} = Number(tokens[ptr++]);\n"
        elif atype == "string":
            code += f"    const {aname} = tokens[ptr++];\n"
        elif "vector<vector<int>>" in atype:
             code += f"    const {aname}_r = parseInt(tokens[ptr++]);\n    const {aname}_c = parseInt(tokens[ptr++]);\n    const {aname} = Array.from({{'length':{aname}_r}}, () => []);\n    for(let i=0; i<{aname}_r; i++) for(let j=0; j<{aname}_c; j++) {aname}[i].push(parseInt(tokens[ptr++]));\n"
        elif "vector<pair<int" in atype:
             code += f"    const {aname}_n = parseInt(tokens[ptr++]);\n    const {aname} = [];\n    for(let i=0; i<{aname}_n; i++) {aname}.push([parseInt(tokens[ptr++]), parseInt(tokens[ptr++])]);\n"
        elif "vector<int>" in atype:
            code += f"    const {aname}_n = parseInt(tokens[ptr++]);\n    const {aname} = [];\n    for(let i=0; i<{aname}_n; i++) {aname}.push(parseInt(tokens[ptr++]));\n"
        elif "vector<string>" in atype:
            code += f"    const {aname}_n = parseInt(tokens[ptr++]);\n    const {aname} = [];\n    for(let i=0; i<{aname}_n; i++) {aname}.push(tokens[ptr++]);\n"
        
        call_args.append(aname)
        
    code += "    const sol = new Solution();\n"
    call = f"sol.{info['method_name']}({', '.join(call_args)})"
    
    ret = info['ret_type']
    if "vector<vector<string>>" in ret:
        code += f"    const res = {call};\n    res.forEach(row => console.log(row.join(' ')));\n"
    elif "vector<vector<int>>" in ret:
        code += f"    const res = {call};\n    res.forEach(row => console.log(row.join(' ')));\n"
    elif "vector<pair<int" in ret:
        code += f"    const res = {call};\n    if(res.length===0) console.log('NONE'); else res.forEach(p => console.log(p.join(' ')));\n"
    elif "vector<string>" in ret:
        code += f"    const res = {call};\n    if(res.length===0) console.log('NONE'); else res.forEach(s => console.log(s));\n"
    elif "vector<int>" in ret:
        code += f"    const res = {call};\n    console.log(res.join(' '));\n"
    else:
        code += f"    console.log({call});\n"
        
    code += "});\n"
    return code

def main():
    cpp_dir = os.path.join(REC_DIR, "cpp")
    java_dir = os.path.join(REC_DIR, "java")
    js_dir = os.path.join(REC_DIR, "javascript")
    
    signatures = {}
    
    # 1. Provide signatures from C++ files (read original content logic)
    # We must be careful not to parse the 'main' we just added. 
    # Better to read top of file.
    
    for f in os.listdir(cpp_dir):
        if not f.endswith(".cpp"): continue
        path = os.path.join(cpp_dir, f)
        with open(path, 'r') as file:
            content = file.read()
            
        # Strip existing main if present for clean parsing
        if "int main()" in content:
            content = content.split("int main()")[0]
            
        sig = parse_cpp_signature(content)
        if sig:
            problem_id = f.split('-')[0] + "-" + f.split('-')[1] # REC-001
            
            # Skip manual override problems
            is_skipped = False
            for skip_id in SKIP_PROBLEMS:
                if skip_id in f:
                    is_skipped = True
                    break
            if is_skipped:
                # print(f"Skipping {f} (Manual)")
                continue

            signatures[f] = sig # Map filename to sig
            
            # 2. Fix C++
            # Always rewrite C++ file with clean content + new main
            new_main = generate_cpp_main(sig)
            # Ensure headers
            if "#include <iostream>" not in content:
                content = "#include <iostream>\n" + content
            
            with open(path, 'w') as out:
                out.write(content + new_main)
            print(f"Fixed C++ {f}")
            
            # 3. Fix Java
            # Find corresponding Java file
            java_name = f.replace(".cpp", ".java")
            java_path = os.path.join(java_dir, java_name)
            if os.path.exists(java_path):
                with open(java_path, 'r') as jf:
                    jcontent = jf.read()
                if "class Main" in jcontent:
                    jcontent = jcontent.split("class Main")[0] # Strip old main
                
                # Java args adaptation for signature?
                # The C++ sig has 'int', 'vector<int>'. Java needs 'int', 'int[]' or 'List<Integer>'.
                # We'll rely on our generate_java_main to map logical types to standard Java IO code.
                # However, Solution method args must match. 
                # If Solution has 'countPaths(int r, int c)', generator makes 'int r = sc.nextInt()'. Correct.
                # If Solution has 'packCombinations(int[] vals)', generator makes 'int[] vals = ...'. Correct.
                # Only issue: List vs Array in Solution arguments.
                
                jmain = generate_java_main(sig)
                with open(java_path, 'w') as out:
                    out.write(jcontent + jmain)
                print(f"Fixed Java {java_name}")
            
            # 4. Fix JS
            js_name = f.replace(".cpp", ".js")
            js_path = os.path.join(js_dir, js_name)
            if os.path.exists(js_path):
                with open(js_path, 'r') as jf:
                   jcontent = jf.read()
                if "require('readline')" in jcontent:
                    jcontent = jcontent.split("const readline = require('readline')")[0]
                
                jsmain = generate_js_main(sig)
                with open(js_path, 'w') as out:
                    out.write(jcontent + jsmain)
                print(f"Fixed JS {js_name}")

if __name__ == "__main__":
    main()
