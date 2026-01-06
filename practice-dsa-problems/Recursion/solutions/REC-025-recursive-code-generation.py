import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    m_count = int(input_data[ptr])
    ptr += 1
    d_limit = int(input_data[ptr])
    ptr += 1
    a0 = int(input_data[ptr])
    ptr += 1
    MOD = 1_000_000_007
    macros = []
    for _ in range(m_count):
        length = int(input_data[ptr])
        ptr += 1
        tokens = []
        for _ in range(length):
            op = input_data[ptr]
            ptr += 1
            val = int(input_data[ptr])
            ptr += 1
            tokens.append((op, val))
        macros.append(tokens)
        
    memo = {}

    def get_transform(macro_id, depth):
        if depth == 0:
            return (1, 0) # No transform
            
        state = (macro_id, depth)
        if state in memo:
            return memo[state]
            
        curr_m = 1
        curr_c = 0
        
        # macro_id is 1-based in input logic assumption?
        if 1 <= macro_id <= len(macros):
            tokens = macros[macro_id - 1]
            for op, val in tokens:
                if op == "ADD":
                    curr_c = (curr_c + val) % MOD
                elif op == "MUL":
                    curr_m = (curr_m * val) % MOD
                    curr_c = (curr_c * val) % MOD
                elif op == "CALL":
                    m_sub, c_sub = get_transform(val, depth - 1)
                    # Apply sub transform: x' = m_sub * x + c_sub
                    # Current: x_curr = curr_m * x + curr_c
                    # New: x_new = m_sub * (curr_m * x + curr_c) + c_sub
                    #            = (m_sub * curr_m) * x + (m_sub * curr_c + c_sub)
                    curr_m = (curr_m * m_sub) % MOD
                    curr_c = (curr_c * m_sub + c_sub) % MOD
                    
        memo[state] = (curr_m, curr_c)
        return (curr_m, curr_c)

    m_res, c_res = get_transform(1, d_limit)
    # Result is a0 transformed
    print((m_res * a0 + c_res) % MOD)


if __name__ == "__main__":
    solve()
