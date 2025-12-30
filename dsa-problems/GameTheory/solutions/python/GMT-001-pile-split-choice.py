def pile_split_game(n: int) -> str:
    if n == 0:
        return "Second"
    
    g = [0] * (n + 1)
    
    for i in range(3, n + 1):
        reachable = set()
        # Split into j and i-j.
        # j goes from 1 up to (i-1)//2
        for j in range(1, (i - 1) // 2 + 1):
            reachable.add(g[j] ^ g[i - j])
        
        mex = 0
        while mex in reachable:
            mex += 1
        g[i] = mex
        
    return "First" if g[n] > 0 else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    print(pile_split_game(n))

if __name__ == "__main__":
    main()
