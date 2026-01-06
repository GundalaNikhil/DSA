import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k_hashes = int(input_data[ptr])
    ptr += 1
    M_size = int(input_data[ptr])
    ptr += 1
    vals = []
    for _ in range(n):
        vals.append(int(input_data[ptr]))
        ptr += 1
        
    val_set = set(vals)
    bitset_str = input_data[ptr]
    ptr += 1
    bitset = [int(c) for c in bitset_str]
    
    hash_params = []
    for _ in range(k_hashes):
        a = int(input_data[ptr])
        ptr += 1
        b = int(input_data[ptr])
        ptr += 1
        hash_params.append((a, b))
        
    q_count = int(input_data[ptr])
    ptr += 1
    
    false_positives = 0
    for _ in range(q_count):
        x = int(input_data[ptr])
        ptr += 1
        
        maybe_present = True
        for a, b in hash_params:
            h = (a * x + b) % M_size
            if bitset[h] == 0:
                maybe_present = False
                break
                
        is_present = x in val_set
        
        if maybe_present:
            if not is_present:
                false_positives += 1
                print("true")
            else:
                print("true")
        else:
            print("false")
            
    print(false_positives)


if __name__ == "__main__":
    solve()
