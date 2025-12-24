import random
import yaml

def solve(k, operations):
    buffer = [0] * k
    head = 0
    tail = 0
    size = 0
    results = []
    
    for op_row in operations:
        op = op_row[0]
        if op == "ENQ":
            x = op_row[1]
            if size < k:
                buffer[tail] = x
                tail = (tail + 1) % k
                size += 1
                results.append("true")
            else:
                results.append("false")
        elif op == "ENQ_OVR":
            x = op_row[1]
            if size < k:
                buffer[tail] = x
                tail = (tail + 1) % k
                size += 1
                results.append("true")
            else:
                buffer[tail] = x
                tail = (tail + 1) % k
                head = (head + 1) % k
                results.append("overwritten")
        elif op == "DEQ":
            if size > 0:
                val = buffer[head]
                head = (head + 1) % k
                size -= 1
                results.append(str(val))
            else:
                results.append("EMPTY")
        elif op == "FRONT":
            if size > 0:
                results.append(str(buffer[head]))
            else:
                results.append("EMPTY")
        elif op == "REAR":
            if size > 0:
                results.append(str(buffer[(tail - 1 + k) % k]))
            else:
                results.append("EMPTY")
        elif op == "ISEMPTY":
            results.append("true" if size == 0 else "false")
        elif op == "ISFULL":
            results.append("true" if size == k else "false")
    return results

def make_test_case(k, operations):
    results = solve(k, operations)
    input_str = f"{k}\n{len(operations)}\n" + "\n".join(" ".join(map(str, op)) for op in operations)
    output_str = "\n".join(results)
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case(2, [
                ["ENQ", 5],
                ["ENQ", 6],
                ["ENQ", 7],
                ["ENQ_OVR", 8],
                ["FRONT"],
                ["REAR"]
            ])
        ],
        "public": [
            make_test_case(1, [["ENQ", 1], ["ENQ", 2], ["ENQ_OVR", 3], ["DEQ"]]),
            make_test_case(3, [["ISEMPTY"], ["ISFULL"], ["ENQ", 10], ["ISEMPTY"], ["ENQ", 20], ["ENQ", 30], ["ISFULL"]])
        ],
        "hidden": []
    }

    # Edge case: Capacity 1 overwriting
    tc["hidden"].append(make_test_case(1, [["ENQ_OVR", i] for i in range(10)] + [["FRONT"]]))
    
    # Large sequence: Fill and empty
    tc["hidden"].append(make_test_case(1000, [["ENQ", i] for i in range(1000)] + [["DEQ"] * 1000]))

    # Stress case
    k_stress = random.randint(1000, 100000)
    m_stress = 100000
    stress_ops = []
    for _ in range(m_stress):
        r = random.random()
        if r < 0.3:
            stress_ops.append(["ENQ", random.randint(-10**9, 10**9)])
        elif r < 0.6:
            stress_ops.append(["ENQ_OVR", random.randint(-10**9, 10**9)])
        elif r < 0.75:
            stress_ops.append(["DEQ"])
        elif r < 0.85:
            stress_ops.append(["FRONT"])
        elif r < 0.95:
            stress_ops.append(["REAR"])
        else:
            stress_ops.append(["ISEMPTY" if random.random() < 0.5 else "ISFULL"])
    tc["hidden"].append(make_test_case(k_stress, stress_ops))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
