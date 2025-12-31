import sys

def highest_occupied_row(r: int, capacities: list, refunds: list) -> int:
    total_capacity = sum(capacities)
    total_people = total_capacity - len(refunds)
    
    if total_people <= 0:
        return 0
        
    for i in range(r):
        total_people -= capacities[i]
        if total_people <= 0:
            return i + 1
            
    return r

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    r = int(next(iterator))
    n = int(next(iterator))
    
    capacities = []
    for _ in range(r):
        capacities.append(int(next(iterator)))
        
    # Skip refunds details as we only need count
    # But we must consume the input
    for _ in range(n):
        next(iterator) # row
        next(iterator) # seat
        
    # Note: refunds list in function signature is just for compatibility with template
    # We can pass a dummy list or just use n
    print(highest_occupied_row(r, capacities, [0]*n))

if __name__ == "__main__":
    main()
