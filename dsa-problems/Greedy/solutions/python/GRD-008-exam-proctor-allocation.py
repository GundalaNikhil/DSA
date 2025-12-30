import sys
import math

def min_proctors(n: int, r: int, exams: list) -> int:
    events = []
    for start, end in exams:
        events.append((start, 1))
        events.append((end, -1))
        
    # Sort events.
    # Primary key: time.
    # Secondary key: type. We want +1 before -1 to maximize overlap at boundaries.
    # In Python sort, (time, -1) comes before (time, 1).
    # So we should use type values that sort correctly, or reverse secondary sort.
    # Let's use type: 1 for start, -1 for end.
    # We want 1 before -1.
    # So sort by (time, -type) or custom key.
    events.sort(key=lambda x: (x[0], -x[1]))
    
    max_overlap = 0
    current_overlap = 0
    
    for _, type_ in events:
        current_overlap += type_
        max_overlap = max(max_overlap, current_overlap)
        
    # Ceiling division
    return (max_overlap + r - 1) // r

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    r = int(next(iterator))
    
    exams = []
    for _ in range(n):
        start = int(next(iterator))
        end = int(next(iterator))
        exams.append([start, end])
    
    result = min_proctors(n, r, exams)
    print(result)

if __name__ == "__main__":
    main()
