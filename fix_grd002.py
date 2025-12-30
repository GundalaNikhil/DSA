import heapq
import yaml

def solve_grd002(k, m, quantities):
    pq = []
    total_kits = 0
    for q in quantities:
        if q > 0:
            heapq.heappush(pq, -q)
            total_kits += q
    
    fulfilled = min(m, total_kits)
    to_distribute = fulfilled
    
    while to_distribute > 0 and pq:
        max_q = -heapq.heappop(pq)
        max_q -= 1
        to_distribute -= 1
        if max_q > 0:
            heapq.heappush(pq, -max_q)
            
    remaining_types = len(pq)
    zeroed_types = k - remaining_types
    return f"{fulfilled} {zeroed_types}"

def generate_tests():
    tests = {
        'problem_id': 'GRD_LAB_KIT_DISTRIBUTION__5291',
        'samples': [
            {'input': "3 4\n3 1 2", 'output': solve_grd002(3, 4, [3, 1, 2])},
        ],
        'public': [
            {'input': "5 10\n2 2 2 2 2", 'output': solve_grd002(5, 10, [2, 2, 2, 2, 2])},
            {'input': "3 10\n1 1 1", 'output': solve_grd002(3, 10, [1, 1, 1])},
        ],
        'hidden': []
    }
    
    # Add some hidden cases
    import random
    for _ in range(10):
        k = random.randint(10, 100)
        m = random.randint(10, 1000)
        q = [random.randint(0, 100) for _ in range(k)]
        input_str = f"{k} {m}\n" + " ".join(map(str, q))
        tests['hidden'].append({'input': input_str, 'output': solve_grd002(k, m, q)})
        
    with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Greedy/testcases/GRD-002-lab-kit-distribution.yaml', 'w') as f:
        yaml.dump(tests, f, default_flow_style=False)

if __name__ == "__main__":
    generate_tests()
