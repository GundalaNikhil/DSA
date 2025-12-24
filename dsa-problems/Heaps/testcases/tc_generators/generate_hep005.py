
import sys
import random
import bisect

# --- Reference Solution ---
def solve(n, k, s, meetings):
    # Sort meetings by start time
    meetings.sort(key=lambda x: x[0])
    
    # Available times of rooms. 
    # To handle 'unused', we can use -1 (assuming starts >= 0).
    # Since starts >= 0, available time of -1 is always valid and <= start.
    # Slack for -1 is 0. 
    # Use a sorted list for availability.
    # Initialize with k rooms at -1.
    
    # Optimization: If k is large, this list is huge.
    # Bisect insort is O(K). Total O(NK).
    # If N=10^5, K=10^5 -> TLE.
    # We will assume for generation we respect limits.
    
    rooms = [-1] * k
    total_slack = 0
    
    for start, end in meetings:
        # Find largest room_end <= start
        # bisect_right returns index where start could be inserted while maintaining order.
        # all elements to left are <= start.
        # The element at idx-1 is the largest <= start.
        
        idx = bisect.bisect_right(rooms, start)
        
        if idx == 0:
            # No room available <= start.
            # But problem guarantees valid schedule exists.
            # If our Greedy fails, the assumption of Best Fit optimality or Valid Schedule Guarantee logic is tricky.
            # However, for Min Idle with fixed intervals, Best Fit is generally correct.
            # If idx=0, it means all available times > start.
            # This implies we MUST pick a room that is not ready? Impossible for valid schedule.
            # So this branch should theoretically not happen given problem statement.
            # We'll raise error or just handle gracefully (pick smalllest > start? No that overlaps).
            # We assume valid input.
            pass
        else:
            best_room_idx = idx - 1
            prev_end = rooms[best_room_idx]
            
            # If prev_end is -1 (unused), slack is 0.
            if prev_end == -1:
                slack = 0
            else:
                slack = start - prev_end
            
            total_slack += slack
            
            # Remove used room and re-insert new availability
            new_avail = end + s
            rooms.pop(best_room_idx)
            bisect.insort(rooms, new_avail)
            
    return total_slack

# --- Test Case Generators ---

def generate_sample_1():
    n, k, s = 3, 2, 1
    meetings = [
        [0, 10],
        [5, 8],
        [13, 20]
    ]
    return n, k, s, meetings

def generate_random_valid(n, k, s, max_time):
    # Generate random meetings.
    # Challenge: Ensure valid schedule exists for k rooms.
    # Strategy: Simulate k parallel timelines.
    # Assign meetings to specific timelines.
    # Collect all meetings and return.
    
    timelines = [0] * k # current end time of each timeline
    meetings = []
    
    # We want roughly n meetings.
    for _ in range(n):
        # Pick a random timeline
        r = random.randint(0, k-1)
        prev_end = timelines[r]
        
        # Start must be >= prev_end + s (if previous existed) or >= 0
        # Add some random slack
        slack = random.randint(0, 100)
        start = max(0, prev_end + s) + slack
        duration = random.randint(1, 100)
        end = start + duration
        
        meetings.append([start, end])
        timelines[r] = end
        
    return n, k, s, meetings

# --- YAML Builder ---

def format_input(n, k, s, meetings):
    lines = [f"{n} {k} {s}"]
    for m in meetings:
        lines.append(f"{m[0]} {m[1]}")
    return "\n".join(lines)

def format_output(val):
    return str(val)

def make_test_case(n, k, s, meetings):
    input_str = format_input(n, k, s, meetings)
    output_val = solve(n, k, s, meetings)
    output_str = format_output(output_val)
    return input_str, output_str


