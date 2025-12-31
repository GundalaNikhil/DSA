
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    try:
        cs = int(data[0])
        w = int(data[1])
        
        if w > 10: # Arbitrary threshold based on Typical Context Switch (approx 5-10us)
            print("MUTEX")
            print(f"Expected wait ({w}us) is large compared to critical section ({cs}us). Spinning would waste CPU cycles. Blocking via Mutex frees the core for other tasks despite the context-switch overhead.")
        else:
            print("SPINLOCK")
            print(f"Expected wait ({w}us) is very short, likely smaller than a context switch. Spinning avoids the overhead of descheduling and is more efficient for such brief contention.")
            
    except Exception:
        return

if __name__ == "__main__":
    solve()
