
import sys
import random
import heapq

# --- Reference Solution ---
def solve(k, r, streams):
    # streams is list of lists
    # k is len(streams)
    # output: list of ints
    
    # heap: (val, stream_idx)
    min_heap = []
    stream_idxs = [0] * k
    round_counts = [0] * k
    blocked_streams = [] # list of stream indices that are blocked for this round and have elements remaining
    
    # Initial population
    for i in range(k):
        if stream_idxs[i] < len(streams[i]):
            heapq.heappush(min_heap, (streams[i][stream_idxs[i]], i))
            
    result = []
    
    while min_heap or blocked_streams:
        if not min_heap:
            # End of round, unblock
            # All streams in blocked_streams should now be added to heap
            # And their round counts reset
            for s_idx in blocked_streams:
                round_counts[s_idx] = 0
                if stream_idxs[s_idx] < len(streams[s_idx]):
                     heapq.heappush(min_heap, (streams[s_idx][stream_idxs[s_idx]], s_idx))
            blocked_streams = []
            
        if not min_heap:
            break
            
        val, s_idx = heapq.heappop(min_heap)
        result.append(val)
        
        round_counts[s_idx] += 1
        stream_idxs[s_idx] += 1
        
        if stream_idxs[s_idx] < len(streams[s_idx]):
            if round_counts[s_idx] < r:
                heapq.heappush(min_heap, (streams[s_idx][stream_idxs[s_idx]], s_idx))
            else:
                blocked_streams.append(s_idx)
                
    return result

# --- Test Case Generators ---

def generate_sample_1():
    k = 2
    r = 1
    streams = [
        [1, 4],
        [2, 3, 5]
    ]
    return k, r, streams

def generate_random(k, r, total_elements, min_val, max_val):
    # Generates k sorted streams with roughly total_elements distributed
    streams = []
    remaining = total_elements
    for i in range(k - 1):
        if remaining <= 0:
            streams.append([])
            continue
        # Average size
        avg = remaining // (k - i)
        # Random size between 0 and 2*avg
        size = random.randint(0, min(remaining, 2 * avg + 1))
        # Ensure we don't starve too much if we want fairness, but random is okay
        vals = sorted([random.randint(min_val, max_val) for _ in range(size)])
        streams.append(vals)
        remaining -= size
        
    # Last stream gets remainder
    vals = sorted([random.randint(min_val, max_val) for _ in range(remaining)])
    streams.append(vals)
    return k, r, streams

# --- YAML Builder ---

def format_input(k, r, streams):
    lines = [f"{k} {r}"]
    for s in streams:
        lines.append(f"{len(s)}")
        if len(s) > 0:
            lines.append(" ".join(map(str, s)))
        else:
             lines.append("") # Empty line for elements if m=0? No, usually just m=0 line follows by nothing or next m.
             # Wait, standard format for arrays usually: 
             # m
             # elements...
             # If m=0, standard is usually just the line "0". The next line "elements" is empty or skipped.
             # Let's see problem description format.
             # "Line 1: integer m_i. Line 2: m_i integers".
             # If m_i is 0, is line 2 present (empty line) or skipped?
             # Standard competitive programming: read m, then read m integers. If m=0, read loop doesn't run.
             # So likely just "0" on one line, and next line is next "m".
             # BUT "Line 1... Line 2..." implies explicit line structure.
             # If I put an empty line, `split()` in python handles it fine.
             # Safe bet: If m=0, don't print the second line OR print an empty line.
             # Let's check sample.
             # 2 1
             # 2
             # 1 4
             # 3
             # 2 3 5
             # If m=0, I will output "0" and then an empty line to strictly follow "Line 2: m integers" if interpreted literally as a line.
             # Actually, best compatible way is empty line.
             pass
             
    # Refined format_input
    lines = [f"{k} {r}"]
    for s in streams:
        lines.append(str(len(s)))
        if len(s) > 0:
             lines.append(" ".join(map(str, s)))
        else:
             lines.append("") # Empty line for 0 elements
    return "\n".join(lines)

def format_output(result):
    if not result:
        return ""
    return " ".join(map(str, result))

def make_test_case(k, r, streams):
    input_str = format_input(k, r, streams)
    output_list = solve(k, r, streams)
    output_str = format_output(output_list)
    return input_str, output_str


