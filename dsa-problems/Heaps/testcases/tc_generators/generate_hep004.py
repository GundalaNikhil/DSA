
import sys
import random

# --- Reference Solution ---
def solve(n, strengths, priority):
    total_strength = sum(strengths)
    
    has_1 = False
    has_2 = False
    has_3 = False
    
    count = 0
    for p in priority:
        if p == 1: has_1 = True
        elif p == 2: has_2 = True
        elif p == 3: has_3 = True
        count += 1
        
    if count <= 1:
        return total_strength
        
    penalty = 0
    
    # We essentially coalesce all same classes for free.
    # Then we merge the Super Ropes.
    
    present = []
    if has_1: present.append(1)
    if has_2: present.append(2)
    if has_3: present.append(3)
    
    if len(present) == 1:
        penalty = 0
    elif len(present) == 2:
        if 1 in present and 2 in present:
            penalty = 1
        elif 2 in present and 3 in present:
            penalty = 1
        elif 1 in present and 3 in present:
            penalty = 2
    elif len(present) == 3:
        # Merge 2 and 3 -> 2 (cost 1). Then 1 and 2 -> 1 (cost 1). Total 2.
        penalty = 2
        
    return total_strength - penalty

# --- Test Case Generators ---

def generate_sample_1():
    n = 3
    s = [6, 5, 4]
    p = [1, 2, 3]
    return n, s, p

def generate_random(n, min_val, max_val):
    s = [random.randint(min_val, max_val) for _ in range(n)]
    p = [random.choice([1, 2, 3]) for _ in range(n)]
    return n, s, p

# --- YAML Builder ---

def format_input(n, s, p):
    lines = []
    lines.append(str(n))
    lines.append(" ".join(map(str, s)))
    lines.append(" ".join(map(str, p)))
    return "\n".join(lines)

def format_output(val):
    return str(val)

def make_test_case(n, s, p):
    input_str = format_input(n, s, p)
    output_val = solve(n, s, p)
    output_str = format_output(output_val)
    return input_str, output_str


def main():
    test_cases = {
        "problem_id": "HEP_ROPE_CONNECT_MAXIMIZE_PRIORITY__6742",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    sn, ss, sp = generate_sample_1()
    si, so = make_test_case(sn, ss, sp)
    test_cases["samples"].append({"input": si, "output": so})
    
    # Sample 2: Same class
    s2n = 3
    s2s = [10, 20, 30]
    s2p = [2, 2, 2]
    s2i, s2o = make_test_case(s2n, s2s, s2p)
    test_cases["samples"].append({"input": s2i, "output": s2o})

    # Public
    # Edge: n=1
    p1n = 1
    p1s = [100]
    p1p = [1]
    pi1, po1 = make_test_case(p1n, p1s, p1p)
    test_cases["public"].append({"input": pi1, "output": po1})
    
    # Edge: Two classes {1, 3} (max penalty merge)
    p2n = 2
    p2s = [10, 10]
    p2p = [1, 3]
    pi2, po2 = make_test_case(p2n, p2s, p2p)
    test_cases["public"].append({"input": pi2, "output": po2}) # 20 - 2 = 18

    # Basic: {1, 2}
    p3n = 2
    p3s = [5, 5]
    p3p = [1, 2]
    pi3, po3 = make_test_case(p3n, p3s, p3p)
    test_cases["public"].append({"input": pi3, "output": po3}) # 10 - 1 = 9
    
    # Basic: {2, 3}
    p4n = 2
    p4s = [5, 5]
    p4p = [2, 3]
    pi4, po4 = make_test_case(p4n, p4s, p4p)
    test_cases["public"].append({"input": pi4, "output": po4})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: All 1s
    _, h1s, h1p = generate_random(10, 1, 100)
    h1p = [1]*10
    hidden_cases.append(make_test_case(10, h1s, h1p))
    
    # 2. Edge: All 2s
    _, h2s, h2p = generate_random(10, 1, 100)
    h2p = [2]*10
    hidden_cases.append(make_test_case(10, h2s, h2p))
    
    # 3. Edge: All 3s
    hidden_cases.append(make_test_case(10, h2s, [3]*10))

    # 4. Stress: Max N, random classes
    h4n = 1000
    _, h4s, h4p = generate_random(h4n, 1000, 1000000)
    hidden_cases.append(make_test_case(h4n, h4s, h4p))
    
    # 5. Negative/Edge: n=1 with class 3
    hidden_cases.append(make_test_case(1, [50], [3]))

    # 6. Special: 1 and 3 many times
    h6p = [1]*5 + [3]*5
    hidden_cases.append(make_test_case(10, [10]*10, h6p))
    
    # 7. Special: 2 and 3 many times
    h7p = [2]*5 + [3]*5
    hidden_cases.append(make_test_case(10, [10]*10, h7p))
    
    # 8. Normal: Random Small
    _, h8s, h8p = generate_random(50, 1, 100)
    hidden_cases.append(make_test_case(50, h8s, h8p))
    
    # 9. Normal: Random Medium
    _, h9s, h9p = generate_random(200, 1, 100)
    hidden_cases.append(make_test_case(200, h9s, h9p))
    
    # 10. Large Values
    h10s = [1000000000] * 5
    h10p = [1, 2, 3, 1, 2]
    hidden_cases.append(make_test_case(5, h10s, h10p))

    # Add to structure
    for inp, out in hidden_cases:
        test_cases["hidden"].append({"input": inp, "output": out})

    # Output YAML
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

def print_case(c):
    print("  - input: |-")
    for line in c["input"].split("\n"):
        print(f"      {line}")
    print("    output: |-")
    print(f"      {c['output']}")

if __name__ == "__main__":
    main()
