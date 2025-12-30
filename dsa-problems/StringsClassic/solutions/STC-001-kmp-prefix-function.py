def prefix_function(s: str) -> list[int]:
    n = len(s)
    pi = [0] * n
    j = 0  # length of the previous longest prefix
    
    for i in range(1, n):
        # Backtrack if characters don't match
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        
        # Extend if characters match
        if s[i] == s[j]:
            j += 1
            
        pi[i] = j
        
    return pi

def main():
    import sys
sys.setrecursionlimit(200000)
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    s = input_data[0]
    pi = prefix_function(s)
    print(*(pi))

if __name__ == "__main__":
    main()