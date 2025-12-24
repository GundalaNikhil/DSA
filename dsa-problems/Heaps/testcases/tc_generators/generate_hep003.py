
import sys
import random
import math

# --- Reference Solution ---
def solve(q, d, k, ops):
    # state: key -> (count, last_update_t)
    state = {}
    outputs = []
    
    current_time = 0
    EPS = 1e-9

    for op in ops:
        type = op[0]
        if type == "ADD":
            key = op[1]
            t = int(op[2])
            current_time = t
            
            if key in state:
                cnt, last_t = state[key]
                # Decay
                steps = (t - last_t) // d
                # Optimization: if steps is large, count becomes 0
                if steps > 60: # 2^60 is huge, count becomes 0 unless count was > 2^60
                     # Initial count usually small (number of adds). 
                     # If q=10^5, max count = 10^5.
                     # 10^5 / 2^20 < 1. 2^60 clears it for sure.
                     val = 0.0
                else:
                     val = cnt * (0.5 ** steps)
                
                # Add 1
                state[key] = (val + 1.0, t)
            else:
                state[key] = (1.0, t)
                
        elif type == "QUERY":
            t = int(op[1])
            current_time = t
            
            # Collect effective counts
            valid_keys = []
            keys_to_remove = []
            
            unique_keys = sorted(state.keys()) # sort for stability if needed, but we sort later
            
            for key in unique_keys:
                cnt, last_t = state[key]
                steps = (t - last_t) // d
                if steps > 60:
                    val = 0.0
                else:
                    val = cnt * (0.5 ** steps)
                
                # Check existance criteria
                # "If no keys exist" implies count > 0?
                # Usually yes. If value effectively 0 (e.g. < 1e-9), maybe considered gone?
                # Problem doesn't say "remove if 0". But decayed infinitely is just small positive.
                # However, if it's 1e-300, it's effectively 0.
                # Let's include everything with > 0.
                if val > 1e-12: # Threshold
                    valid_keys.append((-val, key))
                else:
                    # Optional: clean up very small keys to save memory?
                    # For correctness we keep if strictly > 0 via float logic but logic says 
                    # standard limit usually applies.
                    # Given example, exact values matter?
                    # "1.5 -> 0.75"
                    valid_keys.append((-val, key))
            
            if not valid_keys:
                outputs.append("EMPTY")
            else:
                # Sort: desc count, asc key
                valid_keys.sort()
                
                result_keys = []
                take = min(k, len(valid_keys))
                for i in range(take):
                   result_keys.append(valid_keys[i][1])
                
                outputs.append(" ".join(result_keys))
                
    return outputs

# --- Test Case Generators ---

def generate_sample_1():
    q, d, k = 4, 5, 1
    ops = [
        ["ADD", "a", "0"],
        ["ADD", "a", "5"],
        ["ADD", "b", "5"],
        ["QUERY", "10"]
    ]
    return q, d, k, ops

def generate_random_ops(q, d, k, num_keys, max_time):
    ops = []
    keys = [f"k{i}" for i in range(num_keys)]
    
    # Generate sorted timestamps
    timestamps = sorted([random.randint(0, max_time) for _ in range(q)])
    
    for i in range(q):
        t = timestamps[i]
        is_query = random.random() < 0.3
        
        if is_query:
            ops.append(["QUERY", str(t)])
        else:
            key = random.choice(keys)
            ops.append(["ADD", key, str(t)])
            
    return q, d, k, ops

# --- YAML Builder ---

def format_input(q, d, k, ops):
    lines = [f"{q} {d} {k}"]
    for op in ops:
        if op[0] == "ADD":
            lines.append(f"{op[0]} {op[1]} {op[2]}")
        else:
            lines.append(f"{op[0]} {op[1]}")
    return "\n".join(lines)

def format_output(outputs):
    return "\n".join(outputs)

def make_test_case(q, d, k, ops):
    input_str = format_input(q, d, k, ops)
    output_list = solve(q, d, k, ops)
    output_str = format_output(output_list)
    return input_str, output_str