def main():
    test_cases = {
        "problem_id": "HEP_MEETING_ROOMS_MIN_IDLE_SETUP__3108",
        "samples": [],
        "public": [],
        "hidden": []
    }

    # Samples
    sn, sk, ss, sm = generate_sample_1()
    si, so = make_test_case(sn, sk, ss, sm)
    test_cases["samples"].append({"input": si, "output": so})
    
    # Sample 2: Tight fit
    s2n, s2k, s2s = 2, 1, 5
    s2m = [[0, 10], [15, 20]] # Gap 5. s=5. Slack = 15 - (10+5) = 0.
    s2i, s2o = make_test_case(s2n, s2k, s2s, s2m)
    test_cases["samples"].append({"input": s2i, "output": s2o})

    # Public
    # Edge: n=1
    p1n, p1k, p1s = 1, 1, 0
    p1m = [[10, 20]]
    pi1, po1 = make_test_case(p1n, p1k, p1s, p1m)
    test_cases["public"].append({"input": pi1, "output": po1})
    
    # Edge: k=n (all can be new freq)
    p2n, p2k, p2s = 3, 3, 0
    p2m = [[0, 10], [0, 10], [0, 10]]
    pi2, po2 = make_test_case(p2n, p2k, p2s, p2m)
    test_cases["public"].append({"input": pi2, "output": po2}) # 0 slack

    # Basic: Simple chain
    p3n, p3k, p3s = 2, 1, 0
    p3m = [[0, 5], [10, 15]]
    pi3, po3 = make_test_case(p3n, p3k, p3s, p3m)
    test_cases["public"].append({"input": pi3, "output": po3}) # Slack 5

    # Hidden
    hidden_cases = []
    
    # 1. Edge: s=0
    h1n, h1k, h1s = 10, 2, 0
    _, _, _, h1m = generate_random_valid(h1n, h1k, h1s, 1000)
    hidden_cases.append(make_test_case(h1n, h1k, h1s, h1m))
    
    # 2. Edge: s large
    h2n, h2k, h2s = 10, 2, 1000
    _, _, _, h2m = generate_random_valid(h2n, h2k, h2s, 10000)
    hidden_cases.append(make_test_case(h2n, h2k, h2s, h2m))

    # 3. Stress: N=1000, K=100 (Bisect is fine)
    h3n, h3k, h3s = 1000, 100, 5
    _, _, _, h3m = generate_random_valid(h3n, h3k, h3s, 100000)
    hidden_cases.append(make_test_case(h3n, h3k, h3s, h3m))
    
    # 4. Stress: N=3000, K=10 (Bisect very fast)
    h4n, h4k, h4s = 3000, 10, 5
    _, _, _, h4m = generate_random_valid(h4n, h4k, h4s, 50000)
    hidden_cases.append(make_test_case(h4n, h4k, h4s, h4m))
    
    # 5. Stress: K=N (N moderate 1000) -> O(N^2) bisect? 1000^2 = 10^6. Fast.
    h5n, h5k, h5s = 1000, 1000, 2
    _, _, _, h5m = generate_random_valid(h5n, h5k, h5s, 50000)
    hidden_cases.append(make_test_case(h5n, h5k, h5s, h5m))

    # 6. Negative/Edge: Single room, forced large slack
    h6m = [[0, 10], [100, 110]]
    hidden_cases.append(make_test_case(2, 1, 0, h6m))
    
    # 7. Special: All meetings disjoint, 1 room
    h7m = []
    curr = 0
    for _ in range(10):
        h7m.append([curr, curr+5])
        curr += 10 # gap of 5
    hidden_cases.append(make_test_case(10, 1, 0, h7m))
    
    # 8. Special: All meetings overlapping, K=N needed
    h8m = [[0, 5] for _ in range(10)]
    hidden_cases.append(make_test_case(10, 10, 5, h8m))
    
    # 9. Normal random
    h9n, h9k, h9s = 50, 5, 2
    _, _, _, h9m = generate_random_valid(h9n, h9k, h9s, 1000)
    hidden_cases.append(make_test_case(h9n, h9k, h9s, h9m))

    # 10. Large values
    h10m = [[0, 10], [2000000000, 2000000010]] # 2*10^9 valid? check constraints.
    # Constraints: end <= 10^9. So 2*10^9 is invalid.
    # Use max 10^9.
    h10m = [[0, 10], [999999990, 1000000000]]
    hidden_cases.append(make_test_case(2, 1, 0, h10m))

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
