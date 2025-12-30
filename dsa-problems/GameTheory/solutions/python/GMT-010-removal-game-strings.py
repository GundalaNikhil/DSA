from typing import List

def get_grundy(k: int) -> int:
    if k == 0: return 0
    if k == 1: return 1
    if k == 2: return 0
    rem = k % 3
    if rem == 0: return 2
    if rem == 1: return 1
    return 0

def string_game(n: int, strings: List[str]) -> str:
    xor_sum = 0
    for s in strings:
        if not s:
            continue
        groups = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                groups += 1
        xor_sum ^= get_grundy(groups)
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
        strings = []
        for _ in range(n):
            strings.append(next(iterator))
            
        print(string_game(n, strings))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
