def solve():
    print("""
1. Pseudocode:
   ```python
   class TicketLock:
       def __init__(self):
           self.next_ticket = AtomicInteger(0)
           self.now_serving = AtomicInteger(0)

       def lock(self):
           my_ticket = self.next_ticket.get_and_increment()
           while self.now_serving.get() != my_ticket:
               # Spin hint / yield
               pass
           # Acquired

       def unlock(self):
           # Publish correct ordering
           self.now_serving.increment()
   ```

2. Fairness (FIFO):
   - Tickets are handed out in strictly increasing order (0, 1, 2...).
   - The thread with ticket `k` is ONLY allowed to enter when `nowServing == k`.
   - Since `nowServing` increments by 1 on unlock, threads enter strictly in ticket order. No barge-in possible.

3. Cache Contention:
   - **Thundering Herd / Cache Thrashing**: All waiting threads spin on the SAME `nowServing` cache line.
   - When `nowServing` updates, the line is invalidated for ALL caches. All N threads re-read. O(N) bus traffic per unlock.
   - Poor scalability for high N.

4. Improvement (MCS Lock):
   - **MCS Lock** builds a queue of nodes (linked list) in memory.
   - Each thread spins on its OWN node's flag (`is_locked`).
   - Unlocker only notifies the NEXT thread (writes to next node's cache line).
   - O(1) bus traffic per unlock. Better for high contention/high core count.
""")

if __name__ == "__main__":
    solve()
