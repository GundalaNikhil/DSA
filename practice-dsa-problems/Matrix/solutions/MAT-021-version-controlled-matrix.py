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
    initial = [0] * (n * m)
    for i in range(n * m):
        initial[i] = int(input_data[ptr])
        ptr += 1
        
    versions = [initial]
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == 'SET':
            v_id = int(input_data[ptr])
            ptr += 1
            r = int(input_data[ptr]) - 1
            ptr += 1
            c = int(input_data[ptr]) - 1
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            new_v = list(versions[v_id])
            new_v[r * m + c] = x
            versions.append(new_v)
        elif op == 'MERGE':
            v1_id = int(input_data[ptr])
            ptr += 1
            v2_id = int(input_data[ptr])
            ptr += 1
            base_id = int(input_data[ptr])
            ptr += 1
            v1 = versions[v1_id]
            v2 = versions[v2_id]
            base = versions[base_id]
            new_v = [0] * (n * m)
            conflicts = 0
            for i in range(n * m):
                val1 = v1[i]
                val2 = v2[i]
                val_b = base[i]
                if val1 == val_b and val2 == val_b:
                    new_v[i] = val_b
                elif val1 != val_b and val2 == val_b:
                    new_v[i] = val1
                elif val1 == val_b and val2 != val_b:
                    new_v[i] = val2
                elif val1 != val_b and val2 != val_b:
                    if val1 == val2:
                        new_v[i] = val1
                    else:
                        conflicts += 1
                        new_v[i] = min(val1, val2)
                else: # Should be covered.
                    pass
            versions.append(new_v)
            print(conflicts)
        elif op == 'GET':
            v_id = int(input_data[ptr])
            ptr += 1
            r = int(input_data[ptr]) - 1
            ptr += 1
            c = int(input_data[ptr]) - 1
            ptr += 1
            print(versions[v_id][r * m + c])
if __name__ == '__main__':
    solve()