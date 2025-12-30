import sys

def odd_after_bit_salt(a: list[int], salt: int) -> int:
    result = 0
    for x in a:
        result ^= (x ^ salt)
    return result

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    
    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1
    
    salt = int(data[ptr]); ptr += 1
    
    result = odd_after_bit_salt(a, salt)
    print(result)

if __name__ == "__main__":
    main()
