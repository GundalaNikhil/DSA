import sys

def min_total_delay(n: int, trips: list) -> int:
    # Sort by s + d
    trips.sort(key=lambda x: x[0] + x[1])
    
    current_time = 0
    total_delay = 0
    
    for s, d in trips:
        delay = max(0, current_time - s)
        total_delay += delay
        current_time += d
        
    return total_delay

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    trips = []
    for _ in range(n):
        s = int(next(iterator))
        d = int(next(iterator))
        trips.append([s, d])

    result = min_total_delay(n, trips)
    print(result)

if __name__ == "__main__":
    main()
