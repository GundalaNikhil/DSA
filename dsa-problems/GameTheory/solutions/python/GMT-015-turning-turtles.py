def turning_turtles(n: int, k: int, s: str) -> str:
    xor_sum = 0
    mod = k + 1
    for i, char in enumerate(s):
        if char == 'H':
            xor_sum ^= ((i % mod) + 1)
    return "First" if xor_sum > 0 else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        s = next(iterator)
            
        print(turning_turtles(n, k, s))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
