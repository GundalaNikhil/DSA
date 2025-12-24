
import sys
import random
import heapq
from functools import cmp_to_key

# --- Reference Solution ---

class HeapItem:
    def __init__(self, x, y, w, id):
        self.x = x
        self.y = y
        self.w = w
        self.id = id
        self.num = x*x + y*y
        self.den = w

    def __lt__(self, other):
        # Max-heap logic: we want to pop the 'worst' element.
        # Python heapq is a min-heap. Top is the 'smallest' element according to __lt__.
        # So "Worst" should be "Smallest".
        # Worst element: Largest distance.
        # If distances equal: Largest ID is worse (we prefer smaller IDs).
        
        # Check if self is "worse" than other
        # self.dist > other.dist ?
        lhs = self.num * other.den
        rhs = other.num * self.den
        
        if lhs > rhs:
            return True # self has larger distance, so it is worse ("smaller" in our inverted logic)
        if lhs < rhs:
            return False
            
        # Distances equal
        # Larger ID is worse
        return self.id > other.id

def compare_for_output(a, b):
    # Sort by distance ascending, then id ascending
    # a and b are HeapItem objects
    lhs = a.num * b.den
    rhs = b.num * a.den
    
    if lhs < rhs:
        return -1
    if lhs > rhs:
        return 1
    
    # Distances equal, sort by id ascending
    if a.id < b.id:
        return -1
    if a.id > b.id:
        return 1
    return 0

def solve(q, k, operations):
    heap = [] # will store HeapItem
    results = []
    
    points_added = 0
    current_id = 1
    
    for op_parts in operations:
        op_type = op_parts[0]
        
        if op_type == "ADD":
            x = int(op_parts[1])
            y = int(op_parts[2])
            w = int(op_parts[3])
            
            new_item = HeapItem(x, y, w, current_id)
            current_id += 1
            
            if len(heap) < k:
                heapq.heappush(heap, new_item)
            else:
                # Heap is full. Check if new item is better than the worst (top)
                # Top is the 'worst' element (smallest in our inverted logic)
                worst = heap[0]
                
                # We want to replace worst if new_item is BETTER than worst.
                # Better = Smaller distance, or equal distance and smaller ID.
                # In our inverted logic, "Better" means "Greater" than "Worst" (since Worst is the "Smallest").
                # Let's verify:
                # item < worst means item is WORSE than worst.
                # item > worst means item is BETTER than worst.
                
                # Wait, let's re-verify __lt__
                # __lt__ returns True if self is WORSE.
                # So if new_item < worst, then new_item is WORSE than worst.
                # We only insert if new_item is BETTER than worst.
                # If new_item is BETTER, then worst is WORSE than new_item.
                # So worst < new_item.
                
                if worst < new_item:
                    # worst is indeed worse than new_item.
                    # so we discard worst and keep new_item.
                    heapq.heappop(heap)
                    heapq.heappush(heap, new_item)
                else:
                    # worst is better or equal to new_item?
                    # No, strict ordering.
                    # If not (worst < new_item), then worst >= new_item.
                    # Meaning worst is better (smaller dist/id) or equal.
                    # But worst is supposedly the worst in the heap.
                    # If new_item is worse than the worst in the heap, we definitely don't want it.
                    pass

        elif op_type == "QUERY":
            if not heap:
                results.append("EMPTY")
            else:
                # Return ids sorted
                sorted_items = sorted(heap, key=cmp_to_key(compare_for_output))
                results.append(" ".join(str(item.id) for item in sorted_items))
                
    return results

# --- Test Case Generators ---

def generate_random_ops(q, k, prob_add=0.7, min_coord=-100, max_coord=100, max_w=100):
    ops = []
    
    # Ensure at least some adds
    for _ in range(q):
        if random.random() < prob_add:
            x = random.randint(min_coord, max_coord)
            y = random.randint(min_coord, max_coord)
            w = random.randint(1, max_w)
            ops.append(["ADD", str(x), str(y), str(w)])
        else:
            ops.append(["QUERY"])
    return ops

