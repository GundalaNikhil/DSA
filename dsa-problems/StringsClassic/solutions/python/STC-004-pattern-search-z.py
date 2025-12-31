def find_occurrences(p: str, t: str) -> list[int]:
    s = p + "#" + t
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    
    # Compute Z-array
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
            
    # Collect matches
    matches = []
    p_len = len(p)
    for i in range(p_len + 1, n):
        if z[i] == p_len:
            matches.append(i - (p_len + 1))
            
    return matches

def main():
    import sys
    sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    t = input_data[0]
    p = input_data[1]
    result = find_occurrences(p, t)
    if not result:
        print("-1")
    else:
        print(*(result))

if __name__ == "__main__":
    main()