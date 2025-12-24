
import sys
import random
import heapq

# --- Reference Solution ---

def solve(n, intervals):
    # intervals: list of [start, end, payload]
    if not intervals:
        return []
        
    # Sort by start time
    # If start times equal, sorting by end time or payload doesn't strictly matter for correctness of merging component,
    # but for stability usually by start.
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    if not intervals:
        return merged
        
    current_start, current_end, current_payload = intervals[0]
    
    for i in range(1, n):
        next_start, next_end, next_payload = intervals[i]
        
        if next_start <= current_end:
            # Overlap or touching
            current_end = max(current_end, next_end)
            current_payload = max(current_payload, next_payload)
        else:
            # Disjoint
            merged.append([current_start, current_end, current_payload])
            current_start, current_end, current_payload = next_start, next_end, next_payload
            
    merged.append([current_start, current_end, current_payload])
    
    return merged

# --- Test Case Generators ---

def make_test_case(n, intervals):
    lines = [str(n)]
    for iv in intervals:
        lines.append(f"{iv[0]} {iv[1]} {iv[2]}")
    input_str = "\n".join(lines)
    
    res = solve(n, intervals)
    
    out_lines = [str(len(res))]
    for iv in res:
        out_lines.append(f"{iv[0]} {iv[1]} {iv[2]}")
    output_str = "\n".join(out_lines)
    
    return input_str, output_str

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    for line in c["output"].split("\n"):
        print(f"      {line}")

def main():
    test_cases = {
        "problem_id": "HEP_MERGE_INTERVALS_MAX_PAYLOAD__6043",
        "samples": [],
        "public": [],
        "hidden": []
    }
    
    # Samples
    # 1. Example
    s1_n = 2
    s1_intervals = [[1, 3, 5], [2, 4, 7]]
    si1, so1 = make_test_case(s1_n, s1_intervals)
    test_cases["samples"].append({"input": si1, "output": so1})
    
    # Public
    # 1. Disjoint
    p1_n = 3
    p1_intervals = [[1, 2, 10], [4, 5, 20], [7, 8, 30]]
    # Output should be same
    pi1, po1 = make_test_case(p1_n, p1_intervals)
    test_cases["public"].append({"input": pi1, "output": po1})
    
    # 2. Fully Nested / Covered
    p2_n = 3
    p2_intervals = [[1, 10, 5], [2, 8, 100], [3, 5, 50]]
    # Max range 1-10. Max payload 100.
    pi2, po2 = make_test_case(p2_n, p2_intervals)
    test_cases["public"].append({"input": pi2, "output": po2})
    
    # 3. Touching
    p3_n = 3
    p3_intervals = [[1, 2, 10], [2, 3, 20], [3, 4, 30]]
    # Merge all: 1-4, max 30.
    pi3, po3 = make_test_case(p3_n, p3_intervals)
    test_cases["public"].append({"input": pi3, "output": po3})
    
    # Hidden
    hidden = []
    
    # 1. Edge: Single Interval
    h1_n = 1
    h1_intervals = [[0, 0, 0]]
    hidden.append(make_test_case(h1_n, h1_intervals))
    
    # 2. Edge: Identical Intervals
    h2_n = 5
    h2_intervals = [[1, 5, 10]] * 5
    hidden.append(make_test_case(h2_n, h2_intervals))
    
    # 3. Negative Coordinates
    h3_n = 3
    h3_intervals = [[-10, -5, 1], [-6, -2, 5], [-1, 2, 3]]
    # [-10, -5] and [-6, -2] merge -> [-10, -2], payload 5.
    # [-1, 2] is disjoint.
    hidden.append(make_test_case(h3_n, h3_intervals))
    
    # 4. Long Chain
    h4_n = 100
    h4_intervals = []
    for i in range(h4_n):
        h4_intervals.append([i, i+1, i]) # 0-1, 1-2, 2-3... -> Merge all 0-100, max payload 99
    hidden.append(make_test_case(h4_n, h4_intervals))
    
    # 5. Reverse Input Order (Validation of sorting)
    h5_n = 4
    h5_intervals = [[4, 5, 1], [3, 4, 2], [2, 3, 3], [1, 2, 4]]
    # Should merge 1-5, max payload 4.
    hidden.append(make_test_case(h5_n, h5_intervals))
    
    # 6. Stress: Random small components
    h6_n = 500
    h6_intervals = []
    for _ in range(h6_n):
        start = random.randint(1, 1000)
        end = start + random.randint(0, 10)
        payload = random.randint(1, 1000)
        h6_intervals.append([start, end, payload])
    hidden.append(make_test_case(h6_n, h6_intervals))
    
    # 7. Stress: One huge component
    h7_n = 1000
    h7_intervals = []
    for i in range(h7_n):
        # All overlap range [0, 2000]
        start = random.randint(0, 500)
        end = random.randint(1500, 2000)
        payload = random.randint(1, 10**9)
        h7_intervals.append([start, end, payload])
    hidden.append(make_test_case(h7_n, h7_intervals))
    
    # 8. Large Coordinates
    h8_intervals = [
        [-10**9, -10**9 + 100, 5],
        [10**9 - 100, 10**9, 10]
    ]
    h8_n = len(h8_intervals)
    hidden.append(make_test_case(h8_n, h8_intervals))
    
    # 9. Random large
    h9_n = 2000
    h9_intervals = []
    for _ in range(h9_n):
        start = random.randint(-10000, 10000)
        length = random.randint(0, 1000)
        h9_intervals.append([start, start+length, random.randint(1, 100)])
    hidden.append(make_test_case(h9_n, h9_intervals))
    
    # 10. Max Constraints (10^5) - reduced to 5000 for yaml size but validates logic
    h10_n = 5000
    h10_intervals = []
    for i in range(h10_n):
        start = i * 2
        end = start + 1
        h10_intervals.append([start, end, i])
    # No merges
    hidden.append(make_test_case(h10_n, h10_intervals))

    for inp, out in hidden:
        test_cases["hidden"].append({"input": inp, "output": out})

    # Print YAML
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

if __name__ == "__main__":
    main()
