import sys


def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    res = []
    i = 0
    while i < len(s):
        char = s[i]
        j = i
        while j < len(s) and s[j] == char:
            j += 1
            
        count = j - i
        while count > 9:
            res.append(f"{char}9")
            count -= 9
            
        if count > 0:
            res.append(f"{char}{count}")
            
        i = j
        
    print("".join(res))


if __name__ == "__main__":
    solve()
