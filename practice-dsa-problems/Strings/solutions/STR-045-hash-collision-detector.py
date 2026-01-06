import sys


def compute_hash(s, base, mod):
    h = 0
    p = 1
    for char in s:
        val = ord(char)
        h = (h + val * p) % mod
        p = (p * base) % mod
        
    return h


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    config = input_data[0].split()
    if not config:
        return
    base = int(config[0])
    mod = int(config[1])
    n = int(input_data[1])
    seen_hashes = {}
    collision_found = False
    for i in range(2, 2 + n):
        s = input_data[i].strip()
        h = compute_hash(s, base, mod)
        if h in seen_hashes:
            other_s = seen_hashes[h]
            if other_s != s:
                pair = sorted([s, other_s])
                print(f"COLLISION: {pair[0]} & {pair[1]}")
                collision_found = True
                break
        else:
            seen_hashes[h] = s
            
    if not collision_found:
        print("CLEAR")


if __name__ == "__main__":
    solve()
