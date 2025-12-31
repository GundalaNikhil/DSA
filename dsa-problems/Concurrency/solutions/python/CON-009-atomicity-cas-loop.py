def solve():
    print("""
1. CAS Loop Sketch (Atomic Increment):
   ```python
   def atomic_increment(x):
       while True:
           old_val = x.get()
           new_val = old_val + 1
           if x.compare_and_swap(old_val, new_val):
               return new_val
           # else retry (loop)
   ```

2. ABA Problem:
   - ABA occurs when a value changes from A to B and back to A.
   - A thread reads A, calculates, then tries CAS(A -> New). It succeeds because value is A, but it missed the intermediate B state.
   - **Example**: Stack Pop.
     - Stack: Top -> A -> B.
     - Thread 1 Reads Top (A), Next (B). Preempted.
     - Thread 2 Pops A, Pops B. Pushes A back. Stack: Top -> A.
     - Thread 1 resumes: CAS(Top, A -> B). Succeeds!
     - Stack is now Top -> B. BUT B was freed/gone! Stack is corrupted.

3. Mitigation Strategies:
   - **Tagged Pointers / Version Counting (Preferred for simple cases)**:
     - Store `(value, version)` in the atomic word.
     - CAS checks both. `A -> B -> A` becomes `(A, v1) -> (B, v2) -> (A, v3)`.
     - `CAS((A, v1), ...)` fails against `(A, v3)`.
   - **Hazard Pointers**: Threads publish "I am reading node P". Other threads cannot free P while published. Solves use-after-free inherent in ABA.
""")

if __name__ == "__main__":
    solve()
