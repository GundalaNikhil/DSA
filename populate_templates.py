
import os
import re
import sys

DSA_ROOT = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"

def get_return_value(type_str):
    type_str = type_str.lower()
    if 'void' in type_str:
        return '' 
    if 'int' in type_str or 'long' in type_str or 'double' in type_str or 'float' in type_str:
        return '0'
    if 'boolean' in type_str or 'bool' in type_str:
        return 'false'
    if 'string' in type_str:
        return '""'
    if 'list' in type_str or 'vector' in type_str or 'array' in type_str:
        return '[]' if 'val' not in type_str else 'new ...' 
    return 'null' 

def clean_whitespace(content):
    return re.sub(r'\n{3,}', '\n\n', content)

def hollow_python(content):
    lines = content.split('\n')
    new_lines = []
    
    function_indent = 0
    skip_until_indent_change = False
    
    for line in lines:
        stripped = line.strip()
        
        if not line or stripped.startswith('#') or stripped.startswith('import ') or stripped.startswith('from '):
            if not skip_until_indent_change:
                new_lines.append(line)
            continue
            
        indent = len(line) - len(line.lstrip())
        
        if skip_until_indent_change:
            if indent <= function_indent and stripped:
                skip_until_indent_change = False
            else:
                continue

        if 'def main():' in line or 'if __name__' in line:
            new_lines.append(line)
            continue
            
        if stripped.startswith('def '):
            if 'def main' not in stripped:
                new_lines.append(line)
                
                ret_val = '0' 
                if '->' in line:
                    ret_type = line.split('->')[1].strip().replace(':', '')
                    if 'list' in ret_type.lower(): ret_val = '[]'
                    elif 'none' in ret_type.lower(): ret_val = ''
                    elif 'bool' in ret_type.lower(): ret_val = 'False'
                    elif 'str' in ret_type.lower(): ret_val = '""'
                
                if ret_val:
                    new_lines.append(" " * (indent + 4) + f"return {ret_val}")
                else:
                    new_lines.append(" " * (indent + 4) + "pass")
                    
                skip_until_indent_change = True
                function_indent = indent
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    return clean_whitespace('\n'.join(new_lines))


def hollow_java(content):
    lines = content.split('\n')
    new_lines = []
    in_solution = False
    
    skip_mode = False
    brace_count = 0
    
    for line in lines:
        stripped = line.strip()
        
        if 'class Solution' in line:
            in_solution = True
            new_lines.append(line)
            continue
            
        if not in_solution:
            new_lines.append(line)
            continue
            
        method_match = re.match(r'\s*public\s+[\w<>[\]]+\s+\w+\s*\(.*\)\s*\{', line)
        
        if method_match:
            new_lines.append(line)
            
            parts = stripped.split()
            ret_type = "void"
            if len(parts) > 1:
                ret_type = parts[1]
                
            ret_val = '0'
            if 'void' in ret_type: ret_val = ''
            elif 'boolean' in ret_type: ret_val = 'false'
            elif 'List' in ret_type or '[]' in ret_type: ret_val = 'null' 
            elif 'String' in ret_type: ret_val = '""'
            
            if ret_val:
                new_lines.append("        return " + ret_val + ";")
            
            new_lines.append("    }") 
            
            skip_mode = True 
            brace_count = 1 
            continue
            
        if skip_mode:
            brace_count += line.count('{')
            brace_count -= line.count('}')
            if brace_count == 0:
                skip_mode = False
            continue
            
        new_lines.append(line)

    return clean_whitespace('\n'.join(new_lines))

def hollow_cpp(content):
    lines = content.split('\n')
    new_lines = []
    in_solution = False
    skip_mode = False
    brace_count = 0
    
    ignored_keywords = {'if', 'while', 'for', 'switch', 'catch', 'else'}
    
    for line in lines:
        stripped = line.strip()
        
        if 'class Solution' in line:
            in_solution = True
            new_lines.append(line)
            continue
            
        if not in_solution:
            new_lines.append(line)
            continue

        if 'public:' in line:
            new_lines.append(line)
            continue
            
        method_match = re.match(r'\s*([a-zA-Z0-9_<>:]+)\s+([a-zA-Z0-9_]+)\s*\(.*\)\s*\{', line)
        
        is_method = False
        name_part = ""
        if method_match:
            type_part = method_match.group(1)
            name_part = method_match.group(2)
            if type_part not in ignored_keywords and name_part not in ignored_keywords:
                is_method = True
        
        if is_method and 'class ' not in line and name_part != 'main': 
            new_lines.append(line)
            
            pre_paren = line.split('(')[0].strip()
            words = pre_paren.split()
            type_str = " ".join(words[:-1]) 
            
            ret_val = '0'
            if 'void' in type_str: ret_val = ''
            elif 'bool' in type_str: ret_val = 'false'
            elif 'string' in type_str: ret_val = '""'
            elif 'vector' in type_str: ret_val = '{}'
            
            if ret_val:
                new_lines.append("        return " + ret_val + ";")
                
            new_lines.append("    }")
            
            skip_mode = True
            brace_count = 1
            continue

        if skip_mode:
            brace_count += line.count('{')
            brace_count -= line.count('}')
            if brace_count <= 0:
                skip_mode = False
            continue
            
        new_lines.append(line)

    return clean_whitespace('\n'.join(new_lines))


