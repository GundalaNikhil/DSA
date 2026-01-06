from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    
    if k >= n - 1:
       
        print(max(a))
        return
        
    dq = deque(a)
    winner = dq.popleft()
    curr_wins = 0

    
    while curr_wins < k:
        challenger = dq.popleft()
        if winner > challenger:
            curr_wins += 1
            dq.append(challenger)
        else:
            curr_wins = 1
            dq.append(winner)
            winner = challenger
            
    print(winner)

if __name__ == "__main__":
    solve()
