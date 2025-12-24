
import sys
import random
import heapq

# --- Reference Solution ---

def solve(n, m, max_heap_arr, min_heap_arr):
    combined = sorted(max_heap_arr + min_heap_arr)
    sz = len(combined)
    
    if sz == 0:
        return 0
        
    if sz % 2 == 1:
        return combined[sz // 2]
    else:
        mid1 = combined[sz // 2 - 1]
        mid2 = combined[sz // 2]
        res = (mid1 + mid2) / 2
        if res.is_integer():
            return int(res)
        return res

# --- Test Case Generators ---

def make_test_case(n, m, max_h, min_h):
    # Input format:
    # n m
    # max_heap elements
    # min_heap elements
    input_lines = [f"{n} {m}"]
    
    if n > 0:
        input_lines.append(" ".join(map(str, max_h)))
    else:
        input_lines.append("") # Empty line? or handle reading?
        # Template: "max_heap = list(...) if n > 0 else []"
        # Reading logic usually expects a line if n > 0.
        # If n=0, usually the line is empty or just skipped?
        # Standard input reading: "Second line: n integers".
        # If n=0, usually an empty line.
        # But split() on empty string is empty list.
        # I'll rely on join giving "" if empty list.
        pass
        
    if m > 0:
        input_lines.append(" ".join(map(str, min_h)))
    else:
        input_lines.append("")
        
    # Python join of empty list is empty string.
    # Note: If n=0, we print empty line?
    # Yes, make sure input format is robust.
    # Actually, let's check reader:
    # `max_heap = ... input().split()`
    # If I print a newline, input() reads it as empty string? Yes.
    
    input_str = "\n".join(input_lines)
    
    res = solve(n, m, max_h, min_h)
    output_str = str(res)
    
    return input_str, output_str

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    print(f"      {c['output']}")

def main():
    test_cases = {
        "problem_id": "HEP_MEDIAN_TWO_HEAPS_MERGE__4476",
        "samples": [],
        "public": [],
        "hidden": []
    }
    
    # Samples
    # 1. Example
    s1_n, s1_m = 2, 2
    s1_max = [1, 3]
    s1_min = [2, 4]
    si1, so1 = make_test_case(s1_n, s1_m, s1_max, s1_min)
    test_cases["samples"].append({"input": si1, "output": so1})
    
    # Public
    # 1. Odd Total Count
    p1_n, p1_m = 3, 2
    p1_max = [1, 2, 3]
    p1_min = [4, 5]
    # Sorted: 1 2 3 4 5. Median 3.
    pi1, po1 = make_test_case(p1_n, p1_m, p1_max, p1_min)
    test_cases["public"].append({"input": pi1, "output": po1})
    
    # 2. Even Total Count with .5
    p2_n, p2_m = 1, 1
    p2_max = [1]
    p2_min = [2]
    # Median 1.5
    pi2, po2 = make_test_case(p2_n, p2_m, p2_max, p2_min)
    test_cases["public"].append({"input": pi2, "output": po2})
    
    # Hidden
    hidden = []
    
    # 1. Edge: Empty one side
    h1_max = [10, 20, 30]
    h1_min = []
    hidden.append(make_test_case(3, 0, h1_max, h1_min))
    
    # 2. Edge: Single Element
    h2_max = []
    h2_min = [100]
    hidden.append(make_test_case(0, 1, h2_max, h2_min))
    
    # 3. Disjoint Ranges
    h3_max = [1, 2, 3, 4, 5]
    h3_min = [100, 101, 102, 103, 104]
    # 10 elements. Median between 5 and 100? No.
    # Sorted: 1, 2, 3, 4, 5, 100, ...
    # Mid indices 4 and 5 (0-indexed).
    # Items 5 and 100.
    # Avg (5+100)/2 = 52.5
    hidden.append(make_test_case(5, 5, h3_max, h3_min))
    
    # 4. Large Numbers
    h4_max = [10**9, 10**9]
    h4_min = [10**9, 10**9]
    hidden.append(make_test_case(2, 2, h4_max, h4_min))
    
    # 5. Negative Numbers
    h5_max = [-10, -5]
    h5_min = [-20, -1]
    # Sorted: -20, -10, -5, -1
    # Middle: -10, -5. Avg -7.5
    hidden.append(make_test_case(2, 2, h5_max, h5_min))
    
    # 6. Stress Small
    h6_n = 1000
    h6_arr = [i for i in range(2000)]
    random.shuffle(h6_arr)
    # Median should be (999 + 1000)/2 = 999.5
    hidden.append(make_test_case(h6_n, h6_n, h6_arr[:h6_n], h6_arr[h6_n:]))
    
    # 7. Stress Large (N=100000)
    h7_n = 50000
    h7_arr1 = [random.randint(1, 1000000) for _ in range(h7_n)]
    h7_arr2 = [random.randint(1, 1000000) for _ in range(h7_n)]
    hidden.append(make_test_case(h7_n, h7_n, h7_arr1, h7_arr2))

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
