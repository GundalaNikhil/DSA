
import sys
import random
import heapq
# import collections # standard lib is allowed

# --- Reference Solution ---

class DualHeaps:
    def __init__(self, k):
        self.k = k
        self.small = [] # Max heap (stores negative)
        self.large = [] # Min heap
        self.small_size = 0 # Logical size
        self.large_size = 0 # Logical size
        self.deleted = {} # Map value -> count

    def _prune(self, heap, is_small):
        # Remove deleted elements from top
        while heap:
            val = -heap[0] if is_small else heap[0]
            if self.deleted.get(val, 0) > 0:
                self.deleted[val] -= 1
                if self.deleted[val] == 0:
                    del self.deleted[val]
                heapq.heappop(heap)
            else:
                break
    
    def add(self, val):
        # Always add to small first (conceptually), then balance
        if not self.small or val <= -self.small[0]:
            heapq.heappush(self.small, -val)
            self.small_size += 1
        else:
            heapq.heappush(self.large, val)
            self.large_size += 1
        self.balance()

    def remove(self, val):
        # We don't know exactly where val is, but we can guess based on split point
        # Split point is small[0] (max of small)
        # However, we might need to prune small to get the true split point
        self._prune(self.small, True)
        
        if self.small and val <= -self.small[0]:
            self.small_size -= 1
        else:
            self.large_size -= 1
            
        self.deleted[val] = self.deleted.get(val, 0) + 1
        self.balance()

    def balance(self):
        # Ensure small has exactly k elements (logically)
        
        # While too many in small, move to large
        while self.small_size > self.k:
            self._prune(self.small, True)
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.small_size -= 1
            self.large_size += 1

        # While too few in small, move from large
        while self.small_size < self.k and self.large_size > 0:
            self._prune(self.large, False)
            if not self.large: break # Should not happen if sizes correct
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.small_size += 1
            self.large_size -= 1
            
        # Prune tops after moves
        self._prune(self.small, True)
        self._prune(self.large, False)

    def get_kth(self):
        self._prune(self.small, True)
        if self.small:
            return -self.small[0]
        return 0 # Should not happen

def solve(n, w, k, arr):
    # Sliding window finding kth smallest
    # 1 <= n <= 200000
    # O(n log(w))
    
    dh = DualHeaps(k)
    res = []
    
    # Initialize first window
    for i in range(w):
        dh.add(arr[i])
        
    res.append(dh.get_kth())
    
    # Slide
    for i in range(w, n):
        # Remove arr[i-w]
        dh.remove(arr[i-w])
        # Add arr[i]
        dh.add(arr[i])
        res.append(dh.get_kth())
        
    return res

# --- Test Case Generators ---

def generate_random(n, w_exact, k_exact, min_val, max_val):
    w = w_exact if w_exact else random.randint(1, n)
    k = k_exact if k_exact else random.randint(1, w)
    arr = [random.randint(min_val, max_val) for _ in range(n)]
    return n, w, k, arr

# --- YAML Builder ---

def format_input(n, w, k, arr):
    lines = [f"{n} {w} {k}"]
    lines.append(" ".join(map(str, arr)))
    return "\n".join(lines)

def format_output(res):
    return " ".join(map(str, res))

def make_test_case(n, w, k, arr):
    input_str = format_input(n, w, k, arr)
    output_val = solve(n, w, k, arr)
    output_str = format_output(output_val)
    return input_str, output_str

