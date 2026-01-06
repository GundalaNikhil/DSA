import sys


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0])
    trimmed = []
    
    # Process each string: trim trailing non-digits (logic might be trim trailing digits?)
    # "Numeric Trim" usually means removing numbers?
    # Original logic: `while j >= 0 and s[j].isdigit(): j -= 1`.
    # This trims SUFFIX digits.
    
    for i in range(1, n + 1):
        s = input_data[i]
        j = len(s) - 1
        while j >= 0 and s[j].isdigit():
            j -= 1
        trimmed.append(s[: j + 1])
        
    if not trimmed:
        print("")
        return
        
    # Find Longest Common Prefix of the trimmed strings
    prefix = trimmed[0]
    for i in range(1, len(trimmed)):
        curr = trimmed[i]
        new_len = 0
        min_len = min(len(prefix), len(curr))
        while new_len < min_len and prefix[new_len] == curr[new_len]:
            new_len += 1
        prefix = prefix[:new_len]
        if not prefix:
            break
            
    print(prefix)


if __name__ == "__main__":
    solve()
