
import sys
import random
import heapq

# --- Reference Solution ---
def solve(n, E, tasks):
    # Tasks: list of [d, g]
    s1 = []
    s2 = []
    
    for d, g in tasks:
        if g >= d:
            s1.append((d, g))
        else:
            s2.append((d, g))
            
    # Process S1: Sort by d ASC
    s1.sort(key=lambda x: x[0])
    
    count = 0
    current_E = E
    
    for d, g in s1:
        if current_E >= d:
            current_E = current_E - d + g
            count += 1
        else:
            # Cannot process this task, and since sorted by d, cannot process any subsequent S1 task 
            # (assuming they require even more d, and we rely on tasks to boost E)
            # Actually, could there be a task with same d but we just don't have enough?
            # Yes. We stop.
            # Wait, strictly speaking, if we skip this (d, g), we don't gain g-d.
            # Next task has d' >= d. Since current_E < d <= d', we fail next too.
            break
            
    # Process S2: Sort by g DESC
    s2.sort(key=lambda x: x[1], reverse=True)
    
    # Max-Heap for Costs (d - g). We store negative for min-heap simulating max-heap
    pq = [] 
    
    for d, g in s2:
        cost = d - g
        if current_E >= d:
            # Can execute
            current_E -= cost
            heapq.heappush(pq, -cost)
            count += 1
        else:
            # Regret logic
            if pq:
                max_cost = -pq[0]
                if max_cost > cost:
                    # Check if swapping is valid
                    # We refund max_cost.
                    temp_E = current_E + max_cost
                    if temp_E >= d:
                        # Swap
                        heapq.heappop(pq)
                        heapq.heappush(pq, -cost)
                        current_E = temp_E - cost
                        # Count doesn't change (one out, one in)
                        
    return count

# --- Test Case Generators ---

def generate_sample_1():
    n, E = 2, 3
    tasks = [[2, 3], [3, 1]]
    return n, E, tasks

def generate_random(n, max_e, max_val):
    E = random.randint(0, max_e)
    tasks = []
    for _ in range(n):
        d = random.randint(1, max_val)
        g = random.randint(1, max_val)
        tasks.append([d, g])
    return n, E, tasks

# --- YAML Builder ---

def format_input(n, E, tasks):
    lines = [f"{n} {E}"]
    for t in tasks:
        lines.append(f"{t[0]} {t[1]}")
    return "\n".join(lines)

def format_output(val):
    return str(val)

def make_test_case(n, E, tasks):
    input_str = format_input(n, E, tasks)
    output_val = solve(n, E, tasks)
    output_str = format_output(output_val)
    return input_str, output_str


