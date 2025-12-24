from collections import deque
import random
import yaml

def solve(s):
    counts = {}
    queue = deque()
    results = []
    
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        queue.append(char)
        
        while queue and counts[queue[0]] > 1:
            queue.popleft()
            
        if queue:
            results.append(queue[0])
        else:
            results.append("#")
    return results

def make_test_case(s):
    res = solve(s)
    input_str = f"{s}"
    output_str = " ".join(res)
    return {"input": input_str, "output": output_str}

def generate_yaml():
    tc = {
        "samples": [
            make_test_case("abacb")
        ],
        "public": [
            make_test_case("a"),
            make_test_case("aaaaa"),
            make_test_case("abcdef")
        ],
        "hidden": []
    }

    # Edge cases: All same, All different
    tc["hidden"].append(make_test_case("z" * 100))
    tc["hidden"].append(make_test_case("qwertyuiopasdfghjklzxcvbnm"))
    
    # Large sequence
    large_s = "abcdefghijklmnopqrstuvwxyz" * 3000
    tc["hidden"].append(make_test_case(large_s))

    # Random case
    letters = "abcdefghijklmnopqrstuvwxyz"
    rand_s = "".join(random.choice(letters) for _ in range(1000))
    tc["hidden"].append(make_test_case(rand_s))

    # Large random case
    large_rand_s = "".join(random.choice(letters) for _ in range(100000))
    tc["hidden"].append(make_test_case(large_rand_s))

    print(yaml.dump(tc, sort_keys=False, default_flow_style=False))

if __name__ == "__main__":
    generate_yaml()
