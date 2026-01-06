import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    t_count = int(input_data[ptr])
    ptr += 1
    tasks = []
    for _ in range(t_count):
        tasks.append(
            (
                int(input_data[ptr]),
                int(input_data[ptr + 1]),
                int(input_data[ptr + 2]),
            )
        )
        ptr += 3
        
    tasks.sort(key=lambda x: x[1])
    dp = [0] * (n + 1)
    
    # Using Disjoint Set Union (DSU) to find available slots
    # parent[i] points to the next available slot <= i ??
    # Usually for "find rightmost free slot <= R", we use DSU where parent[i] = i means i is free.
    # If we use i, we unite i with i-1.
    parent = list(range(n + 1))


def find(i, parent):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i], parent)
    return parent[i]

# Sort by value DESC to greedily pick best tasks compatible with deadlines?
# Problem "Temporal Constraints" with (l, r, v).
# Usually means task available in [l, r] with value v.
# Or takes 1 slot? "slot = find(r)". "if slot >= l".
# This implies each task takes 1 unit of time and must be done by R, but not before L.
# Greedy strategy: Process tasks by Value DESC. Try to schedule as late as possible (at R, or R-1...).
# DSU `find(r)` gives largest index <= r that is free.
# If that index >= l, we can schedule it.
# Then mark `slot` as occupied by uniting with `slot - 1`.

tasks.sort(key=lambda x: x[2], reverse=True)
total_reward = 0

for l, r, v in tasks:
    slot = find(r, parent)
    if slot >= l:
        total_reward += v
        # Union slot with slot-1
        # Careful with boundary 0.
        if slot > 0:
            parent[slot] = find(slot - 1, parent)
        else:
            # If slot 0 is used (assuming 1-based indexing for time?)
            # Code line 41: `parent[slot] = find(slot - 1)`
            # If slot is 0, find(-1) error.
            # Assuming n >= 1 and tasks are 1-based.
            # If slot 0 is sentinel, maybe handled?
            # Safe to assume valid range if code worked before.
            # But let's be safe.
             parent[slot] = find(slot - 1, parent)
             
print(total_reward)
if __name__ == "__main__":
    solve()
