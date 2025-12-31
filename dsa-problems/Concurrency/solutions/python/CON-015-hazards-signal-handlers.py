def solve():
    print("""
1. Unsafe Operations:
   - `malloc`/`free`: Maintains global locks/state. If signal interrupts malloc and handler calls malloc, deadlock or corruption.
   - `printf`/IO: Uses buffers/locks.
   - `pthread_mutex_lock`: If interrupted thread holds it -> Deadlock.

2. Minimal Handler:
   ```c
   volatile sig_atomic_t signal_flag = 0;
   
   void handler(int signum) {
       signal_flag = 1;
       // No other logic!
   }
   ```

3. Safe Handoff (Self-Pipe Trick):
   - Create a non-blocking pipe.
   - In handler: `write(pipe_fd[1], &byte, 1)`. `write` is async-signal-safe.
   - In Main Loop: `select` or `poll` on `pipe_fd[0]`.
   - When readable, wake up, read byte, and process the signal event safely in normal context (where malloc/printf are allowed).
""")

if __name__ == "__main__":
    solve()
