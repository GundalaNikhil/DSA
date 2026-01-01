import os
import re

SKIP_PROBLEMS = []

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
REC_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Strings", "solutions")

def parse_cpp_signature(content):
    # Heuristic: Find method in Solution class
    # Regex for method: type name(args)
    # We look for public: ... or just indentation in Solution
    
    # We want to capture return type, method name, and args list
    # e.g. long long countPaths(int r, int c)
    # vector<string> generatePermutations(string s)
    
    match = re.search(r'public:\s+([\w<>: ,]+)\s+(\w+)\s*\(([^)]*)\)', content, re.MULTILINE | re.DOTALL)
    if not match:
        match = re.search(r'class Solution\s*\{.*?(?:public:)?\s*([\w<>: ,]+)\s+(\w+)\s*\(([^)]*)\)', content, re.MULTILINE | re.DOTALL)
    
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
            if char == '<':
                depth += 1
                current += char
            elif char == '>':
                depth -= 1
                current += char
            elif char == ',' and depth == 0:
                parts.append(current)
                current = ""
                continue
            else:
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
    
    # Heuristic: 1 string arg -> read all
    if len(info['args']) == 1 and info['args'][0][0] == "string":
        aname = info['args'][0][1]
        # code += f"    string {aname}; {{ char buf[1000000]; if(cin.read(buf, sizeof(buf))) {aname} = string(buf, cin.gcount()); else {aname} = \"\"; }} \n" 
        # Better: use string assign from istreambuf_iterator?
        # code += f"    string {aname}((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());\n"
        # But allow trimming? Python .strip(). 
        # Let's use simple getline loop or iterator.
        # Iterator approach reads ALL.
        code = "\nint main() {\n    ios::sync_with_stdio(false); cin.tie(nullptr);\n"
        code += f"    string {aname}((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());\n"
        # Strip trailing newline/space for consistency with Python .strip()?
        code += f"    while(!{aname}.empty() && isspace({aname}.back())) {aname}.pop_back();\n"
        code += f"    while(!{aname}.empty() && isspace({aname}.front())) {aname}.erase(0, 1);\n" # slightly inefficient but ok
        call_args.append(aname)
    else:
        for atype, aname in info['args']:
            print(f"DEBUG: Problem {info['method_name']} Arg {aname} Type '{atype}'")
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
            elif "unordered_set<string>" in atype or "set<string>" in atype:
                code += f"    int {aname}_n; cin >> {aname}_n; {atype} {aname}; for(int i=0; i<{aname}_n; i++) {{ string s; cin >> s; {aname}.insert(s); }}\n"
            call_args.append(aname)
        
    call_expr = f"sol.{info['method_name']}({', '.join(call_args)})"
    
    ret = info['ret_type']
    printer = ""
    # Check complex first
    if "vector<vector<string>>" in ret:
         printer = f"vector<vector<string>> res = {call_expr}; for(const auto& row : res) {{ for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?\"\":\" \"); cout << endl; }}"
    elif "vector<vector<int>>" in ret:
        printer = f"vector<vector<int>> res = {call_expr}; for(const auto& row : res) {{ for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?\"\":\" \"); cout << endl; }}"
    elif "pair<int, vector<string>>" in ret:
         printer = f"pair<int, vector<string>> res = {call_expr}; cout << res.first << endl; for(const string& s : res.second) cout << s << endl; if(res.second.empty()) cout << \"NONE\" << endl;"
    elif "pair<int, string>" in ret:
        printer = f"pair<int, string> res = {call_expr}; cout << res.first << endl; cout << res.second << endl;"
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
    
    # Heuristic: 1 string arg -> read all
    if len(info['args']) == 1 and info['args'][0][0] == "string":
        aname = info['args'][0][1]
        code += f"        String {aname} = sc.useDelimiter(\"\\\\A\").hasNext() ? sc.next() : \"\";\n"
        code += f"        {aname} = {aname}.trim();\n"
        call_args.append(aname)
    else:
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
            elif "unordered_set<string>" in atype or "set<string>" in atype:
                 code += f"        int {aname}_n = sc.nextInt();\n        Set<String> {aname} = new HashSet<>();\n        for(int i=0; i<{aname}_n; i++) {aname}.add(sc.next());\n"
            
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
    elif "pair<int, string>" in ret:
        # Assume Java returns Object[] {Integer, String}
        code += f"        Object[] res = {call};\n        System.out.println(res[0]);\n        System.out.println(res[1]);\n"
    elif "pair<int, vector<string>>" in ret:
        # Java solution returns Object[] {Integer, List<String>}
        code += f"        Object[] res = {call};\n"
        code += f"        System.out.println(res[0]);\n"
        code += f"        @SuppressWarnings(\"unchecked\")\n"
        code += f"        List<String> list = (List<String>)res[1];\n"
        code += f"        for(String s : list) System.out.println(s);\n"
        code += f"        if(list.isEmpty()) System.out.println(\"NONE\");\n"
    else:
         # Fallback
        code += f"        System.out.println({call});\n"
        
    code += "        sc.close();\n    }\n}\n"
    return code

