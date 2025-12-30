import sys
import math

def top_k_with_decay(events: list[tuple[int, int]], now: int, D: int, k: int) -> list[int]:
    scores = {}
    
    for val, t in events:
        term = math.exp(-(now - t) / D)
        scores[val] = scores.get(val, 0.0) + term
        
    # Convert to list of (score, val)
    # Sort key: (-score, val) -> Descending score, Ascending val
    items = []
    for val, score in scores.items():
        items.append((-score, val))
        
    items.sort()
    
    result = []
    for i in range(min(k, len(items))):
        result.append(items[i][1]) # Append val
        
    return result

def main():
    n = int(input())
    events = []
    for _ in range(n):
        value, timestamp = map(int, input().split())
        events.append((value, timestamp))
    now, D, k = map(int, input().split())

    result = top_k_with_decay(events, now, D, k)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
