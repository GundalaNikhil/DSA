
import sys
import random
import bisect

# --- Reference Solution ---
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def find_kth(self, k):
        # Binary search on the BIT
        idx = 0
        for i in range(len(self.tree).bit_length() - 1, -1, -1):
            next_idx = idx + (1 << i)
            if next_idx < len(self.tree) and self.tree[next_idx] < k:
                idx = next_idx
                k -= self.tree[idx]
        return idx + 1

def solve(q, T, operations):
    # Coordinate Compression
    values = set()
    for op in operations:
        if op[0] in ("ADD", "DEL"):
            values.add(int(op[1]))
    
    sorted_vals = sorted(list(values))
    rank_map = {val: i + 1 for i, val in enumerate(sorted_vals)}
    
    bit = FenwickTree(len(sorted_vals))
    current_size = 0
    multiset_counts = {} # To track existence for DEL
    
    outputs = []
    
    for op in operations:
        type = op[0]
        if type == "ADD":
            val = int(op[1])
            rank = rank_map[val]
            bit.update(rank, 1)
            multiset_counts[val] = multiset_counts.get(val, 0) + 1
            current_size += 1
            
        elif type == "DEL":
            val = int(op[1])
            if multiset_counts.get(val, 0) > 0:
                rank = rank_map[val]
                bit.update(rank, -1)
                multiset_counts[val] -= 1
                if multiset_counts[val] == 0:
                    del multiset_counts[val]
                current_size -= 1
                
        elif type == "MEDIAN":
            if current_size == 0:
                outputs.append("EMPTY")
            elif current_size < T:
                outputs.append("NA")
            else:
                k = (current_size + 1) // 2
                rank_k = bit.find_kth(k)
                outputs.append(str(sorted_vals[rank_k - 1]))
                
    return outputs

# --- Test Case Generators ---

def generate_sample_1():
    q = 4
    T = 2
    ops = [
        ["ADD", "1"],
        ["ADD", "5"],
        ["DEL", "1"],
        ["MEDIAN"]
    ]
    return q, T, ops

def generate_random(q, T, min_val, max_val, prob_add=0.6, prob_del=0.2):
    ops = []
    active_elements = []  # Just to help probability of valid deletes
    
    for _ in range(q):
        r = random.random()
        if r < prob_add:
            val = random.randint(min_val, max_val)
            ops.append(["ADD", str(val)])
            active_elements.append(val)
        elif r < prob_add + prob_del:
            if active_elements and random.random() < 0.8:
                val = random.choice(active_elements)
                ops.append(["DEL", str(val)])
                # Don't strictly remove from active_elements list to keep it fast, 
                # simulation will handle it. But to increase hit rate, good to remove.
                # removing is O(N), so we just pick random.
            else:
                val = random.randint(min_val, max_val)
                ops.append(["DEL", str(val)])
        else:
            ops.append(["MEDIAN"])
    return q, T, ops

# --- YAML Builder ---

def format_input(q, T, ops):
    lines = [f"{q} {T}"]
    for op in ops:
        lines.append(" ".join(op))
    return "\n".join(lines)

def format_output(outputs):
    return "\n".join(outputs)

def make_test_case(q, T, ops):
    input_str = format_input(q, T, ops)
    output_list = solve(q, T, ops)
    output_str = format_output(output_list)
    return input_str, output_str


