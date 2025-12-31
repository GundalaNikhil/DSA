def compute_prefix_function(p: str) -> list[int]:
    m = len(p)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
        pi[i] = j
    return pi

def find_occurrences(p: str, t: str) -> list[int]:
    if not p:
        return []
        
    pi = compute_prefix_function(p)
    m = len(p)
    n = len(t)
    matches = []
    j = 0
    
    for i in range(n):
        while j > 0 and t[i] != p[j]:
            j = pi[j - 1]
        if t[i] == p[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = pi[j - 1]
            
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