from typing import List, Tuple

def chomp_game(R: int, C: int, poisons: List[List[int]]) -> str:
    memo = {}
    
    def is_valid(r, c):
        for pr, pc in poisons:
            if pr >= r and pc >= c:
                return False
        return True

    def can_win(state: Tuple[int]) -> bool:
        if state in memo:
            return memo[state]
        
        # Try all moves
        for c in range(C):
            for r in range(state[c]):
                if is_valid(r, c):
                    # Construct next state
                    next_state_list = list(state)
                    for i in range(c, C):
                        next_state_list[i] = min(next_state_list[i], r)
                    next_state = tuple(next_state_list)
                    
                    if not can_win(next_state):
                        memo[state] = True
                        return True
        
        memo[state] = False
        return False

    initial_state = tuple([R] * C)
    return "First" if can_win(initial_state) else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        R = int(next(iterator))
        C = int(next(iterator))
        K = int(next(iterator))
        poisons = []
        for _ in range(K):
            r = int(next(iterator))
            c = int(next(iterator))
            poisons.append([r, c])
            
        print(chomp_game(R, C, poisons))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
