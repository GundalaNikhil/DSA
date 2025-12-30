import sys

# Increase recursion depth just in case, though not needed for iterative
sys.setrecursionlimit(2000)

def compute_prefix_hashes(s: str, B: int, M: int) -> list:
    hashes = []
    current_hash = 0

    for char in s:
        # ord(char) gets the ASCII value
        current_hash = (current_hash * B + ord(char)) % M
        hashes.append(current_hash)

    return hashes

def main():
    # Read input line by line
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 2:
        return

    s = lines[0]
    B, M = map(int, lines[1].split())

    result = compute_prefix_hashes(s, B, M)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
