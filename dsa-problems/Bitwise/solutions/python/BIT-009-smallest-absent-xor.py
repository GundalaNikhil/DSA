import sys

def smallest_absent_xor(a: list[int]) -> int:
    basis = [0] * 32
    
    for x in a:
        for i in range(30, -1, -1):
            if (x >> i) & 1:
                if basis[i] == 0:
                    basis[i] = x
                    break
                x ^= basis[i]
                
    for i in range(31):
        if basis[i] == 0:
            return 1 << i
            
    return 1 << 31

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
        
    result = smallest_absent_xor(a)
    print(result)

if __name__ == "__main__":
    main()