def main():
    test_cases = {
        "problem_id": "HEP_SLIDING_WINDOW_KTH_SMALLEST__2665", # from md file
        "samples": [],
        "public": [],
        "hidden": []
    }
    
    # Samples
    # 1. Example
    s1_n, s1_w, s1_k = 5, 3, 2
    s1_arr = [1, 3, 2, 6, 4]
    si1, so1 = make_test_case(s1_n, s1_w, s1_k, s1_arr)
    test_cases["samples"].append({"input": si1, "output": so1})
    
    # Public
    # 1. Basic small
    p1_n, p1_w, p1_k = 5, 2, 1
    p1_arr = [10, 20, 5, 15, 30]
    # Windows: [10,20]->10, [20,5]->5, [5,15]->5, [15,30]->15
    pi1, po1 = make_test_case(p1_n, p1_w, p1_k, p1_arr)
    test_cases["public"].append({"input": pi1, "output": po1})
    
    # 2. k = w (Max in window)
    p2_n, p2_w, p2_k = 6, 3, 3
    p2_arr = [1, 5, 2, 8, 3, 7]
    pi2, po2 = make_test_case(p2_n, p2_w, p2_k, p2_arr)
    test_cases["public"].append({"input": pi2, "output": po2})
    
    # 3. Sorted array
    p3_n, p3_w, p3_k = 5, 3, 2
    p3_arr = [1, 2, 3, 4, 5]
    # [1,2,3]->2, [2,3,4]->3, [3,4,5]->4
    pi3, po3 = make_test_case(p3_n, p3_w, p3_k, p3_arr)
    test_cases["public"].append({"input": pi3, "output": po3})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: w=1 (output matches input)
    h1_n = 20
    h1_w, h1_k = 1, 1
    h1_arr = [random.randint(1, 100) for _ in range(h1_n)]
    hidden_cases.append(make_test_case(h1_n, h1_w, h1_k, h1_arr))
    
    # 2. Edge: w=n (single output)
    h2_n = 20
    h2_w, h2_k = 20, 10
    h2_arr = [random.randint(1, 100) for _ in range(h2_n)]
    hidden_cases.append(make_test_case(h2_n, h2_w, h2_k, h2_arr))
    
    # 3. Edge: All same elements
    h3_n, h3_w, h3_k = 20, 5, 3
    h3_arr = [7] * 20
    hidden_cases.append(make_test_case(h3_n, h3_w, h3_k, h3_arr))
    
    # 4. Stress: N=1000, w=100, k=50
    h4_n, h4_w, h4_k = 1000, 100, 50
    h4_arr = [random.randint(1, 1000) for _ in range(h4_n)]
    hidden_cases.append(make_test_case(h4_n, h4_w, h4_k, h4_arr))
    
    # 5. Stress: N=5000, Large values
    h5_n, h5_w, h5_k = 5000, 500, 250
    h5_arr = [random.randint(-10**9, 10**9) for _ in range(h5_n)]
    hidden_cases.append(make_test_case(h5_n, h5_w, h5_k, h5_arr))
    
    # 6. Negative values only
    h6_n, h6_w, h6_k = 50, 10, 5
    h6_arr = [random.randint(-100, -1) for _ in range(h6_n)]
    hidden_cases.append(make_test_case(h6_n, h6_w, h6_k, h6_arr))
    
    # 7. Reverse sorted
    h7_n, h7_w, h7_k = 20, 5, 3
    h7_arr = list(range(20, 0, -1))
    hidden_cases.append(make_test_case(h7_n, h7_w, h7_k, h7_arr))
    
    # 8. Alternating high-low
    h8_arr = []
    for i in range(100):
        h8_arr.append(1)
        h8_arr.append(1000)
    h8_n = len(h8_arr)
    h8_w, h8_k = 10, 5
    hidden_cases.append(make_test_case(h8_n, h8_w, h8_k, h8_arr))
    
    # 9. Large Window (almost N)
    h9_n = 200
    h9_w, h9_k = 190, 100
    h9_arr = [random.randint(1, 10000) for _ in range(h9_n)]
    hidden_cases.append(make_test_case(h9_n, h9_w, h9_k, h9_arr))
    
    # 10. Random Case
    h10_n, h10_w, h10_k = 500, 50, 10
    h10_arr = [random.randint(1, 1000) for _ in range(h10_n)]
    hidden_cases.append(make_test_case(h10_n, h10_w, h10_k, h10_arr))

    # Add hidden
    for inp, out in hidden_cases:
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

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    print(f"      {c['output']}")

if __name__ == "__main__":
    main()