def main():
    test_cases = {
        "problem_id": "HEP_RUNNING_MEDIAN_DELETE_THRESHOLD__4217",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    sq, st, sops = generate_sample_1()
    si, so = make_test_case(sq, st, sops)
    test_cases["samples"].append({"input": si, "output": so})
    
    # Sample 2 (User defined simple)
    s2q, s2t = 6, 2
    s2ops = [
        ["ADD", "10"],
        ["MEDIAN"],   # size 1 < 2 -> NA
        ["ADD", "20"],
        ["MEDIAN"],   # size 2 -> 10
        ["ADD", "30"],
        ["MEDIAN"]    # size 3 -> 20
    ]
    s2i, s2o = make_test_case(s2q, s2t, s2ops)
    test_cases["samples"].append({"input": s2i, "output": s2o})

    # Public
    # Edge: Minimum
    pq1, pt1 = 1, 0
    p1ops = [["MEDIAN"]]
    pi1, po1 = make_test_case(pq1, pt1, p1ops)
    test_cases["public"].append({"input": pi1, "output": po1}) # EMPTY
    
    # Edge: Empty/Zero
    pq2, pt2 = 5, 5
    p2ops = [["MEDIAN"]]*5
    pi2, po2 = make_test_case(pq2, pt2, p2ops)
    test_cases["public"].append({"input": pi2, "output": po2})

    # Basic
    pq3, pt3 = 5, 1
    p3ops = [["ADD", "10"], ["MEDIAN"], ["ADD", "5"], ["MEDIAN"], ["DEL", "10"]]
    pi3, po3 = make_test_case(pq3, pt3, p3ops)
    test_cases["public"].append({"input": pi3, "output": po3})
    
    # Boundary
    pq4, pt4 = 5, 2
    p4ops = [["ADD", "1"], ["ADD", "2"], ["MEDIAN"], ["DEL", "1"], ["MEDIAN"]]
    pi4, po4 = make_test_case(pq4, pt4, p4ops)
    test_cases["public"].append({"input": pi4, "output": po4})


    # Hidden
    hidden_cases = []
    
    # 1. Edge: T=0
    h1q, h1t, h1ops = generate_random(20, 0, 1, 100, 0.5, 0.2)
    hidden_cases.append(make_test_case(h1q, h1t, h1ops))
    
    # 2. Edge: T=max, q=max
    h2q, h2t = 50, 100
    _, _, h2ops = generate_random(50, 100, 1, 100, 0.8, 0.0) # Mostly adds
    hidden_cases.append(make_test_case(h2q, h2t, h2ops))
    
    # 3. Edge: All deletes on empty
    h3ops = [["DEL", "5"]] * 10 + [["MEDIAN"]]
    hidden_cases.append(make_test_case(11, 2, h3ops))

    # 4. Edge: Single element median
    h4ops = [["ADD", "42"], ["MEDIAN"], ["DEL", "42"], ["MEDIAN"]]
    hidden_cases.append(make_test_case(4, 1, h4ops))
    
    # 5. Boundary: Alternating Add/Del to keep size around T
    h5t = 5
    h5ops = []
    vals = [1, 2, 3, 4, 5]
    for v in vals: h5ops.append(["ADD", str(v)]) # size 5
    h5ops.append(["MEDIAN"])
    h5ops.append(["DEL", "1"]) # size 4 -> NA
    h5ops.append(["MEDIAN"])
    h5ops.append(["ADD", "6"]) # size 5 -> median
    h5ops.append(["MEDIAN"])
    hidden_cases.append(make_test_case(len(h5ops), h5t, h5ops))
    
    # 6. Negative/NA: Never reach T
    h6q, h6t, h6ops = generate_random(20, 50, 1, 100, 0.5, 0.1) # Max size likely < 20 < 50
    hidden_cases.append(make_test_case(h6q, h6t, h6ops))

    # 7. Negative: No solution? (Just NA or EMPTY) - Repeated empty checks
    h7ops = [["MEDIAN"]]*10
    hidden_cases.append(make_test_case(10, 1, h7ops))
    
    # 8. Special: All same values
    h8ops = []
    for _ in range(10): h8ops.append(["ADD", "7"])
    h8ops.append(["MEDIAN"])
    h8ops.append(["DEL", "7"])
    h8ops.append(["MEDIAN"])
    hidden_cases.append(make_test_case(len(h8ops), 1, h8ops))
    
    # 9. Normal: Random Small
    h9q, h9t, h9ops = generate_random(50, 5, 1, 100)
    hidden_cases.append(make_test_case(h9q, h9t, h9ops))
    
    # 10. Normal: Random Medium
    h10q, h10t, h10ops = generate_random(100, 10, 1, 1000)
    hidden_cases.append(make_test_case(h10q, h10t, h10ops))
    
    # 11. Stress 1: Large Q, many adds, T small
    h11q, h11t, h11ops = generate_random(1000, 10, 1, 10000)
    hidden_cases.append(make_test_case(h11q, h11t, h11ops))
    
    # 12. Stress 2: Large Q, many adds, T large
    h12q, h12t, h12ops = generate_random(1000, 500, 1, 10000)
    hidden_cases.append(make_test_case(h12q, h12t, h12ops))
    
    # 13. Stress 3: Max Constraints
    # generate_random might be slow for full 10^5 in python if we do it many times.
    # Let's do a moderate stress 5000 ops.
    h13q, h13t, h13ops = generate_random(5000, 100, -100000, 100000)
    hidden_cases.append(make_test_case(h13q, h13t, h13ops))
    
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
    if not c["output"]: # handle empty output case (shouldn't happen for this problem but good practice)
        pass 
    for line in c["output"].split("\n"):
        if line:
            print(f"      {line}")

if __name__ == "__main__":
    main()
