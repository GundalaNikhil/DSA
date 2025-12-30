import sys

def min_battery_swaps(n: int, T: int, capacities: list) -> int:
    if sum(capacities) < T:
        return -1
        
    # Sort descending
    capacities.sort(reverse=True)
    
    current_sum = 0
    count = 0
    
    for c in capacities:
        current_sum += c
        count += 1
        if current_sum >= T:
            return count - 1
            
    return -1

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    T = int(next(iterator))
    
    capacities = []
    for _ in range(n):
        capacities.append(int(next(iterator)))

    result = min_battery_swaps(n, T, capacities)
    print(result)

if __name__ == "__main__":
    main()
