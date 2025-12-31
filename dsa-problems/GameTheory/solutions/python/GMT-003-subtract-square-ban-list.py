from typing import List

def subtract_square_game(n: int, banned: List[int]) -> str:
    banned_set = set(banned)
    dp = [False] * (n + 1)
    
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            s = j * j
            if s not in banned_set:
                if not dp[i - s]:
                    dp[i] = True
                    break
            j += 1
            
    return "First" if dp[n] else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        banned = []
        for _ in range(k):
            banned.append(int(next(iterator)))
            
        print(subtract_square_game(n, banned))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
