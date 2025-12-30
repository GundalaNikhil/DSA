#!/usr/bin/env python3
"""
Simplified test case generator for HEP-010: Top K Products with Index Gap
Only simple, edge, corner, and basic test cases (no stress tests)
"""

import yaml
import heapq
import random

def top_k_products(A, B, k, d):
    """Reference solution."""
    n, m = len(A), len(B)
    pq = []
    visited = set()
    
    def push(r, c, direction):
        if 0 <= r < n and 0 <= c < m and abs(r - c) >= d:
            key = (r, c)
            if key not in visited:
                visited.add(key)
                val = A[r] * B[c]
                heapq.heappush(pq, (-val, r, c, direction))
    
    # TL Starts
    if d < n:
        push(d, 0, 1)
    if d < m and d > 0:
        push(0, d, 1)
    elif d == 0:
        push(0, 0, 1)
    
    # BR Starts
    if d < n:
        start_i = n - 1
        start_j = min(m - 1, n - 1 - d)
        if start_j >= 0:
            push(start_i, start_j, -1)
    
    if d < m and d > 0:
        start_j = m - 1
        start_i = min(n - 1, m - 1 - d)
        if start_i >= 0:
            push(start_i, start_j, -1)
    
    res = []
    while k > 0 and pq:
        val, r, c, direction = heapq.heappop(pq)
        res.append(-val)
        k -= 1
        
        if direction == 1:
            push(r + 1, c, 1)
            push(r, c + 1, 1)
        else:
            push(r - 1, c, -1)
            push(r, c - 1, -1)
    
    return res

def generate_test_cases():
    test_cases = {
        'problem_id': 'HEP_TOPK_PRODUCTS_INDEX_GAP__8206',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample from problem
    test_cases['samples'].append({
        'input': "3 3 3 1\n9 7 5\n8 3 1",
        'output': "56 40 27"
    })
    
    # Public (Simple)
    public_specs = [
        ([10, 5], [4, 2], 2, 0),
        ([5, 4, 3], [6, 2, 1], 5, 1),
        ([10, 5], [3, 2], 1, 2)
    ]
    for A, B, k, d in public_specs:
        result = top_k_products(A, B, k, d)
        inp = f"{len(A)} {len(B)} {k} {d}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        out = ' '.join(map(str, result)) if result else ""
        test_cases['public'].append({'input': inp, 'output': out})
    
    # Hidden (Edge, Corner, Basic)
    hidden_specs = [
        ([1], [1], 1, 0, "Edge: Single element each, d=0"),
        ([10, 5], [3, 2], 1, 1, "Corner: Small arrays with d=1"),
        ([5, 4, 3, 2, 1], [10, 9, 8, 7, 6], 3, 0, "Basic: d=0, all pairs valid"),
        ([10, 5, 1], [20, 10, 5], 2, 2, "Corner: d=2, limited valid pairs"),
        ([7, 6, 5, 4], [8, 6, 4, 2], 5, 1, "Basic: d=1, k=5"),
        ([-5, -10], [-3, -8], 2, 0, "Edge: Negative numbers"),
    ]
    
    for A, B, k, d, desc in hidden_specs:
        result = top_k_products(A, B, k, d)
        inp = f"{len(A)} {len(B)} {k} {d}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        out = ' '.join(map(str, result)) if result else ""
        test_cases['hidden'].append({'input': inp, 'output': out})
    
    # Add more to reach 30
    for i in range(30 - len(test_cases['hidden'])):
        n = random.randint(10, 50)
        m = random.randint(10, 50)
        k = random.randint(1, 10)
        d = random.randint(0, min(n, m) - 1)
        A = sorted([random.randint(-100, 100) for _ in range(n)], reverse=True)
        B = sorted([random.randint(-100, 100) for _ in range(m)], reverse=True)
        result = top_k_products(A, B, k, d)
        inp = f"{n} {m} {k} {d}\n{' '.join(map(str, A))}\n{' '.join(map(str, B))}"
        out = ' '.join(map(str, result)) if result else ""
        test_cases['hidden'].append({'input': inp, 'output': out})
    
    return test_cases

def main():
    test_cases = generate_test_cases()
    output_path = '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Heaps/testcases/HEP-010-topk-products-index-gap.yaml'
    
    with open(output_path, 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"✅ Generated {len(test_cases['samples'])} samples, {len(test_cases['public'])} public, {len(test_cases['hidden'])} hidden test cases for HEP-010")

if __name__ == '__main__':
    main()
