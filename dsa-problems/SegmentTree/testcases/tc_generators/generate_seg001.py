import random
import yaml

def solve(n, q, m, a, queries):
    bit = [0] * (n + 1)
    def add(idx, val):
        idx += 1
        while idx <= n:
            bit[idx] = (bit[idx] + val) % m
            idx += idx & (-idx)
            
    def query(idx):
        idx += 1
        s = 0
        while idx > 0:
            s = (s + bit[idx]) % m
            idx -= idx & (-idx)
        return s

    for i, x in enumerate(a):
        add(i, x % m)
        
    curr_a = [x % m for x in a]
    history = []
    results = []
    
    for op in queries:
        if op[0] == "UPDATE":
            idx, val = op[1], op[2]
            val %= m
            old_val = curr_a[idx]
            history.append((idx, old_val))
            diff = (val - old_val) % m
            add(idx, diff)
            curr_a[idx] = val
        elif op[0] == "QUERY":
            l, r = op[1], op[2]
            res = (query(r) - query(l - 1)) % m
            results.append(str(res))
        elif op[0] == "UNDO":
            k = op[1]
            while k > 0 and history:
                idx, old_val = history.pop()
                curr_val = curr_a[idx]
                diff = (old_val - curr_val) % m
                add(idx, diff)
                curr_a[idx] = old_val
                k -= 1
    return results

def make_test_case(n, q, m, a, queries):
    input_str = f"{n} {q} {m}\n"
    input_str += " ".join(map(str, a)) + "\n"
    for op in queries:
        input_str += " ".join(map(str, op)) + "\n"
    output_str = "\n".join(solve(n, q, m, a, queries))
    return input_str, output_str

def generate_queries(n, q, prob_update=0.4, prob_query=0.4, max_k=100):
    queries = []
    num_updates = 0
    for _ in range(q):
        r = random.random()
        if r < prob_update:
            idx = random.randint(0, n - 1)
            val = random.randint(-10**9, 10**9)
            queries.append(["UPDATE", idx, val])
            num_updates += 1
        elif r < prob_update + prob_query:
            l = random.randint(0, n - 1)
            r2 = random.randint(l, n - 1)
            queries.append(["QUERY", l, r2])
        else:
            k = random.randint(0, min(max_k, num_updates))
            queries.append(["UNDO", k])
            num_updates -= k
            if num_updates < 0: num_updates = 0
    return queries

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, q, m = 5, 5, 1000
    a = [1, 2, 3, 4, 5]
    queries = [
        ["QUERY", 1, 3],
        ["UPDATE", 2, 10],
        ["QUERY", 0, 4],
        ["UNDO", 1],
        ["QUERY", 0, 4]
    ]
    input_str, output_str = make_test_case(n, q, m, a, queries)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # 1. All Queries
    n, q, m = 10, 5, 10**9 + 7
    a = [i for i in range(n)]
    queries = [["QUERY", 0, n - 1] for _ in range(q)]
    input_str, output_str = make_test_case(n, q, m, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # 2. All Updates then Undo
    n, q, m = 10, 10, 100
    a = [0] * n
    queries = [["UPDATE", i, i + 1] for i in range(5)]
    queries += [["UNDO", 5]]
    queries += [["QUERY", 0, n - 1] for _ in range(4)]
    input_str, output_str = make_test_case(n, q, m, a, queries)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    # 1. n=1, q=1
    test_cases["hidden"].append({"input": f"1 1 10\n5\nQUERY 0 0\n", "output": "5", "category": "edge"})
    
    # 2. UNDO 0
    n, q, m = 5, 3, 100
    a = [1] * 5
    queries = [["UPDATE", 0, 10], ["UNDO", 0], ["QUERY", 0, 0]]
    input_str, output_str = make_test_case(n, q, m, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "edge"})

    # 3. UNDO more than updates
    n, q, m = 5, 3, 100
    a = [1] * 5
    queries = [["UPDATE", 0, 10], ["UNDO", 100], ["QUERY", 0, 0]]
    input_str, output_str = make_test_case(n, q, m, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "edge"})

    # Stress Cases
    # 1. Max N, Q
    n, q, m = 200000, 200000, 10**9 + 7
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = generate_queries(n, q, prob_update=0.45, prob_query=0.45, max_k=100)
    input_str, output_str = make_test_case(n, q, m, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    # 2. Heavy UNDO
    n, q, m = 200000, 200000, 999999937
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    queries = generate_queries(n, q, prob_update=0.4, prob_query=0.2, max_k=100)
    input_str, output_str = make_test_case(n, q, m, a, queries)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-001-range-sum-point-updates-undo.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
