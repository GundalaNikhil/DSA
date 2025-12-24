import random
import yaml

def solve(commands):
    queue = []
    front_idx = 0
    results = []
    for cmd in commands:
        if cmd[0] == "ENQUEUE":
            queue.append(cmd[1])
        elif cmd[0] == "DEQUEUE":
            if front_idx < len(queue):
                results.append(str(queue[front_idx]))
                front_idx += 1
            else:
                results.append("EMPTY")
        elif cmd[0] == "FRONT":
            if front_idx < len(queue):
                results.append(str(queue[front_idx]))
            else:
                results.append("EMPTY")
    return results

def make_test_case(commands):
    results = solve(commands)
    input_str = f"{len(commands)}\n" + "\n".join(" ".join(map(str, cmd)) for cmd in commands)
    output_str = "\n".join(results)
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case([
                ["ENQUEUE", 12],
                ["ENQUEUE", -5],
                ["FRONT"],
                ["DEQUEUE"],
                ["FRONT"],
                ["DEQUEUE"]
            ])
        ],
        "public": [
            make_test_case([["DEQUEUE"], ["FRONT"]]),
            make_test_case([["ENQUEUE", 100], ["DEQUEUE"], ["DEQUEUE"]]),
            make_test_case([["ENQUEUE", i] for i in range(5)] + [["FRONT"], ["DEQUEUE"]] * 5)
        ],
        "hidden": []
    }

    # Edge cases: Empty dequeue
    tc["hidden"].append(make_test_case([["DEQUEUE"] * 10]))
    
    # Large sequence
    large_cmds = []
    for i in range(1000):
        large_cmds.append(["ENQUEUE", i])
    for i in range(1000):
        large_cmds.append(["DEQUEUE"])
    tc["hidden"].append(make_test_case(large_cmds))

    # Stress case
    stress_cmds = []
    for i in range(100000):
        r = random.random()
        if r < 0.6:
            stress_cmds.append(["ENQUEUE", random.randint(-10**9, 10**9)])
        elif r < 0.8:
            stress_cmds.append(["DEQUEUE"])
        else:
            stress_cmds.append(["FRONT"])
    tc["hidden"].append(make_test_case(stress_cmds))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
