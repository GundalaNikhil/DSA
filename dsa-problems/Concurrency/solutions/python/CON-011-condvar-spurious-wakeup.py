def solve():
    print("""
1. Canonical Wait Loop:
   ```python
   lock.acquire()
   while not predicate():
       cond.wait()  # Releases lock, sleeps, re-acquires lock upon wake
   # Check passed, proceed
   do_work()
   lock.release()
   ```

2. Spurious & Lost Wakeups:
   - **Spurious Wakeup**: A thread trapped in `cond.wait()` might wake up *without* a corresponding `signal()`/`notify()` call from another thread. This can happen due to OS scheduling quirks or signal handling. Using a `while` loop checks the predicate again; if false, it goes back to sleep.
   - **Lost Wakeup**: Occurs if a thread calls `signal()` *before* the waiter actually waits (and the signal isn't "saved"). Since Condition Variables differ from Semaphores (no state), signals meant for future waiters are lost. Ensuring the waiter checks the predicate *under the lock* before waiting prevents this race.

3. Common Bug:
   - Using `if` instead of `while`:
     ```python
     if not predicate:
         cond.wait()
     # Proceed assuming predicate is true
     ```
     - **Why it fails**: If a spurious wakeup occurs, the thread proceeds with the False predicate, potentially violating invariants (e.g., consuming from empty buffer).
     - Also fails if multiple threads wake up but only one unit of resource is available (Signal-Stealing).
""")

if __name__ == "__main__":
    solve()
