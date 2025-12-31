def solve():
    print("""
1. State Variables:
   - `active_readers`: count of readers currently holding the lease.
   - `writer_waiting`: boolean/count, true if a writer is waiting.
   - `max_lease_expiry`: timestamp of the furthest lease expiry among active readers.
   - `mutex`: protects state.
   - `cond_read`: for readers to wait.
   - `cond_write`: for writers to wait.

2. Waiting Rules:
   - **Reader Entry**: Can proceed if `!writer_waiting`. If valid, increments `active_readers`, sets local lease expiry `now + L`.
   - **Reader Renewal**: Can renew if `!writer_waiting`. Updates local lease and global `max_lease_expiry`.
   - **Writer Entry**: Sets `writer_waiting = true`. Waits on `cond_write` until `active_readers == 0`.

3. Renewal Policy:
   - If a writer arrives (`writer_waiting` becomes true), NEW readers are blocked.
   - EXISTING readers attempting to renew are *also* blocked (or told to release). This allows the active leases to naturally expire within at most `L` time, preventing writer starvation.

4. Writer Starvation Prevention:
   - The `writer_waiting` flag acts as a gate. Once set, no new read leases (or renewals) are granted.
   - The system drains active readers.
   - Writer proceeds after the last reader leaves.
   - Upon exit, writer clears `writer_waiting` and wakes all readers/writers.

5. Assumptions:
   - Readers cooperate (check renewal or release).
   - Clocks are reasonably synchronized or monotonic for `L`. Lease expiry is a failsafe.
""")

if __name__ == "__main__":
    solve()
