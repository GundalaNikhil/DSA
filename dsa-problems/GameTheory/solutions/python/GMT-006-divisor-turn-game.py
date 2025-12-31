import sys

# Increase recursion depth just in case, though depth is log(N)
sys.setrecursionlimit(20000)

def divisor_game(n: int) -> str:
    memo = {}

    def can_win(curr):
        if curr in memo:
            return memo[curr]
        
        # Try to find a move to a losing state
        i = 2
        while i * i <= curr:
            if curr % i == 0:
                d1 = i
                if not can_win(d1):
                    memo[curr] = True
                    return True
                d2 = curr // i
                if d2 < curr:
                    if not can_win(d2):
                        memo[curr] = True
                        return True
            i += 1
        
        # If no moves lead to losing state (or no moves at all - prime), we lose
        memo[curr] = False
        return False

    return "First" if can_win(n) else "Second"

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    print(divisor_game(n))

if __name__ == "__main__":
    main()
