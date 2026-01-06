import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    q = int(input_data[ptr])
    ptr += 1
    
    rules = []
    for _ in range(q):
        rt = input_data[ptr]
        ptr += 1
        if rt.startswith("FILTER"):
            rules.append((rt, int(input_data[ptr])))
            ptr += 1
        else:
            rules.append((rt, int(input_data[ptr]), int(input_data[ptr])))
            ptr += 2
            
    # Apply rules
    for rule in rules:
        if rule[0] == "FILTER_LT":
            x = rule[1]
            vals = [v for v in vals if v >= x]
        elif rule[0] == "FILTER_EQ":
            x = rule[1]
            vals = [v for v in vals if v != x]
            
    inserts = []
    for rule in rules:
        if rule[0] == "INSERT_AFTER":
            inserts.append((rule[1], rule[2]))
            
    ins_map = {}
    for v_target, x_val in inserts:
        if v_target not in ins_map:
            ins_map[v_target] = []
        ins_map[v_target].append(x_val)
        
    final_list = []
    for v in vals:
        final_list.append(v)
        if v in ins_map:
            for x in ins_map[v]:
                final_list.append(x)
                
    print(*(final_list))


if __name__ == "__main__":
    solve()
