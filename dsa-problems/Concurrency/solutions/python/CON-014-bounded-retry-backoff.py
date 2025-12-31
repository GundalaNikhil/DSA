def solve():
    print("""
1. Retry Loop with Exponential Backoff + Jitter:
   ```python
   def retry_op(max_retries, initial_delay, max_cap):
       retries = 0
       delay = initial_delay
       
       while True:
           try:
               return attempt_op()
           except TransientError:
               retries += 1
               if retries > max_retries:
                   raise PermanentFailure()
               
               # Jitter to avoid resonance
               sleep_time = random.uniform(0, min(delay, max_cap))
               sleep(sleep_time)
               
               delay *= 2  # Exponential increase
   ```

2. Why it improves behavior:
   - **Exponential**: Quickly reduces load if the system is overloaded. If 1000 threads fail, they spread out their retries (1ms, 2ms, 4ms...) rather than hammering repeatedly at fixed intervals.
   - **Jitter**: Prevents "synchronized" retries where batches of threads wake up, fail together, and wait together. Randomness de-synchronizes the herd.

3. Choosing Caps:
   - `initialDelay`: Round-trip time or expected recovery time (e.g., 5-50ms).
   - `maxDelay`: Depends on user latency tolerance (e.g., 1s for interactive, 30s for background).
   - `maxRetries`: Budget for total waiting time.
""")

if __name__ == "__main__":
    solve()
