def z_function(s: str) -> list[int]:
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
            
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
            
    return z

def main():
    import sys
sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    z = z_function(s)
    print(*(z))

if __name__ == "__main__":
    main()