def main():
    test_cases = {
        "problem_id": "HEP_TOP_K_FREQUENT_DECAY__5829",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    sq, sd, sk, sops = generate_sample_1()
    si, so = make_test_case(sq, sd, sk, sops)
    test_cases["samples"].append({"input": si, "output": so})
    
    # Sample 2: Tie breaking
    # a: 1 at 0 -> 1 at 10 (d=100 so Factor=1)
    # b: 1 at 0 -> ...
    # k=2
    s2ops = [
        ["ADD", "b", "0"],
        ["ADD", "a", "0"],
        ["QUERY", "1"]
    ]
    s2i, s2o = make_test_case(3, 100, 2, s2ops)
    test_cases["samples"].append({"input": s2i, "output": s2o})

    # Public
    # Edge: Empty
    pq1, pd1, pk1 = 1, 1, 1
    p1ops = [["QUERY", "0"]]
    pi1, po1 = make_test_case(pq1, pd1, pk1, p1ops)
    test_cases["public"].append({"input": pi1, "output": po1}) # EMPTY
    
    # Edge: Decay to near zero
    pq2, pd2, pk2 = 3, 1, 1
    p2ops = [["ADD", "a", "0"], ["QUERY", "100"]] # large time gap
    pi2, po2 = make_test_case(pq2, pd2, pk2, p2ops)
    test_cases["public"].append({"input": pi2, "output": po2}) # "a" still exists? Yes.

    # Basic: Simple sorting
    pq3, pd3, pk3 = 5, 10, 3
    p3ops = [["ADD", "c", "0"], ["ADD", "b", "0"], ["ADD", "a", "0"], ["QUERY", "0"]]
    pi3, po3 = make_test_case(pq3, pd3, pk3, p3ops)
    test_cases["public"].append({"input": pi3, "output": po3}) # a b c

    # Hidden
    hidden_cases = []
    
    # 1. Edge: d is large (no decay)
    _, _, _, h1ops = generate_random_ops(20, 10000, 5, 5, 100)
    hidden_cases.append(make_test_case(20, 10000, 5, h1ops))
    
    # 2. Edge: d=1 (fast decay)
    _, _, _, h2ops = generate_random_ops(20, 1, 2, 5, 20) # timestamps up to 20
    hidden_cases.append(make_test_case(20, 1, 2, h2ops))
    
    # 3. Edge: k=1
    _, _, _, h3ops = generate_random_ops(15, 5, 1, 3, 50)
    hidden_cases.append(make_test_case(15, 5, 1, h3ops))

    # 4. Stress: All ADDs
    h4ops = [["ADD", str(i), str(i)] for i in range(10)] + [["QUERY", "100"]]
    hidden_cases.append(make_test_case(11, 5, 5, h4ops))
    
    # 5. Negative: No keys for query
    h5ops = [["QUERY", "10"], ["QUERY", "20"]]
    hidden_cases.append(make_test_case(2, 5, 5, h5ops))

    # 6. Special: Identical counts, lex tiebreak
    h6ops = [["ADD", "ba", "0"], ["ADD", "ab", "0"], ["QUERY", "1"]]
    hidden_cases.append(make_test_case(3, 10, 2, h6ops)) # ab, ba
    
    # 7. Normal: Random Small
    hq, hd, hk, hps = generate_random_ops(50, 5, 3, 10, 100)
    hidden_cases.append(make_test_case(50, 5, 3, hps))
    
    # 8. Normal: Random Medium (careful with simulation speed)
    hq8, hd8, hk8, hps8 = generate_random_ops(200, 10, 5, 20, 500)
    hidden_cases.append(make_test_case(200, 10, 5, hps8))
    
    # 9. Normal: Large time gap
    h9ops = [["ADD", "a", "0"], ["ADD", "b", "0"], ["QUERY", "1000"]] # d=10
    hidden_cases.append(make_test_case(3, 10, 2, h9ops))
    
    # 10. Boundary: Updates align with decay period exactly
    # d=5. t=0, 5, 10
    h10ops = [["ADD", "a", "0"], ["ADD", "a", "5"], ["ADD", "a", "10"], ["QUERY", "15"]]
    hidden_cases.append(make_test_case(4, 5, 1, h10ops)) 
    
    # 11. Stress: Many keys
    hq11 = 500
    hps11_ops = []
    for i in range(hq11 - 1):
        hps11_ops.append(["ADD", f"k{i}", "0"])
    hps11_ops.append(["QUERY", "10"])
    hidden_cases.append(make_test_case(hq11, 100, 10, hps11_ops))
    
    # 12. Stress: Max k (return all)
    hps12_ops = [["ADD", "a", "0"], ["ADD", "b", "0"], ["QUERY", "1"]]
    hidden_cases.append(make_test_case(3, 10, 1000, hps12_ops))

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
    if not c["output"]:
        print("      ")
    for line in c["output"].split("\n"):
        if line:
            print(f"      {line}")

if __name__ == "__main__":
    main()
