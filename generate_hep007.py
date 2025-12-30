#!/usr/bin/env python3
import yaml
import random
import heapq
from collections import Counter, defaultdict

class DualHeap:
    def __init__(self, k):
        self.k = k
        self.small = []  # Max-heap
        self.large = []  # Min-heap
        self.small_count = 0
        self.large_count = 0
        self.lazy = Counter()
        self.in_small = defaultdict(int)
        self.in_large = defaultdict(int)
    
    def _prune(self, heap, is_small):
        while heap:
            val = -heap[0] if is_small else heap[0]
            if self.lazy[val] > 0:
                self.lazy[val] -= 1
                heapq.heappop(heap)
            else:
                break
    
    def add(self, x):
        if self.small_count < self.k:
            heapq.heappush(self.small, -x)
            self.small_count += 1
            self.in_small[x] += 1
        else:
            self._prune(self.small, True)
            if not self.small:
                heapq.heappush(self.small, -x)
                self.small_count += 1
                self.in_small[x] += 1
            else:
                small_max = -self.small[0]
                if x <= small_max:
                    heapq.heappop(self.small)
                    self.in_small[small_max] -= 1
                    heapq.heappush(self.small, -x)
                    self.in_small[x] += 1
                    heapq.heappush(self.large, small_max)
                    self.in_large[small_max] += 1
                    self.large_count += 1
                else:
                    heapq.heappush(self.large, x)
                    self.in_large[x] += 1
                    self.large_count += 1
        self._balance()

    def remove(self, x):
        self.lazy[x] += 1
        if self.in_small[x] > 0:
            self.in_small[x] -= 1
            self.small_count -= 1
        else:
            self.in_large[x] -= 1
            self.large_count -= 1
        self._balance()

    def _balance(self):
        self._prune(self.small, True)
        self._prune(self.large, False)
        while self.small_count < self.k and self.large:
            self._prune(self.large, False)
            if not self.large: break
            val = heapq.heappop(self.large)
            self.in_large[val] -= 1
            heapq.heappush(self.small, -val)
            self.in_small[val] += 1
            self.small_count += 1
            self.large_count -= 1
            self._prune(self.small, True)
        while self.small_count > self.k:
            self._prune(self.small, True)
            val = -heapq.heappop(self.small)
            self.in_small[val] -= 1
            heapq.heappush(self.large, val)
            self.in_large[val] += 1
            self.small_count -= 1
            self.large_count += 1
            self._prune(self.large, False)

    def get_kth_smallest(self):
        self._prune(self.small, True)
        if self.small:
            return -self.small[0]
        return None

def solve(n, w, k, arr):
    dh = DualHeap(k)
    result = []
    for i in range(w):
        dh.add(arr[i])
    result.append(dh.get_kth_smallest())
    for i in range(w, n):
        dh.remove(arr[i-w])
        dh.add(arr[i])
        result.append(dh.get_kth_smallest())
    return result

def generate():
    random.seed(42)
    test_cases = {'problem_id': 'HEP_SLIDING_WINDOW_KTH_SMALLEST__2665', 'samples': [], 'public': [], 'hidden': []}
    
    # Existing sample
    arr = [1, 3, 2, 6, 4]
    test_cases['samples'].append({'input': "5 3 2\n1 3 2 6 4", 'output': " ".join(map(str, solve(5, 3, 2, arr)))})
    
    # Public cases
    public_specs = [(5, 2, 1, [10, 20, 5, 15, 30]), (10, 4, 2, [random.randint(1, 100) for _ in range(10)]), (8, 3, 3, [random.randint(1, 50) for _ in range(8)])]
    for n, w, k, arr in public_specs:
        test_cases['public'].append({'input': f"{n} {w} {k}\n" + " ".join(map(str, arr)), 'output': " ".join(map(str, solve(n, w, k, arr)))})
    
    # Hidden cases - 30 cases
    for i in range(30):
        if i < 5: # Edge cases
            n = random.randint(1, 10)
            w = random.randint(1, n)
            k = random.randint(1, w)
            arr = [random.randint(1, 20) for _ in range(n)]
        elif i < 15: # Random normal
            n = random.randint(50, 200)
            w = random.randint(10, 50)
            k = random.randint(1, w)
            arr = [random.randint(1, 1000) for _ in range(n)]
        elif i < 25: # Large values, duplicates
            n = random.randint(500, 1000)
            w = random.randint(100, 500)
            k = random.randint(1, w)
            arr = [random.randint(1, 100) for _ in range(n)] # High chance of duplicates
        else: # Stress cases
            n = 2000
            w = 500
            k = 250
            arr = [random.randint(1, 10**6) for _ in range(n)]
            
        test_cases['hidden'].append({'input': f"{n} {w} {k}\n" + " ".join(map(str, arr)), 'output': " ".join(map(str, solve(n, w, k, arr)))})
        
    with open('/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Heaps/testcases/HEP-007-sliding-window-kth-smallest.yaml', 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    generate()
