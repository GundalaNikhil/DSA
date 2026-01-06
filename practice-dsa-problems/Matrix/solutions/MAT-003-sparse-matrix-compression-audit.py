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
    k = int(input_data[ptr])
    ptr += 1
    A = []
    non_zeros_a = set()
    for r in range(n):
        row = []
        for c in range(m):
            val = int(input_data[ptr])
            ptr += 1
            row.append(val)
            if val != 0:
                non_zeros_a.add((r + 1, c + 1, val))
        A.append(row)
        
    for i in range(1, k + 1):
        s_count = int(input_data[ptr])
        ptr += 1
        sparse_entries = set()
        for _ in range(s_count):
            r = int(input_data[ptr])
            ptr += 1
            c = int(input_data[ptr])
            ptr += 1
            v = int(input_data[ptr])
            ptr += 1
            sparse_entries.add((r, c, v))
            
        decomp = []
        for r in range(n):
            row = []
            for c in range(m):
                row.append(int(input_data[ptr]))
                ptr += 1
            decomp.append(row)
            
        if sparse_entries != non_zeros_a:
            print(f"COMPRESS {i}")
            return
            
        for r in range(n):
            if decomp[r] != A[r]:
                print(f"DECOMPRESS {i}")
                return
                
    print("OK")


if __name__ == "__main__":
    solve()