def make_test_case(q, k, operations):
    # operations is list of lists
    input_str = f"{q} {k}\n" + "\n".join(" ".join(op) for op in operations)
    res = solve(q, k, operations)
    output_str = "\n".join(res)
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
        "problem_id": "HEP_K_CLOSEST_STREAM_WEIGHT__4950",
        "samples": [],
        "public": [],
        "hidden": []
    }
    
    # Samples
    # 1. Example 1
    # 3 1
    # ADD 1 1 1
    # ADD 2 2 1
    # QUERY
    s1_ops = [
        ["ADD", "1", "1", "1"],
        ["ADD", "2", "2", "1"],
        ["QUERY"]
    ]
    si1, so1 = make_test_case(3, 1, s1_ops)
    test_cases["samples"].append({"input": si1, "output": so1})
    
    # Public
    # 1. Basic Sequence
    p1_q, p1_k = 5, 2
    p1_ops = [
        ["ADD", "10", "10", "1"], # dist 200
        ["QUERY"],                # 1
        ["ADD", "1", "1", "1"],   # dist 2
        ["QUERY"],                # 2 1
        ["ADD", "5", "5", "100"]  # dist (50)/100 = 0.5
    ]
    # Final state: 1(200), 2(2), 3(0.5). k=2. Remove worst (1). Keep 2, 3.
    # Sorted by dist: 3(0.5), 2(2). Output "3 2" theoretically.
    # Add final query
    p1_ops.append(["QUERY"])
    pi1, po1 = make_test_case(6, p1_k, p1_ops)
    test_cases["public"].append({"input": pi1, "output": po1})
    
    # 2. Tie Breaking
    p2_q, p2_k = 5, 1
    p2_ops = [
        ["ADD", "2", "2", "1"], # dist 8, id 1
        ["ADD", "2", "2", "1"], # dist 8, id 2
        ["QUERY"],              # Keep min dist, min id. Both dist 8. id 1 < id 2. Keep 1.
        ["ADD", "1", "1", "1"], # dist 2, id 3. Better than 1.
        ["QUERY"]               # 3
    ]
    pi2, po2 = make_test_case(5, p2_k, p2_ops)
    test_cases["public"].append({"input": pi2, "output": po2})
    
    # Hidden
    hidden = []
    
    # 1. Edge: No Points
    h1_ops = [["QUERY"]]
    hidden.append(make_test_case(1, 10, h1_ops))
    
    # 2. Edge: Fewer than k points
    h2_ops = [["ADD", "1", "1", "1"], ["QUERY"]]
    hidden.append(make_test_case(2, 5, h2_ops))
    
    # 3. Edge: Exactly k points
    h3_ops = [["ADD", str(i), "1", "1"] for i in range(5)]
    h3_ops.append(["QUERY"])
    hidden.append(make_test_case(6, 5, h3_ops))
    
    # 4. Large Coordinates
    h4_ops = [
        ["ADD", "1000000", "1000000", "1"],
        ["ADD", "-1000000", "-1000000", "1"],
        ["QUERY"]
    ]
    hidden.append(make_test_case(3, 1, h4_ops))
    
    # 5. Large Weights vs Small Weights
    h5_ops = [
        ["ADD", "10", "10", "1000000"], # very small dist
        ["ADD", "1", "1", "1"],         # dist 2
        ["QUERY"]
    ]
    hidden.append(make_test_case(3, 2, h5_ops))
    
    # 6. Stress Small
    h6_q, h6_k = 100, 10
    h6_ops = generate_random_ops(h6_q, h6_k, prob_add=0.8)
    hidden.append(make_test_case(h6_q, h6_k, h6_ops))

    # 7. Stress Medium
    h7_q, h7_k = 1000, 100
    h7_ops = generate_random_ops(h7_q, h7_k, prob_add=0.8, min_coord=-1000, max_coord=1000, max_w=1000)
    hidden.append(make_test_case(h7_q, h7_k, h7_ops))
    
    # 8. All Queries
    h8_ops = [["QUERY"] for _ in range(50)]
    hidden.append(make_test_case(50, 5, h8_ops))
    
    # 9. All Adds then One Query
    h9_n = 500
    h9_ops = [["ADD", str(random.randint(1,100)), str(random.randint(1,100)), str(random.randint(1,100))] for _ in range(h9_n)]
    h9_ops.append(["QUERY"])
    hidden.append(make_test_case(h9_n+1, 10, h9_ops))

    # 10. Max Constraints (validating efficient logic)
    # We won't go full 10^5 in python generated string for sanity, but enough to test logic correctness
    h10_q, h10_k = 2000, 50
    h10_ops = generate_random_ops(h10_q, h10_k, prob_add=0.6, min_coord=-10000, max_coord=10000, max_w=10000)
    hidden.append(make_test_case(h10_q, h10_k, h10_ops))

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
