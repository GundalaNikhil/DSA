import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    bonuses = []
    for _ in range(m):
        bonuses.append(int(input_data[ptr]))
        ptr += 1
        
    bonuses.sort(reverse=True)
    ans = 0
    curr_sum = 0
    
    # Logic: Pick k items. Which k? Top k?
    # Problem "Hidden State Reveal": sounds like we reveal top K bonuses?
    # Formula: `(n - k) * curr_sum`.
    # `curr_sum` is sum of first k bonuses.
    # We iterate k from 1 to min(n, m).
    
    for k in range(1, min(n, m) + 1):
        curr_sum += bonuses[k - 1]
        ans = max(ans, (n - k) * curr_sum)
        
    print(ans)


if __name__ == "__main__":
    solve()
