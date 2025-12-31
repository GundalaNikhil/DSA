def solve():
    print("""
1. Worker-Local Deque:
   - Each worker `i` has a Deque `D_i`.
   - **Local Ops (Push/Pop)**: Worker `i` pushes new tasks to `D_i` bottom (Tail). Pops from `D_i` bottom (Tail). This is LIFO (Stack-like) for locality.
   - **Steal Ops**: Thief `j` steals from `D_i` top (Head). This is FIFO for fairness and to avoid conflict with local ops at the other end.
   - **Synchronization**:
     - Use a heavy lock? No, performance.
     - Use CAS on `top` and `bottom` indices.
     - Chase-Lev Deque is the standard lock-free structure.
     - Minimal locking: Use a standard Mutex/Spinlock per deque if simplest, but Lock-Free is standard description.

2. Steal Correctness:
   - If `D_i` has many items, Local Pop and Steal don't conflict (different ends).
   - Conflict only when Deque has 1 item (or becomes empty).
   - Use CAS/Atomic loop. If Local Pop sees size 0 or conflict, it handles empty/contention.
   - If Thief sees conflict or empty, it retries or moves to next victim.

3. Sleep/Wake Strategy:
   - If Worker local deque is empty AND steal attempts fail (all other queues empty):
     - Worker enters "Parked" state.
     - Increments `idle_workers` count.
     - Waits on a global Condition Variable or Semaphore.
   - When a task is added (globally or locally):
     - If `idle_workers > 0`, signal one sleeper.

4. Preventing Contention:
   - Randomized Stealing: Thief picks a random victim rather than iterating 0..W leads to less contention.
   - Backoff: If failed to steal, yield/sleep briefly before retry.
   - Local LIFO: keeps hot data in local cache, avoiding true sharing.
""")

if __name__ == "__main__":
    solve()
