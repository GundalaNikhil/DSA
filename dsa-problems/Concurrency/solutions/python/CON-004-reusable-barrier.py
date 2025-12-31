def solve():
    print("""
1. Algorithm (Two-Phase / Generation Barrier):
   - State: `count` (arrived threads), `N` (total), `generation` (phase ID).
   - Mutex `lock` and Condition Variable `cv`.
   - **Arrival**:
     - Acquire lock.
     - `my_gen = generation`.
     - `count++`.
     - If `count == N`:
       - `count = 0` (reset for next phase/release).
       - `generation++` (advance phase).
       - `broadcast(cv)` (wake everyone).
     - Else:
       - While `my_gen == generation`: `wait(cv)`.
     - Release lock.

2. Reusability:
   - The `generation` ID distinguishes phases. Threads waiting for phase `k` explicitly check `generation == k`.
   - When the last thread arrives, it updates `generation` to `k+1`. This condition fails for all waiting threads, so they wake and exit the loop.
   - They leave the barrier and proceed. The barrier state (`count=0`, `generation=k+1`) is ready for the next phase.

3. Lost/Spurious Wakeups:
   - **Lost Wakeup**: Handled by `broadcast`. All threads effectively check condition.
   - **Spurious Wakeup**: Handled by the `while` loop checking `generation`. If woken spuriously but generation hasn't changed, thread sleeps again.
""")

if __name__ == "__main__":
    solve()