def hollow_js(content):
    lines = content.split('\n')
    new_lines = []
    
    has_class_solution = 'class Solution' in content
    in_solution_class = False
    skip_mode = False
    brace_count = 0
    
    for line in lines:
        stripped = line.strip()
        
        if 'class Solution' in line:
            in_solution_class = True
            new_lines.append(line)
            continue
        
        if has_class_solution and not in_solution_class:
            if not skip_mode:
                new_lines.append(line)
            continue
            
        method_match = None
        is_function_kw = stripped.startswith('function ')
        
        if has_class_solution and in_solution_class:
             match = re.match(r'\s*([a-zA-Z0-9_]+)\s*\(.*\)\s*\{', line)
             if match:
                 if match.group(1) not in ['if', 'while', 'for', 'switch', 'catch', 'constructor']:
                     method_match = True
        elif not has_class_solution:
            if is_function_kw and '{' in line:
                method_match = True

        if method_match:
             new_lines.append(line)
             new_lines.append("    return 0;")
             new_lines.append("  }")
             
             skip_mode = True
             brace_count = 1
             continue
             
        if skip_mode:
            brace_count += line.count('{')
            brace_count -= line.count('}')
            if brace_count <= 0:
                skip_mode = False
            continue
             
        new_lines.append(line)
        
    return clean_whitespace('\n'.join(new_lines))


def process_section(section_name):
    section_path = os.path.join(DSA_ROOT, section_name)
    problems_dir = os.path.join(section_path, "problems")
    solutions_dir = os.path.join(section_path, "solutions")
    
    if not os.path.exists(problems_dir) or not os.path.exists(solutions_dir):
        return

    for filename in os.listdir(problems_dir):
        if not filename.endswith(".md"):
            continue
            
        prob_path = os.path.join(problems_dir, filename)
        prob_id = filename.replace(".md", "") 
        slug = prob_id
        
        replacements = {}
        langs = {
            'java': ('java', hollow_java),
            'python': ('py', hollow_python),
            'cpp': ('cpp', hollow_cpp),
            'javascript': ('js', hollow_js)
        }
        
        found_any_solution = False
        for lang_name, (ext, func) in langs.items():
            sol_path = os.path.join(solutions_dir, lang_name, f"{slug}.{ext}")
            
            if os.path.exists(sol_path):
                found_any_solution = True
                with open(sol_path, 'r') as f:
                    full_code = f.read()
                try:
                    hollowed = func(full_code)
                    replacements[lang_name] = hollowed
                except Exception as e:
                    print(f"Error hollowing {lang_name} for {slug}: {e}")
            else:
                pass
        
        if not found_any_solution:
            continue

        with open(prob_path, 'r') as f:
            md_content = f.read()
            
        ordered_langs = ['Java', 'Python', 'C++', 'JavaScript']
        key_map = {'Java': 'java', 'Python': 'python', 'C++': 'cpp', 'JavaScript': 'javascript'}
        
        new_template_section = "## Solution Template\n\n"
        
        for lang_title in ordered_langs:
            key = key_map[lang_title]
            if key in replacements:
                code_block_lang = key if key != 'cpp' else 'cpp'
                if key == 'javascript': code_block_lang = 'javascript'
                
                new_template_section += f"### {lang_title}\n\n"
                new_template_section += f"```{code_block_lang}\n"
                new_template_section += replacements[key].strip() + "\n"
                new_template_section += "```\n\n"

        if "## Solution Template" in md_content:
            parts = md_content.split("## Solution Template")
            preamble = parts[0]
            if not preamble.strip(): preamble = md_content 
            new_full_content = preamble + new_template_section
        else:
            if not md_content.endswith("\n"):
                md_content += "\n"
            new_full_content = md_content + "\n" + new_template_section
        
        with open(prob_path, 'w') as f:
            f.write(new_full_content)
        
        print(f"Updated {slug}")

def main():
    sections = [d for d in os.listdir(DSA_ROOT) if os.path.isdir(os.path.join(DSA_ROOT, d))]
    for section in sections:
        process_section(section)

if __name__ == "__main__":
    main()