def main():
    test_cases = {
        "problem_id": "HEP_TASK_SCHEDULER_ENERGY__9471",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    sn, se, st = generate_sample_1()
    si, so = make_test_case(sn, se, st)
    test_cases["samples"].append({"input": si, "output": so})
    
    # Sample 2: Regret case
    # E=10. T1(10, 5) cost 5. T2(6, 4) cost 2.
    # S2 logic: T1 g=5, T2 g=4. Sorted.
    # Do T1: E -> 5. 
    # Try T2: Need 6. Have 5. Fail.
    # Swap? max_cost=5. E' = 5+5=10. 10>=6. Swap. E = 10-2=8.
    # Count 1 (T2).
    # Wait, if we do T2 first: E=10-2=8. Try T1: Need 10. Fail.
    # Max tasks is 1. Swapping gives 1. Just doing T1 gives 1.
    # We need a case where count improves or maintains lower cost?
    # Actually count is same. Energy remaining is higher with swap (8 vs 5).
    # Higher energy might allow T3.
    # Let's add T3(8, 0). Cost 8.
    # With T1: E=5. T3 needs 8. Fail. Total 1.
    # With T2: E=8. T3 needs 8. Do it. E=0. Total 2.
    # So swap was crucial.
    s2tasks = [[10, 5], [6, 4], [8, 0]]
    s2i, s2o = make_test_case(3, 10, s2tasks)
    test_cases["samples"].append({"input": s2i, "output": s2o})

    # Public
    # Edge: E=0
    p1n, p1e = 1, 0
    p1t = [[5, 10]] # Can't start
    pi1, po1 = make_test_case(p1n, p1e, p1t)
    test_cases["public"].append({"input": pi1, "output": po1}) # 0
    
    # Edge: S1 only, huge gains
    p2n, p2e = 3, 1
    p2t = [[1, 100], [50, 60], [10, 20]] # Sorted d: (1,100), (10,20), (50,60). E grows 1->100->110->120. All 3.
    pi2, po2 = make_test_case(p2n, p2e, p2t)
    test_cases["public"].append({"input": pi2, "output": po2})

    # Basic: S2 chain
    p3n, p3e = 2, 10
    p3t = [[5, 4], [4, 3]] # Cost 1 each.
    pi3, po3 = make_test_case(p3n, p3e, p3t)
    test_cases["public"].append({"input": pi3, "output": po3}) # 2

    # Hidden
    hidden_cases = []
    
    # 1. Edge: All G < D, E large
    h1n, h1e = 10, 1000
    _, _, h1t = generate_random(h1n, 100, 50) # random, all likely feasible
    hidden_cases.append(make_test_case(h1n, h1e, h1t))
    
    # 2. Edge: All G > D, but E small
    h2t = [[100, 200], [5, 10], [50, 60]] # Need 5 first.
    hidden_cases.append(make_test_case(3, 5, h2t))
    
    # 3. Stress: N=1000 optimized S2
    # Many small cost items vs one huge cost item
    h3t = []
    for i in range(500):
        h3t.append([10, 9]) # Cost 1, Need 10.
    h3t.append([1000, 500]) # Cost 500. Need 1000.
    # If E=1000. 
    # S2 sort by g DESC: [1000, 500] (g=500), then [10, 9]...
    # Do big one: E -> 500.
    # Do small ones: Need 10. E=500. Can do many.
    # If we had strictly limited E?
    h3e = 600
    # Big one: E->100.
    # Small ones: 100/1 = 100 tasks. Total 101.
    # If we skipped big one? E=600. Small ones: 500 tasks. Total 500.
    # Swap logic should kick in.
    hidden_cases.append(make_test_case(501, h3e, h3t))

    # 4. Stress: N=1000, Random
    h4n, h4e = 1000, 10000
    _, _, h4t = generate_random(h4n, 10000, 5000)
    hidden_cases.append(make_test_case(h4n, h4e, h4t))
    
    # 5. Negative: E always increasing
    h5t = [[i, i+1] for i in range(1, 20)]
    hidden_cases.append(make_test_case(19, 1, h5t))
    
    # 6. Negative: E drops to 0 exactly then fails
    h6t = [[10, 0], [10, 0]]
    hidden_cases.append(make_test_case(2, 10, h6t)) # Do 1, E=0. Fail 2nd.

    # 7. Stress: Max values
    h7t = [[1000000000, 999999999]] # Cost 1
    hidden_cases.append(make_test_case(1, 1000000000, h7t))
    
    # 8. Special: Mix of S1 and S2
    h8t = [[5, 10], [20, 10], [2, 4], [15, 5]]
    hidden_cases.append(make_test_case(4, 5, h8t))
    
    # 9. Normal random
    h9n, h9e = 50, 100
    _, _, h9t = generate_random(h9n, 100, 50)
    hidden_cases.append(make_test_case(h9n, h9e, h9t))
    
    # 10. Edge: E=0 but S1 task [0, 5] (d=0 allowed?)
    # Problem d_i >= 1.
    # Constraints: 1 <= d_i. So n/a.
    pass

    # Add to structure
    for inp, out in hidden_cases:
        test_cases["hidden"].append({"input": inp, "output": out})

    # Output YAML
    print(f"problem_id: {test_cases['problem_id']}")
    print("samples:")
    for c in test_cases["samples"]:
        print_case(c)
    print("\npublic:")
    for c in test_cases["public"]:
        print_case(c)
    print("\nhidden:")
    for c in test_cases["hidden"]:
        print_case(c)

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    print(f"      {c['output']}")

if __name__ == "__main__":
    main()
