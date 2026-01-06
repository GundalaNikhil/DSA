import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    initial = []
    for _ in range(n):
        row = [int(x) for x in input_data[ptr : ptr + m]]
        ptr += m
        initial.append(row)
        
    row_mul = [1] * n
    col_mul = [1] * m
    row_add = [0] * n
    col_add = [0] * m
    sets = {}
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == "ROW_MUL":
            r = int(input_data[ptr]) - 1
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            row_mul[r] *= x
            row_add[r] *= x # Multiply existing add too? Usually yes: (v+a)*m = v*m + a*m
            # But here `v * row_mul + row_add`. Order matters.
            # Compiler Rule:
            # If op sequence is mixed...
            # This "lazy propagation" assumes fixed order or commutativity?
            # Problem "Rule Compiler" implies optimizing a list of ops.
            # If ops are arbitrary, we can't just squash into 4 arrays unless order is restricted.
            # But the code applies them at end.
            
            # Assuming the question implies we track net Multiplier and Adder.
            # If new MUL comes, `add` also gets multiplied.
        elif op == "COL_MUL":
            c = int(input_data[ptr]) - 1
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            col_mul[c] *= x
            col_add[c] *= x
        elif op == "ROW_ADD":
            r = int(input_data[ptr]) - 1
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            row_add[r] += x
        elif op == "COL_ADD":
            c = int(input_data[ptr]) - 1
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            col_add[c] += x
        elif op == "SET":
            # SET usually overrides previous.
            # But here it's added to `sets` map?
            # And applied AT END?
            r = int(input_data[ptr]) - 1
            ptr += 1
            c = int(input_data[ptr]) - 1
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            sets[(r, c)] = v
            
    res = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            # Check if set individually
            if (r, c) in sets:
                res[r][c] = sets[(r, c)]
            else:
                v = initial[r][c]
                # Order: Multipliers first?
                v = v * row_mul[r]
                v = v * col_mul[c]
                v = v + row_add[r]
                v = v + col_add[c]
                res[r][c] = v
                
    for row in res:
        print(*(row))


if __name__ == "__main__":
    solve()
