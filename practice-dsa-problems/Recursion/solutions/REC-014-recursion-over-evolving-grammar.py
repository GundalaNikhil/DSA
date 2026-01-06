import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    start_symbol = input_data[ptr]
    ptr += 1
    r_count = int(input_data[ptr])
    ptr += 1
    rules = {}
    current_rule_idx = {}
    for _ in range(r_count):
        nt = input_data[ptr]
        ptr += 1
        k = int(input_data[ptr])
        ptr += 1
        r_list = []
        for _ in range(k):
            r_list.append(input_data[ptr])
            ptr += 1
        rules[nt] = r_list
        current_rule_idx[nt] = 0
        
    l_max = int(input_data[ptr])
    ptr += 1
    
    stack = [start_symbol]
    final_chars = []
    
    while stack:
        symbol = stack.pop()
        
        if "a" <= symbol <= "z":
            final_chars.append(symbol)
            if len(final_chars) > l_max:
                print("TOO_LONG")
                return
        elif "A" <= symbol <= "Z":
            if symbol in rules:
                idx = current_rule_idx[symbol]
                production = rules[symbol][idx]
                current_rule_idx[symbol] = (idx + 1) % len(rules[symbol])
                
                # Push production in reverse order so first char is popped first
                for i in range(len(production) - 1, -1, -1):
                    stack.append(production[i])
                    
    print("".join(final_chars))
if __name__ == "__main__":
    solve()