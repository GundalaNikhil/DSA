import os
import re

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA"
REC_DIR = os.path.join(DSA_ROOT, "dsa-problems", "Recursion", "solutions", "cpp")

def get_arg_reader(type_str, name):
    type_str = type_str.strip()
    if type_str == "int":
        return f"int {name}; cin >> {name};"
    elif type_str == "long long":
        return f"long long {name}; cin >> {name};"
    elif type_str == "string":
        return f"string {name}; cin >> {name};"
    elif "vector<int>" in type_str:
        return f"int {name}_n; cin >> {name}_n; vector<int> {name}({name}_n); for(int i=0; i<{name}_n; i++) cin >> {name}[i];"
    elif "vector<string>" in type_str:
        return f"int {name}_n; cin >> {name}_n; vector<string> {name}({name}_n); for(int i=0; i<{name}_n; i++) cin >> {name}[i];"
    elif "vector<vector<int>>" in type_str:
         return f"int {name}_r, {name}_c; cin >> {name}_r >> {name}_c; vector<vector<int>> {name}({name}_r, vector<int>({name}_c)); for(int i=0; i<{name}_r; i++) for(int j=0; j<{name}_c; j++) cin >> {name}[i][j];"
    return f"// UNKNOWN TYPE: {type_str} {name}"

def generate_printer(return_type, expr):
    return_type = return_type.strip()
    if return_type in ["int", "long long", "double", "string", "bool"]:
        if return_type == "bool":
             return f"cout << ({expr} ? \"true\" : \"false\") << endl;"
        return f"cout << {expr} << endl;"
    elif "vector<vector<int>>" in return_type:
        return f"vector<vector<int>> res = {expr}; for(const auto& row : res) {{ for(size_t i=0; i<row.size(); i++) cout << row[i] << (i==row.size()-1?\"\":\" \"); cout << endl; }}"
    elif "vector<string>" in return_type:
        return f"vector<string> res = {expr}; for(const string& s : res) cout << s << endl; if(res.empty()) cout << \"NONE\" << endl;"
    elif "vector<int>" in return_type:
        return f"vector<int> res = {expr}; for(size_t i=0; i<res.size(); i++) cout << res[i] << (i==res.size()-1?\"\":\" \"); cout << endl;"
    # Add more complex types if needed
    return f"// UNKNOWN RETURN: {return_type}\ncout << {expr} << endl;"

def process_file(path):
    with open(path, 'r') as f:
        content = f.read()
    
    if "int main()" in content:
        return
        
    # Find public method
    # heuristic: first method after "public:" or just a method that looks like solution
    
    # Regex for method: type name(args)
    # Exclude helper methods? Usually Solution has one public method.
    
    match = re.search(r'public:\s+([\w<>: ]+)\s+(\w+)\s*\(([^)]*)\)', content, re.MULTILINE | re.DOTALL)
    if not match:
        # Maybe struct?
        match = re.search(r'class Solution\s*\{.*?(?:public:)?\s*([\w<>: ]+)\s+(\w+)\s*\(([^)]*)\)', content, re.MULTILINE | re.DOTALL)
    
    if not match:
        print(f"Skipping {os.path.basename(path)}: No method found")
        return

    ret_type = match.group(1).strip()
    func_name = match.group(2).strip()
    args_str = match.group(3).strip()
    
    # Parse args
    args = []
    if args_str:
        # Split by comma but ignore commas in template types usually not an issue for simple args
        # But vector<int, alloc> might break. Assuming simple signatures.
        parts = args_str.split(',')
        for p in parts:
            p = p.strip()
            # type name
            # last word is name
            last_space = p.rfind(' ')
            if last_space == -1: 
                last_space = p.rfind('&') # int& n
            if last_space == -1: 
                last_space = p.rfind('*')
             
            # A bit hacky, cleaner regex:
            # ([\w<>: &*]+)\s+(\w+)
            arg_match = re.search(r'([\w<>: &*]+)\s+(\w+)$', p)
            if arg_match:
                atype = arg_match.group(1).strip()
                if atype.endswith('&'): atype = atype[:-1]
                aname = arg_match.group(2).strip()
                args.append((atype, aname))
            else:
                print(f"Warning: could not parse arg '{p}' in {os.path.basename(path)}")
    
    # Generate main
    main_code = "\nint main() {\n"
    # IO speedup
    main_code += "    ios::sync_with_stdio(false); cin.tie(nullptr);\n"
    
    call_args = []
    for atype, aname in args:
        main_code += "    " + get_arg_reader(atype, aname) + "\n"
        call_args.append(aname)
        
    call_expr = f"sol.{func_name}({', '.join(call_args)})"
    main_code += "    Solution sol;\n"
    main_code += "    " + generate_printer(ret_type, call_expr) + "\n"
    main_code += "    return 0;\n"
    main_code += "}\n"
    
    # Needs headers?
    if "<iostream>" not in content:
        content = "#include <iostream>\n" + content
    
    with open(path, 'w') as f:
        f.write(content + main_code)
        print(f"Updated {os.path.basename(path)}")

def main():
    for f in os.listdir(REC_DIR):
        if f.endswith(".cpp"):
            process_file(os.path.join(REC_DIR, f))

if __name__ == "__main__":
    main()
