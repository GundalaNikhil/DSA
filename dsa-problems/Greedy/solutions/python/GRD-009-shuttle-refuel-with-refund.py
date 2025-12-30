import sys

def find_start(n: int, gain: list, cost: list) -> int:
    total_gain = sum(gain)
    total_cost = sum(cost)
    max_cost = max(cost)
    
    # If even with refund we can't make it, return -1
    if total_gain < total_cost - max_cost:
        return -1
        
    # Find index of max cost to skip
    # If multiple, any will do, usually first one is fine
    max_cost_idx = cost.index(max_cost)
    
    current_tank = 0
    start = 0
    
    for i in range(n):
        current_cost = 0 if i == max_cost_idx else cost[i]
        current_tank += gain[i] - current_cost
        
        if current_tank < 0:
            start = i + 1
            current_tank = 0
            
    return start

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
