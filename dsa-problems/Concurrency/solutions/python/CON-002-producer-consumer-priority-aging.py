def solve():
    # Design problem - output text description
    print("""
1. Data Structures:
   - A Min-Heap storing `(effective_priority, arrival_time, item)`.
   - A Mutex `lock` to protect the queue.
   - Two Condition Variables: `not_full` (for producers) and `not_empty` (for consumers).

2. Concurrency Primitives:
   - Mutex for mutual exclusion.
   - Condition Variables for signaling state changes (queue space available / item available).

3. Synchronization Rules:
   - Producer: Acquire lock. While queue is full, wait on `not_full`. Insert item with base priority. Signal `not_empty`. Release lock.
   - Consumer: Acquire lock. While queue is empty, wait on `not_empty`. Extract min (highest priority). Signal `not_full`. Release lock.
   - To avoid lost wakeups, use `notify_all` if multiple threads may be woken, or ensure signal logic covers all waiters. Using distinct CVs prevents "wrong thread" wakeups.

4. Efficient Aging:
   - Instead of updating all priorities every T ms (O(N) or O(N log N)), store `(base_priority - arrival_time / T)` as the key.
   - Effective Priority P_eff = P_base + (current_time - arrival_time) / T
                              = P_base - arrival_time/T + current_time/T
   - Since `current_time/T` is common to all items, we can just sort by `P_base - arrival_time/T`.
   - The item with the largest such key has the highest effective priority. (Note: Problem says Higher Integer = More Important, checks Max-Heap logic).

5. Starvation Prevention:
   - Aging ensures that an old item's priority strictly increases over time relative to new items. Eventually, any waiting item will exceed the priority of incoming items, guaranteeing it will be strictly chosen.
""")

if __name__ == "__main__":
    solve()
