#!/usr/bin/env python3
"""
Test case generator for HEP-008: Huffman with Merge Limit
Generates comprehensive test cases following the Universal DSA Problem Generation Prompt
"""

import yaml
import random
import heapq
from typing import List

def huffman_cost(freq: List[int], m: int) -> int:
    """Reference solution for generating correct outputs."""
    pq = [x for x in freq]
    heapq.heapify(pq)
    
    # Padding
    while (len(pq) - 1) % (m - 1) != 0:
        heapq.heappush(pq, 0)
        
    total_cost = 0
    
    while len(pq) > 1:
        current_sum = 0
        for _ in range(m):
            current_sum += heapq.heappop(pq)
        
        total_cost += current_sum
        heapq.heappush(pq, current_sum)
        
    return total_cost

def generate_test_cases():
    test_cases = {
        'problem_id': 'HEP_HUFFMAN_MERGE_LIMIT__1584',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample test cases
    samples = [
        # Sample from problem description
        ([5, 7, 10], 2),
    ]
    
    for freq, m in samples:
        n = len(freq)
        inp = f"{n} {m}\n{' '.join(map(str, freq))}"
        out = str(huffman_cost(freq, m))
        test_cases['samples'].append({'input': inp, 'output': out})
    
    # Public test cases
    public = [
        ([1, 1, 1, 1], 2),  # All equal
        ([10, 20, 30], 3),  # 3-ary, no padding needed
        ([1, 2, 3, 4, 5], 2),  # Sequential
        ([100], 2),  # Single element (edge case)
    ]
    
    for freq, m in public:
        n = len(freq)
        inp = f"{n} {m}\n{' '.join(map(str, freq))}"
        out = str(huffman_cost(freq, m))
        test_cases['public'].append({'input': inp, 'output': out})
    
    # Hidden test cases
    hidden_specs = [
        # Edge: single element
        ([1000000000], 2, "Edge: Single large value"),
        ([0, 0, 0], 2, "Edge: All zeros"),
        
        # Boundary: min/max m
        ([1, 2, 3, 4, 5], 2, "Boundary: m=2 (binary)"),
        ([1, 2, 3, 4, 5, 6, 7], 5, "Boundary: m=5 (max)"),
        
        # Negative: zeros in input
        ([0, 1, 2, 3], 2, "Negative: Contains zeros"),
        ([0, 0, 1, 1, 1], 3, "Negative: Multiple zeros"),
        
        # Special: Padding scenarios
        ([10, 10, 10, 10], 3, "Special: Needs padding (example from editorial)"),
        ([1, 1, 1, 1, 1, 1, 1], 2, "Special: No padding needed (n-1)%(m-1)=0"),
        
        # Normal: Mixed values
        ([random.randint(1, 100) for _ in range(10)], 2, "Normal: Random 10 values, m=2"),
        ([random.randint(1, 1000) for _ in range(15)], 3, "Normal: Random 15 values, m=3"),
        ([random.randint(1, 10000) for _ in range(20)], 4, "Normal: Random 20 values, m=4"),
        
        # Stress: Large inputs
        ([random.randint(1, 1000000) for _ in range(100)], 2, "Stress: 100 values, m=2"),
        ([random.randint(1, 100000) for _ in range(500)], 3, "Stress: 500 values, m=3"),
        ([random.randint(1, 100000) for _ in range(1000)], 2, "Stress: 1000 values, m=2"),
        ([i for i in range(1, 1001)], 5, "Stress: Sequential 1-1000, m=5"),
    ]
    
    for freq, m, desc in hidden_specs:
        n = len(freq)
        inp = f"{n} {m}\n{' '.join(map(str, freq))}"
        out = str(huffman_cost(freq, m))
        test_cases['hidden'].append({'input': inp, 'output': out})
    
    # Add more to reach 30
    for i in range(30 - len(test_cases['hidden'])):
        n = random.randint(1000, 5000)
        m = random.randint(2, 5)
        freq = [random.randint(1, 10**6) for _ in range(n)]
        inp = f"{n} {m}\n{' '.join(map(str, freq))}"
        out = str(huffman_cost(freq, m))
        test_cases['hidden'].append({'input': inp, 'output': out})
    
    return test_cases

def main():
    random.seed(42)  # For reproducibility
    test_cases = generate_test_cases()
    
    output_path = '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Heaps/testcases/HEP-008-huffman-merge-limit.yaml'
    
    with open(output_path, 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"✅ Generated {len(test_cases['samples'])} samples, {len(test_cases['public'])} public, {len(test_cases['hidden'])} hidden test cases")
    print(f"   Saved to: {output_path}")

if __name__ == '__main__':
    main()
