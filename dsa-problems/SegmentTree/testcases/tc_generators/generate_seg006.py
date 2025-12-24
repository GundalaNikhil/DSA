import random
import yaml
import bisect

def solve(n, q, a, queries):
    # Square Root Decomposition for reference
    block_size = int(n**0.5) + 1
    blocks = []
    for i in range(0, n, block_size):
        chunk = a[i : i + block_size]
        blocks.append(sorted(chunk))
        
    curr_a = list(a)
    results = []
    
    for op in queries:
        if op[0] == "SET":
            idx = int(op[1])
            new_val = int(op[2])
            old_val = curr_a[idx]
            
            b_idx = idx // block_size
            # Update curr_a
            curr_a[idx] = new_val
            # Update sorted block
            # list.remove is O(blockSize), bisect.insort is O(blockSize)
            blocks[b_idx].remove(old_val)
            bisect.insort(blocks[b_idx], new_val)
            
        elif op[0] == "COUNT":
            l, r, x, y = map(int, op[1:])
            count = 0
            
            bl = l // block_size
            br = r // block_size
            
            if bl == br:
                for i in range(l, r + 1):
                    if x <= curr_a[i] <= y:
                        count += 1
            else:
                # Left partial block
                for i in range(l, (bl + 1) * block_size):
                    if x <= curr_a[i] <= y:
                        count += 1
                # Full blocks
                for b_idx in range(bl + 1, br):
                    b = blocks[b_idx]
                    # count elements in [x, y] in sorted b
                    # num <= y minus num < x
                    it1 = bisect.bisect_right(b, y)
                    it2 = bisect.bisect_left(b, x)
                    count += (it1 - it2)
                # Right partial block
                for i in range(br * block_size, r + 1):
                    if x <= curr_a[i] <= y:
                        count += 1
            results.append(str(count))
            
    return results

def make_test_case(n, q, a, queries):
    input_str = f"{n} {q}\n"
    input_str += " ".join(map(str, a)) + "\n"
    for op in queries:
        input_str += " ".join(map(str, op)) + "\n"
    output_str = "\n".join(solve(n, q, a, queries))
    return input_str, output_str

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, q = 3, 1
    a = [1, 5, 2]
    queries = [["COUNT", 0, 2, 2, 5]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # 1. Updates and Queries
    n, q = 5, 3
    a = [1, 2, 3, 4, 5]
    queries = [["SET", 2, 10], ["COUNT", 0, 4, 3, 10], ["COUNT", 2, 2, 10, 10]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    # 1. n=1
    test_cases["hidden"].append({"input": f"1 1\n5\nCOUNT 0 0 5 5\n", "output": "1", "category": "edge"})
    
    # 2. x > y
    n, q = 5, 1
    a = [1, 2, 3, 4, 5]
    queries = [["COUNT", 0, 4, 10, 5]]
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "edge"})

    # Stress Cases
    # 1. Medium N, Q for Python generator
    n, q = 5000, 5000
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = []
    for _ in range(q):
        if random.random() < 0.3:
            queries.append(["SET", random.randint(0, n-1), random.randint(-10**9, 10**9)])
        else:
            l = random.randint(0, n-1)
            r = random.randint(l, n-1)
            x = random.randint(-10**9, 10**9)
            y = random.randint(x, 10**9)
            queries.append(["COUNT", l, r, x, y])
    input_str, output_str = make_test_case(n, q, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-006-count-values-in-range.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
