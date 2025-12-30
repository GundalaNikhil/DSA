from typing import List, Tuple

def circular_nim(n: int, piles: List[int]) -> str:
    memo = {}
    visiting = set()

    def solve(current_piles: Tuple[int], depth: int) -> str:
        if depth > 50:
            return "Draw"
        if current_piles in memo:
            return memo[current_piles]
        if current_piles in visiting:
            return "Draw"
        
        visiting.add(current_piles)
        
        can_reach_loss = False
        can_reach_draw = False
        has_moves = False
        
        for i in range(n):
            if current_piles[i] > 0:
                for k in range(1, current_piles[i] + 1):
                    has_moves = True
                    next_piles = list(current_piles)
                    next_piles[i] -= k
                    next_piles[(i - 1 + n) % n] += 1
                    next_piles[(i + 1) % n] += 1
                    
                    res = solve(tuple(next_piles), depth + 1)
                    
                    if res == "Second":
                        can_reach_loss = True
                        break
                    if res == "Draw":
                        can_reach_draw = True
                if can_reach_loss:
                    break
        
        visiting.remove(current_piles)
        
        if can_reach_loss:
            result = "First"
        elif not has_moves:
            result = "Second"
        elif can_reach_draw:
            result = "Draw"
        else:
            result = "Second"
            
        memo[current_piles] = result
        return result

    return solve(tuple(piles), 0)

def main():
    import sys
    # Increase recursion depth
    sys.setrecursionlimit(20000)
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        piles = []
        for _ in range(n):
            piles.append(int(next(iterator)))
            
        print(circular_nim(n, piles))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
