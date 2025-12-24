import random
import yaml
import heapq

def solve(n, arrivals, departures):
    if n == 0:
        return 0
    
    intervals = sorted(zip(arrivals, departures))
    heap = []
    max_seats = 0
    
    for arr, dep in intervals:
        while heap and heap[0] <= arr:
            heapq.heappop(heap)
        heapq.heappush(heap, dep)
        max_seats = max(max_seats, len(heap))
    
    return max_seats

def make_test_case(arrivals, departures):
    n = len(arrivals)
    res = solve(n, arrivals, departures)
    input_str = f"{n}\n" + " ".join(map(str, arrivals)) + "\n" + " ".join(map(str, departures))
    output_str = str(res)
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([0, 4, 4], [5, 5, 9])
        ],
        "public": [
            make_test_case([1, 2, 3], [2, 3, 4]),
            make_test_case([1, 1, 1], [2, 2, 2]),
            make_test_case([0, 5, 10], [5, 10, 15])
        ],
        "hidden": []
    }

    # Edge cases: n=1, All overlap, None overlap
    tc["hidden"].append(make_test_case([0], [10**9]))
    tc["hidden"].append(make_test_case([1] * 10, [10] * 10))
    tc["hidden"].append(make_test_case([i*10 for i in range(10)], [i*10+5 for i in range(10)]))
    
    # Large sequence
    n_large = 100000
    arrivals_large = [random.randint(0, 10**9) for _ in range(n_large)]
    departures_large = [a + random.randint(1, 10**6) for a in arrivals_large]
    tc["hidden"].append(make_test_case(arrivals_large, departures_large))

    # Stress case
    tc["hidden"].append(make_test_case([random.randint(0, 10**9) for _ in range(100000)], 
                                     [random.randint(0, 10**9) for _ in range(100000)]))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
