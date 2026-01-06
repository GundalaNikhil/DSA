import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        s = int(next(iterator))
        b = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
            
        table = []
        for _ in range(s):
            row = []
            for _ in range(b):
                row.append(int(next(iterator)))
            table.append(row)
    except StopIteration:
        return

    
    visit_counts = [0] * s
    curr_state = 0
    visit_counts[curr_state] += 1 # Initial state visited? Usually yes.
    
    for x in a:
        bucket = ((x % b) + b) % b
        curr_state = table[curr_state][bucket]
        visit_counts[curr_state] += 1
        
    print(*(visit_counts))

if __name__ == "__main__":
    solve()
