import sys

def mod_exp_stream(a: int, m: int, e: str) -> int:
    # Python handles large integers automatically, so pow(a, int(e), m) works.
    # However, for educational purposes and strict O(|e|) without big int conversion overhead:
    
    ans = 1
    for char in e:
        d = int(char)
        # ans = ans^10 * a^d
        ans = pow(ans, 10, m)
        term = pow(a, d, m)
        ans = (ans * term) % m
        
    return ans

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    a = int(data[0])
    m = int(data[1])
    e = data[2]
    print(mod_exp_stream(a, m, e))

if __name__ == "__main__":
    main()
