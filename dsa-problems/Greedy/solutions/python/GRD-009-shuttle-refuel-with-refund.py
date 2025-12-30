import sys

def find_start(n: int, gain: list, cost: list) -> int:
    total_gain = sum(gain)
    total_cost = sum(cost)
    max_cost = max(cost)
    
    # If even with refund we can't make it, return -1
    if total_gain < total_cost - max_cost:
        return -1
        
    def check_start(start_idx):
        fuel = 0
        max_c = 0
        used = False
        for i in range(n):
            idx = (start_idx + i) % n
            fuel += gain[idx]
            max_c = max(max_c, cost[idx])
            fuel -= cost[idx]
            if fuel < 0:
                if not used:
                    fuel += max_c
                    used = True
                    if fuel < 0: return False
                else:
                    return False
        return True

    # Total gain + max cost must be >= total cost
    if total_gain + max_cost < total_cost:
        return -1
        
    # Check classic gas station start first
    diff = [gain[i] - cost[i] for i in range(n)]
    curr = 0
    min_sum = 0
    start_cand = 0
    for i in range(n):
        curr += diff[i]
        if curr < min_sum:
            min_sum = curr
            start_cand = (i + 1) % n
            
    if check_start(start_cand):
        return start_cand
        
    # If not, try all (n=10^5 might be slow but let's see)
    # Actually, we can optimize: the only candidates are those after a failed point.
    # But for medium complexity, trying all is risky.
    # However, N is 10^5.
    for i in range(n):
        if check_start(i):
            return i
            
    return -1

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    
    gain = []
    for _ in range(n):
        gain.append(int(next(iterator)))
        
    cost = []
    for _ in range(n):
        cost.append(int(next(iterator)))

    result = find_start(n, gain, cost)
    print(result)

if __name__ == "__main__":
    main()
