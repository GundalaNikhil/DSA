#!/usr/bin/env python3
"""
Test case generator for HEP-009: Dynamic Median of Medians
Generates 30 hidden test cases focusing on basic, edge, and corner scenarios.
"""

import yaml
import random
import bisect

def get_median(arr):
    if not arr: return None
    n = len(arr)
    # Lower median for even size: index (n-1)//2
    return sorted(arr)[(n - 1) // 2]

def solve_naive(operations):
    groups = {}
    results = []
    
    for op in operations:
        if op[0] == "NEW":
            gid = op[1]
            vals = list(map(int, op[3:]))
            groups[gid] = sorted(vals)
        elif op[0] == "ADD":
            gid = op[1]
            x = int(op[2])
            if gid in groups:
                bisect.insort(groups[gid], x)
        elif op[0] == "MERGE":
            gid1, gid2 = op[1], op[2]
            if gid1 in groups and gid2 in groups:
                # Merge gid2 into gid1
                new_arr = sorted(groups[gid1] + groups[gid2])
                groups[gid1] = new_arr
                del groups[gid2]
        elif op[0] == "QUERY":
            medians = []
            for gid in sorted(groups.keys()):
                m = get_median(groups[gid])
                if m is not None:
                    medians.append(m)
            if not medians:
                results.append("EMPTY")
            else:
                results.append(str(get_median(medians)))
    return results

def generate_test_cases():
    random.seed(42)
    test_cases = {
        'problem_id': 'HEP_DYNAMIC_MEDIAN_OF_MEDIANS__7312',
        'samples': [],
        'public': [],
        'hidden': []
    }
    
    # Sample from problem
    sample_ops = [["NEW", "1", "1", "3"], ["NEW", "2", "2"], ["MERGE", "1", "2"], ["QUERY"]]
    # Wait, the sample in my previous file was different. Let's use the one from problem description if I had it.
    # Looking at my previous tool output: "NEW 1 2\n1 3\nNEW 2 1\n2\nMERGE 1 2\nQUERY" -> "2"
    sample_ops = [["NEW", "1", "1", "3"], ["NEW", "2", "2"], ["MERGE", "1", "2"], ["QUERY"]]
    # Actually let's just use the one that works.
    test_cases['samples'].append({
        'input': "4\nNEW 1 2\n1 3\nNEW 2 1\n2\nMERGE 1 2\nQUERY",
        'output': "2"
    })
    
    # Public (Simple)
    test_cases['public'].extend([
        {'input': "2\nNEW 1 1\n5\nQUERY", 'output': "5"},
        {'input': "3\nNEW 1 1\n10\nNEW 2 1\n20\nQUERY", 'output': "10"},
        {'input': "1\nQUERY", 'output': "EMPTY"},
    ])
    
    # Hidden (30 cases)
    for i in range(30):
        ops = []
        if i < 5: # Basic sequences
            n_groups = random.randint(1, 3)
            for g in range(n_groups):
                m = random.randint(1, 3)
                vals = [str(random.randint(1, 10)) for _ in range(m)]
                ops.append(["NEW", str(g), str(m)] + vals)
            ops.append(["QUERY"])
        elif i < 15: # Mixed ADD and QUERY
            n_groups = random.randint(2, 5)
            for g in range(n_groups):
                ops.append(["NEW", str(g), "1", str(random.randint(1, 20))])
            for _ in range(10):
                choice = random.random()
                if choice < 0.6:
                    ops.append(["ADD", str(random.randint(0, n_groups-1)), str(random.randint(1, 50))])
                else:
                    ops.append(["QUERY"])
        elif i < 25: # MERGE heavy
            n_groups = 10
            for g in range(n_groups):
                ops.append(["NEW", str(g), "1", str(random.randint(1, 100))])
            active_groups = list(range(n_groups))
            for _ in range(15):
                choice = random.random()
                if choice < 0.5 and len(active_groups) >= 2:
                    idx2 = random.randint(0, len(active_groups)-1)
                    g2 = active_groups.pop(idx2)
                    idx1 = random.randint(0, len(active_groups)-1)
                    g1 = active_groups[idx1]
                    ops.append(["MERGE", str(g1), str(g2)])
                elif choice < 0.8:
                    if active_groups:
                        ops.append(["ADD", str(random.choice(active_groups)), str(random.randint(1, 100))])
                else:
                    ops.append(["QUERY"])
        else: # Edge cases: empty groups, large numbers
            ops.append(["NEW", "1", "0"]) # Empty group
            ops.append(["QUERY"])
            ops.append(["ADD", "1", "1000000"])
            ops.append(["QUERY"])
            ops.append(["NEW", "2", "3", "10", "15", "20"]) # Duplicates
            ops.append(["QUERY"])

        q = len(ops)
        inp_lines = [str(q)]
        for op in ops:
            if op[0] == "NEW":
                gid, m = op[1], int(op[2])
                vals = op[3:]
                inp_lines.append(f"NEW {gid} {m}")
                if vals:
                    inp_lines.append(" ".join(vals))
            elif op[0] == "ADD":
                inp_lines.append(f"ADD {op[1]} {op[2]}")
            elif op[0] == "MERGE":
                inp_lines.append(f"MERGE {op[1]} {op[2]}")
            else:
                inp_lines.append("QUERY")
        
        result = solve_naive(ops)
        test_cases['hidden'].append({
            'input': "\n".join(inp_lines),
            'output': "\n".join(result)
        })
    
    return test_cases

def main():
    test_cases = generate_test_cases()
    output_path = '/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Heaps/testcases/HEP-009-dynamic-median-of-medians.yaml'
    
    with open(output_path, 'w') as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"✅ Generated {len(test_cases['samples'])} samples, {len(test_cases['public'])} public, {len(test_cases['hidden'])} hidden test cases for HEP-009")

if __name__ == '__main__':
    main()
