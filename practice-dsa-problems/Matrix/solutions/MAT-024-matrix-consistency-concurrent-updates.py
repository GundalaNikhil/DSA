import sys
from collections import defaultdict
import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    cell_writers = {}
    cell_readers = defaultdict(list)
    adj = defaultdict(set)
    threads = set()
    for _ in range(q):
        tid = int(input_data[ptr])
        ptr += 1
        op = input_data[ptr]
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        c = int(input_data[ptr])
        ptr += 1
        threads.add(tid)
        cell = (r, c)
        if op == "R":
            if cell in cell_writers:
                w_tid = cell_writers[cell]
                if w_tid != tid:
                    adj[w_tid].add(tid)
            cell_readers[cell].append(tid)
        else: # W
            if cell in cell_writers:
                w_tid = cell_writers[cell]
                if w_tid != tid:
                    adj[w_tid].add(tid) # Current writer must be after prev writer?
                    # "Concurrent updates": Usually "Serialization Graph".
                    # T1 writes x, T2 reads x -> T1 -> T2.
                    # T1 writes x, T2 writes x -> T1 -> T2.
                    # T1 reads x, T2 writes x -> T1 -> T2.
                    
            # Add edges from readers to this writer
            for r_tid in cell_readers[cell]:
                if r_tid != tid:
                    adj[r_tid].add(tid)
                    
            cell_writers[cell] = tid
            cell_readers[cell] = [] # Readers processed? Or kept?
            # Writers obscure previous version. Readers read new one.
            # So dependent edges already added.
            
    visited = {}
    
    def has_cycle(u):
        visited[u] = 0 # Gray
        for v in adj[u]:
            if v not in visited:
                if has_cycle(v):
                    return True
            elif visited[v] == 0:
                return True
        visited[u] = 1 # Black
        return False

    for t in threads:
        if t not in visited:
            if has_cycle(t):
                print("NOT_SERIALIZABLE")
                return
    print("SERIALIZABLE")


if __name__ == "__main__":
    solve()