def generate_js_main(info, use_class=True):
    # Heuristic: 1 string arg -> read all
    if len(info['args']) == 1 and info['args'][0][0] == "string":
        aname = info['args'][0][1]
        code = f"\n\nconst fs = require('fs');\nconst {aname} = fs.readFileSync(0, 'utf-8').trim();\n"
        # No loop over tokens.
        
        call_args = [aname]
        if use_class:
            code += "const sol = new Solution();\n"
            call = f"sol.{info['method_name']}({', '.join(call_args)})"
        else:
            call = f"{info['method_name']}({', '.join(call_args)})"
            
        ret = info['ret_type']
        if "pair<int, string>" in ret:
             code += f"const res = {call};\nconsole.log(res[0]);\nconsole.log(res[1]);\n"
        elif "pair<int, vector<string>>" in ret:
             code += f"const res = {call};\nconsole.log(res[0]);\nif(res[1].length > 0) {{ for(const s of res[1]) console.log(s); }} else {{ console.log('NONE'); }}\n"
        elif ret == "bool":
             code += f"console.log({call} ? 'true' : 'false');\n"
        else:
             code += f"console.log({call});\n"
        return code

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
        elif "unordered_set<string>" in atype or "set<string>" in atype:
             code += f"    const {aname}_n = parseInt(tokens[ptr++]);\n    const {aname} = new Set();\n    for(let i=0; i<{aname}_n; i++) {aname}.add(tokens[ptr++]);\n"
        
        call_args.append(aname)
        
    if use_class:
        code += "    const sol = new Solution();\n"
        call = f"sol.{info['method_name']}({', '.join(call_args)})"
    else:
        call = f"{info['method_name']}({', '.join(call_args)})"
    
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
    elif "pair<int, vector<string>>" in ret:
        code += f"    const res = {call};\n    console.log(res[0]);\n    if(res[1].length > 0) {{ for(const s of res[1]) console.log(s); }} else {{ console.log('NONE'); }}\n"
    elif "pair<int, string>" in ret:
        code += f"    const res = {call};\n    console.log(res[0]);\n    console.log(res[1]);\n"
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
            if "#include <vector>" not in content:
                content = "#include <vector>\n" + content
            if "#include <string>" not in content:
                content = "#include <string>\n" + content
            if "#include <algorithm>" not in content:
                content = "#include <algorithm>\n" + content
            if "#include <unordered_set>" not in content:
                content = "#include <unordered_set>\n" + content
            if "#include <unordered_map>" not in content:
                content = "#include <unordered_map>\n" + content
            if "#include <set>" not in content:
                content = "#include <set>\n" + content
            if "#include <map>" not in content:
                content = "#include <map>\n" + content
            if "using namespace std;" not in content:
                content = "using namespace std;\n\n" + content
            
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
                
                # Check imports
                if "import java.util" not in jcontent:
                     jcontent = "import java.util.*;\n\n" + jcontent
                
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
                if "require('fs')" in jcontent:
                    jcontent = jcontent.split("const fs = require('fs')")[0]
                
                # REPAIR LOGIC: Undo the broken wrapper
                # Pattern: class Solution {\n    function ... OR class Solution {\n    class ...
                # If content has class Solution, check if it looks broken (has 'function ' or doubled indentation)
                pattern_broken = False
                if "class Solution {\n    function" in jcontent: pattern_broken = True
                if "class Solution {\n    class" in jcontent: pattern_broken = True
                if "class Solution" in jcontent and "function " in jcontent.split("class Solution")[1]: pattern_broken = True

                if pattern_broken:
                    # Strip first line "class Solution {"
                    # Strip last "}" from content (before driver was stripped)
                    # Unindent 4 spaces
                    lines = jcontent.split('\n')
                    if lines[0].strip().startswith("class Solution"):
                        lines = lines[1:] # Drop first
                    
                    # Drop last closing brace if it looks like the wrapper's
                    if lines and lines[-1].strip() == "}":
                         lines = lines[:-1]
                    elif lines and lines[-1].strip() == "":
                         while lines and lines[-1].strip() == "": lines.pop()
                         if lines and lines[-1].strip() == "}": lines.pop()
                    
                    # Unindent
                    new_lines = []
                    for line in lines:
                        if line.startswith("    "):
                            new_lines.append(line[4:])
                        else:
                            new_lines.append(line)
                    jcontent = "\n".join(new_lines) + "\n"
                
                # Determine if we should use class or standalone
                use_class = False
                if "class Solution" in jcontent and "function" not in jcontent.split("class Solution")[1]:
                     # If class Solution exists AND it doesn't look like our broken wrapper (checked above, but double check)
                     # Real class methods don't have 'function' keyword
                     use_class = True
                
                jsmain = generate_js_main(sig, use_class=use_class)
                with open(js_path, 'w') as out:
                    out.write(jcontent + jsmain)
                print(f"Fixed JS {js_name}")

if __name__ == "__main__":
    main()
