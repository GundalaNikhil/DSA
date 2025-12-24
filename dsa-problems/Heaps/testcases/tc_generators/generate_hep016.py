
import sys
import random
import heapq

# --- Reference Solution ---

def solve(q, operations):
    # Min Heap: (value, id)
    pq = []
    # Map: id -> current_value
    # Used to validate heap entries (lazy deletion)
    current_values = {}
    
    results = []
    
    for op_parts in operations:
        op = op_parts[0]
        
        if op == "INSERT":
            tid = op_parts[1]
            val = int(op_parts[2])
            current_values[tid] = val
            heapq.heappush(pq, (val, tid))
            
        elif op == "DECREASE":
            tid = op_parts[1]
            delta = int(op_parts[2])
            # Assume valid id in current_values per problem constraints context
            if tid in current_values:
                new_val = current_values[tid] - delta
                current_values[tid] = new_val
                heapq.heappush(pq, (new_val, tid))
            
        elif op == "EXTRACT":
            found = False
            while pq:
                val, tid = heapq.heappop(pq)
                # Check if this heap entry matches current state
                if tid in current_values and current_values[tid] == val:
                    # Valid
                    results.append(f"{val} {tid}")
                    del current_values[tid]
                    found = True
                    break
                # Else: it's a stale entry (old value), discard.
            
            if not found:
                results.append("EMPTY")
                
    return results

# --- Test Case Generators ---

def make_test_case(q, operations):
    lines = [str(q)]
    for op in operations:
        lines.append(" ".join(map(str, op)))
    input_str = "\n".join(lines)
    
    res = solve(q, operations)
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
        "problem_id": "HEP_PRIORITY_QUEUE_DECREASE_KEY__8091",
        "samples": [],
        "public": [],
        "hidden": []
    }
    
    # Samples
    # 1. Example
    s1_ops = [
        ["INSERT", "id1", "5"],
        ["INSERT", "id2", "3"],
        ["DECREASE", "id1", "4"], # id1 -> 1
        ["EXTRACT"], # id1 (1)
        ["EXTRACT"]  # id2 (3)
    ]
    si1, so1 = make_test_case(5, s1_ops)
    test_cases["samples"].append({"input": si1, "output": so1})
    
    # Public
    # 1. Tie Breaking
    p1_ops = [
        ["INSERT", "B", "10"],
        ["INSERT", "A", "10"],
        ["EXTRACT"], # A 10
        ["EXTRACT"]  # B 10
    ]
    pi1, po1 = make_test_case(4, p1_ops)
    test_cases["public"].append({"input": pi1, "output": po1})
    
    # 2. Frequent Updates
    p2_ops = [
        ["INSERT", "A", "100"],
        ["DECREASE", "A", "10"], # 90
        ["DECREASE", "A", "10"], # 80
        ["EXTRACT"] # A 80
    ]
    pi2, po2 = make_test_case(4, p2_ops)
    test_cases["public"].append({"input": pi2, "output": po2})
    
    # Hidden
    hidden = []
    
    # 1. Empty Extract
    h1_ops = [["EXTRACT"]]
    hidden.append(make_test_case(1, h1_ops))
    
    # 2. Insert then Extract all
    h2_ops = [
        ["INSERT", "X", "10"],
        ["EXTRACT"],
        ["EXTRACT"]
    ]
    hidden.append(make_test_case(3, h2_ops))
    
    # 3. Multiple Decreases and Tie Break
    h3_ops = [
        ["INSERT", "C", "50"],
        ["INSERT", "B", "50"],
        ["INSERT", "A", "50"],
        ["DECREASE", "C", "10"], # C=40
        ["DECREASE", "B", "20"], # B=30
        ["EXTRACT"], # B 30
        ["EXTRACT"], # C 40
        ["EXTRACT"] # A 50
    ]
    hidden.append(make_test_case(8, h3_ops))
    
    # 4. Stress: Many Inserts
    h4_ops = []
    for i in range(100):
        h4_ops.append(["INSERT", f"id{i}", str(random.randint(1000, 2000))])
    for _ in range(100):
        h4_ops.append(["EXTRACT"])
    hidden.append(make_test_case(200, h4_ops))
    
    # 5. Stress: DECREASE dominated
    h5_ops = [["INSERT", "Target", "1000000"]]
    for _ in range(500):
        h5_ops.append(["DECREASE", "Target", "1"])
    h5_ops.append(["EXTRACT"])
    hidden.append(make_test_case(502, h5_ops))

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
