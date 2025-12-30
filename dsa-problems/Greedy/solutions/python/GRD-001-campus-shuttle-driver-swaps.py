import sys

def min_driver_swaps(trips, driver_a, driver_b) -> int:
    n = len(trips)
    INF = float('inf')
    
    # cost_a: min switches ending with A
    # cost_b: min switches ending with B
    cost_a = INF
    cost_b = INF
    
    # Helper to check coverage
    def can_cover(trip, driver):
        return driver[0] <= trip[0] and trip[1] <= driver[1]
    
    # Base case: Trip 0
    if can_cover(trips[0], driver_a):
        cost_a = 0
    if can_cover(trips[0], driver_b):
        cost_b = 0
        
    for i in range(1, n):
        next_cost_a = INF
        next_cost_b = INF
        
        # Try assigning current trip to A
        if can_cover(trips[i], driver_a):
            next_cost_a = min(cost_a, cost_b + 1)
            
        # Try assigning current trip to B
        if can_cover(trips[i], driver_b):
            next_cost_b = min(cost_b, cost_a + 1)
            
        cost_a = next_cost_a
        cost_b = next_cost_b
        
    result = min(cost_a, cost_b)
    return result if result != INF else -1

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    
    trips = []
    for _ in range(n):
        start = int(next(iterator))
        end = int(next(iterator))
        trips.append((start, end))
        
    a_start = int(next(iterator))
    a_end = int(next(iterator))
    driver_a = (a_start, a_end)
    
    b_start = int(next(iterator))
    b_end = int(next(iterator))
    driver_b = (b_start, b_end)
    
    print(min_driver_swaps(trips, driver_a, driver_b))

if __name__ == "__main__":
    main()
