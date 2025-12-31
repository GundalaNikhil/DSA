def solve():
    print("""
1. Semaphore Usage:
   - Use a Semaphore initialized to `k`. Each `acquire()` call decrements it.
   - The semaphore represents "available tokens" for the current time window.

2. Refill Mechanism:
   - Token Bucket Approach:
     - Background thread or lazy refill.
     - **Lazy Refill (preferred)**: On `acquire`, check `now`.
     - Calculate `tokens_to_add = (now - last_refill_time) * rate`.
     - Update `current_tokens = min(capacity, current_tokens + tokens_to_add)`.
     - `last_refill_time = now`.
   - Alternatively, for strict 1-second windows: A timer thread adds `k` tokens every second (up to max `k`).

3. Handling Bursts & Drift:
   - **Bursts**: Cap the semaphore value at `k` (capacity). This allows a burst of up to `k` immediately, but no more until time passes.
   - **Drift**: Use a monotonic clock. If using lazy refill, calculation absorbs drift naturally. If using a timer thread, drift is negligible over short periods.

4. Scalability:
   - Standard semaphore operations are O(1).
   - For High Concurrency (`k=10^6`): Contention on the single semaphore lock can be a bottleneck.
   - Mitigation: Striping (multiple semaphores) or using Atomic CAS for token count can improve throughput.
""")

if __name__ == "__main__":
    solve()
