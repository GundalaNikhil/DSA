def solve():
    print("""
1. Snapshot Rules (Read Visibility):
   - A transaction T (start timestamp TS_S) reads a row version V if:
     - V.created < TS_S (Created before T started).
     - V.deleted > TS_S (Not deleted before T started, or not deleted at all).
     - V is committed.
   - **Result**: Readers see a consistent snapshot of the DB at `TS_S`, ignoring active writes by other txns (Non-blocking reads).

2. Commit Rules:
   - Writes create NEW versions of rows (append-only logic or diffs).
   - On commit, new versions become visible to future transactions.
   - Update Transaction timestamp to Current.

3. Write-Write Conflicts:
   - If T1 wants to update Row R, but R was updated by T2 (which committed AFTER T1 started, or is active):
   - **Detection**: T1 checks if the latest version of R is visible to it. If latest version > T1.start, Conflict.
   - **Resolution**: T1 Aborts (First-Committer-Wins) OR T1 waits for T2 to commit/abort (in blocking databases like Postgres, picking up the new version if Isolation allows).

4. Garbage Collection (Vacuum):
   - Old versions that are no longer visible to ANY active transaction snapshot (Created < Oldest_Active_Start) must be cleaned up to reclaim space.
""")

if __name__ == "__main__":
    solve()
