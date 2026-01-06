import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    w_size = int(input_data[ptr])
    ptr += 1
    m_events = int(input_data[ptr])
    ptr += 1
    log = []
    for _ in range(m_events):
        log.append(int(input_data[ptr]))
        ptr += 1
        
    counts = {}
    for i in range(m_events):
        a = log[i]
        seen_in_window = set()
        # Look ahead in window
        # Logic seems fine, just nested deeply.
        for j in range(i + 1, min(m_events, i + 1 + w_size)):
            b = log[j]
            # Rule: A implies B within window?
            # Counting pairs (A, B) appearing within window distance.
            pair = (a, b)
            counts[pair] = counts.get(pair, 0) + 1
            
    # Find best rule after counting ALL
    best_rule = (0, 0)
    max_c = -1
    
    for (a, b), c in counts.items():
        if c > max_c:
            max_c = c
            best_rule = (a, b)
        elif c == max_c:
            # Tie-breaking
            if a < best_rule[0]:
                best_rule = (a, b)
            elif a == best_rule[0]:
                if b < best_rule[1]:
                    best_rule = (a, b)
                    
    print(f"{best_rule[0]} {best_rule[1]}")


if __name__ == "__main__":
    solve()
