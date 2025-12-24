
import random
import heapq
import yaml
import os

def solve(n, m, freq):
    """
    Reference solution for Huffman with Merge Limit using m-ary Huffman.
    """
    if n == 0:
        return 0
    if n == 1:
        return 0
    
    # Pad with 0s if necessary
    # We want (total_nodes - 1) % (m - 1) == 0
    # Let rem = (n - 1) % (m - 1)
    # if rem != 0, we need to add (m - 1) - rem zeros.
    
    rem = (n - 1) % (m - 1)
    if rem != 0:
        needed = (m - 1) - rem
        freq.extend([0] * needed)
    
    heapq.heapify(freq)
    
    total_cost = 0
    
    while len(freq) > 1:
        current_sum = 0
        # Extract up to m elements
        # Due to padding, we should always be able to extract exactly m
        # unless something is wrong or loop condition is subtle.
        # Actually with correct padding, (len - 1) is divisible by (m-1).
        # So len = k*(m-1) + 1. Since len > 1, len >= m.
        
        for _ in range(m):
            if freq:
                current_sum += heapq.heappop(freq)
        
        total_cost += current_sum
        heapq.heappush(freq, current_sum)
        
    return total_cost

def generate_test_cases():
    test_cases = []
    
    # -------------------------------------------------------------------------
    # 1. SAMPLE TEST CASES
    # -------------------------------------------------------------------------
    
    # Sample 1
    input_sample1 = {
        "n": 3,
        "m": 2,
        "freq": [5, 7, 10]
    }
    output_sample1 = solve(input_sample1["n"], input_sample1["m"], list(input_sample1["freq"]))
    test_cases.append({
        "input": f"{input_sample1['n']} {input_sample1['m']}\n{' '.join(map(str, input_sample1['freq']))}",
        "output": str(output_sample1),
        "category": "sample",
        "description": "Sample case with binary merge"
    })
    
    # -------------------------------------------------------------------------
    # 2. HIDDEN: EDGE CASES
    # -------------------------------------------------------------------------
    
    # Edge Case 1: n = 1 (Already merged, 0 cost)
    n_edge1, m_edge1 = 1, 3
    freq_edge1 = [100]
    test_cases.append({
        "input": f"{n_edge1} {m_edge1}\n{' '.join(map(str, freq_edge1))}",
        "output": str(solve(n_edge1, m_edge1, list(freq_edge1))),
        "category": "edge",
        "description": "Smallest n (1), no merges needed"
    })

    # Edge Case 2: n small, < m, needs padding
    n_edge2, m_edge2 = 2, 5
    freq_edge2 = [10, 20]
    # Here n=2, m=5. (2-1)%(4) = 1 != 0. Need 3 zeros.
    # Total nodes = 5. One merge of 5 items (0, 0, 0, 10, 20) -> sum 30. Cost 30.
    test_cases.append({
        "input": f"{n_edge2} {m_edge2}\n{' '.join(map(str, freq_edge2))}",
        "output": str(solve(n_edge2, m_edge2, list(freq_edge2))),
        "category": "edge",
        "description": "n < m, requires padding"
    })
    
    # Edge Case 3: Zeros in input
    n_edge3, m_edge3 = 5, 2
    freq_edge3 = [0, 0, 5, 5, 10]
    test_cases.append({
        "input": f"{n_edge3} {m_edge3}\n{' '.join(map(str, freq_edge3))}",
        "output": str(solve(n_edge3, m_edge3, list(freq_edge3))),
        "category": "edge",
        "description": "Input contains zeros"
    })

    # -------------------------------------------------------------------------
    # 3. HIDDEN: BOUNDARY CASES
    # -------------------------------------------------------------------------
    
    # Boundary 1: n is exactly such that (n-1) % (m-1) == 0 w/o padding
    # Let m = 3. m-1 = 2. We want n-1 to be even. n can be 5.
    n_bound1, m_bound1 = 5, 3
    freq_bound1 = [1, 2, 3, 4, 5]
    test_cases.append({
        "input": f"{n_bound1} {m_bound1}\n{' '.join(map(str, freq_bound1))}",
        "output": str(solve(n_bound1, m_bound1, list(freq_bound1))),
        "category": "boundary",
        "description": "Perfect fit, no padding needed"
    })
    
    # Boundary 2: Requires maximal padding (m-2 zeros)
    # Let m=5. m-1=4. We want (n-1)%4 != 0.
    # If n=2, rem=1, need 3 zeros.
    # If n=6, rem=1, need 3 zeros.
    n_bound2, m_bound2 = 6, 5
    freq_bound2 = [10] * 6
    test_cases.append({
        "input": f"{n_bound2} {m_bound2}\n{' '.join(map(str, freq_bound2))}",
        "output": str(solve(n_bound2, m_bound2, list(freq_bound2))),
        "category": "boundary",
        "description": "Requires padding of m-2 zeros"
    })

    # -------------------------------------------------------------------------
    # 4. HIDDEN: STRESS CASES
    # -------------------------------------------------------------------------
    
    # Stress 1: Large n, m=2 (Standard Huffman)
    n_stress1 = 1000
    m_stress1 = 2
    freq_stress1 = [random.randint(1, 1000) for _ in range(n_stress1)]
    test_cases.append({
        "input": f"{n_stress1} {m_stress1}\n{' '.join(map(str, freq_stress1))}",
        "output": str(solve(n_stress1, m_stress1, list(freq_stress1))),
        "category": "stress",
        "description": "Large n with m=2"
    })
    
    # Stress 2: Large n, m=5
    n_stress2 = 10000
    m_stress2 = 5
    freq_stress2 = [random.randint(1, 1000000) for _ in range(n_stress2)]
    test_cases.append({
        "input": f"{n_stress2} {m_stress2}\n{' '.join(map(str, freq_stress2))}",
        "output": str(solve(n_stress2, m_stress2, list(freq_stress2))),
        "category": "stress",
        "description": "Large n with m=5, large values"
    })
    
    # -------------------------------------------------------------------------
    # 5. HIDDEN: NORMAL CASES
    # -------------------------------------------------------------------------
    
    # Normal 1: Random small
    n_norm1 = 20
    m_norm1 = 3
    freq_norm1 = [random.randint(1, 100) for _ in range(n_norm1)]
    test_cases.append({
        "input": f"{n_norm1} {m_norm1}\n{' '.join(map(str, freq_norm1))}",
        "output": str(solve(n_norm1, m_norm1, list(freq_norm1))),
        "category": "normal",
        "description": "Random normal case"
    })

    return test_cases

def main():
    test_cases = generate_test_cases()
    
    yaml_output = {
        "problem_id": "HEP-008",
        "test_cases": test_cases
    }
    
    # Custom Dumper to enforce block scalars for input/output
    class BlockDumper(yaml.Dumper):
        def increase_indent(self, flow=False, indentless=False):
            return super(BlockDumper, self).increase_indent(flow, False)

    def str_presenter(dumper, data):
        if '\n' in data:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    yaml.add_representer(str, str_presenter, Dumper=BlockDumper)
    
    output_path = "HEP-008-huffman-merge-limit.yaml"
    with open(output_path, 'w') as f:
        yaml.dump(yaml_output, f, Dumper=BlockDumper, default_flow_style=False, sort_keys=False)
    
    print(f"Generated {len(test_cases)} test cases in {output_path}")

if __name__ == "__main__":
    main()
