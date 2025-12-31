def solve():
    print("""
1. Michael-Scott Queue Invariants:
   - Linked List of nodes.
   - `head` points to a dummy node (or valid head). `tail` points to last or near-last node.
   - `next` pointers are atomic.
   - Invariant: `tail` is reachable from `head`. List is always connected.

2. Enqueue(x):
   - Allocate Node `new(x)`.
   - Loop:
     - Read `tail` (T), `T.next` (N).
     - If `T` usually points to last, `N` should be Null.
     - If `N` != Null: `tail` is lagging. Help advance it: `CAS(tail, T -> N)`. Retry.
     - If `N` == Null: Try `CAS(T.next, Null -> new)`.
     - If success: `CAS(tail, T -> new)` (Advance tail). Return.
     - If fail: Retry.

3. Dequeue():
   - Loop:
     - Read `head` (H), `tail` (T), `H.next` (N).
     - If `H == T`:
       - If `N == Null`: Queue empty. Return.
       - Else: `tail` lagging. `CAS(tail, T -> N)`. Retry.
     - Read value from `N`.
     - Try `CAS(head, H -> N)`. (Swing head forward).
     - If success: Return value. (Old head H is reclaimed).

4. Memory Reclamation (ABA):
   - Issue: If `Dequeue` reads H, sleeps, then H is freed and reallocated as new node inserted at Tail... complex corruption.
   - **Mitigation (Epoch Based Reclamation)**:
     - Global `epoch`. Threads register into local epoch.
     - `Free(node)` doesn't delete immediately. Adds to `limbo` list for `current_epoch`.
     - When all threads have moved past `epoch e`, nodes in `limbo[e]` are safely deleted.
""")

if __name__ == "__main__":
    solve()