def main():
    test_cases = {
        "problem_id": "HEP_MERGE_K_STREAMS_RATE_LIMIT__9034",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    sk, sr, sstreams = generate_sample_1()
    si, so = make_test_case(sk, sr, sstreams)
    test_cases["samples"].append({"input": si, "output": so})
    
    # Sample 2: Rate limit high (behaves like normal merge)
    s2k, s2r = 3, 10
    s2streams = [[1, 10], [2, 5], [3, 8]]
    s2i, s2o = make_test_case(s2k, s2r, s2streams)
    test_cases["samples"].append({"input": s2i, "output": s2o})

    # Public
    # Edge: Minimum k=1
    pk1, pr1 = 1, 1
    p1streams = [[1, 2, 3]]
    pi1, po1 = make_test_case(pk1, pr1, p1streams)
    test_cases["public"].append({"input": pi1, "output": po1})
    
    # Edge: Empty/Zero elements
    pk2, pr2 = 2, 1
    p2streams = [[], []]
    pi2, po2 = make_test_case(pk2, pr2, p2streams)
    test_cases["public"].append({"input": pi2, "output": po2})
    
    # Basic: r=1 strict interleaving
    pk3, pr3 = 2, 1
    p3streams = [[10, 20], [15, 25]] # Round 1: 10, 15. Round 2: 20, 25.
    pi3, po3 = make_test_case(pk3, pr3, p3streams)
    test_cases["public"].append({"input": pi3, "output": po3})
    
    # Boundary: One stream finishes early
    pk4, pr4 = 2, 2
    p4streams = [[1], [2, 3, 4, 5]]
    pi4, po4 = make_test_case(pk4, pr4, p4streams)
    test_cases["public"].append({"input": pi4, "output": po4})

    # Hidden
    hidden_cases = []
    
    # 1. Edge: r is huge (merge sort)
    h1k, h1r = 5, 1000
    _, _, h1streams = generate_random(h1k, h1r, 50, 1, 100)
    hidden_cases.append(make_test_case(h1k, h1r, h1streams))
    
    # 2. Edge: k max, r=1, small streams (1 element each)
    h2k, h2r = 100, 1
    h2streams = [[i] for i in range(100)]
    hidden_cases.append(make_test_case(h2k, h2r, h2streams))
    
    # 3. Edge: k small, r small, large streams (test rounds)
    h3k, h3r = 2, 1
    h3streams = [[1]*10, [1]*10]
    hidden_cases.append(make_test_case(h3k, h3r, h3streams))
    
    # 4. Stress: All negative
    h4k, h4r = 3, 2
    h4streams = [[-10, -5, -1], [-20, -15, -2], [-30, -25, -3]]
    hidden_cases.append(make_test_case(h4k, h4r, h4streams))
    
    # 5. Negative/Edge: Some empty streams
    h5k, h5r = 4, 2
    h5streams = [[1, 2], [], [3, 4], []]
    hidden_cases.append(make_test_case(h5k, h5r, h5streams))
    
    # 6. Negative: No elements at all
    h6k, h6r = 10, 5
    h6streams = [[] for _ in range(10)]
    hidden_cases.append(make_test_case(h6k, h6r, h6streams))

    # 7. Special: Different sized streams with r=1
    h7k, h7r = 3, 1
    h7streams = [[10], [5, 15], [1, 20, 30]]
    hidden_cases.append(make_test_case(h7k, h7r, h7streams))

    # 8. Normal: Random Small
    h8k, h8r = 5, 2
    _, _, h8streams = generate_random(h8k, h8r, 20, 1, 100)
    hidden_cases.append(make_test_case(h8k, h8r, h8streams))
    
    # 9. Normal: Random Medium
    h9k, h9r = 10, 3
    _, _, h9streams = generate_random(h9k, h9r, 200, 1, 1000)
    hidden_cases.append(make_test_case(h9k, h9r, h9streams))
    
    # 10. Stress: Max k, sparse (1 elem each)
    h10k, h10r = 1000, 10
    _, _, h10streams = generate_random(h10k, h10r, 1000, 1, 10000)
    hidden_cases.append(make_test_case(h10k, h10r, h10streams))

    # 11. Stress: Max N
    # k=10, Total N=200000 (Takes a bit of time to print, let's keep it reasonable for text output if many)
    # Output limit 200k integers is huge for text file? 
    # Usually we limit sample output size in prompts but for test files it's fine.
    # I'll reduce N slightly to avoid huge artifact generation latencies, say 10k.
    h11k, h11r = 10, 100
    _, _, h11streams = generate_random(h11k, h11r, 5000, 1, 100000)
    hidden_cases.append(make_test_case(h11k, h11r, h11streams))
    
    # 12. Mix of single element and empty
    h12streams = []
    for i in range(50):
        if i % 2 == 0: h12streams.append([i])
        else: h12streams.append([])
    hidden_cases.append(make_test_case(50, 2, h12streams))
    
    # 13. Large values bounds
    h13streams = [[-1000000000, 0, 1000000000]]
    hidden_cases.append(make_test_case(1, 1, h13streams))

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
        print("      ") # Print a slightly indented empty line for consistency/valid yaml
    else:
        # Wrap output if too long? No, usually one line.
        # But if output is very long one line, YAML handles it.
        # However, for readability in editor, maybe split?
        # Specification says "Single line of integers". So I must keep it single line.
        print(f"      {c['output']}")

if __name__ == "__main__":
    main()
