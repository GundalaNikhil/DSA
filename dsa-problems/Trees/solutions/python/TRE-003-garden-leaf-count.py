import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def count_leaves(n: int, left: list[int], right: list[int]) -> int:
    if n == 0:
        return 0
    
    # Iterative approach on array
    count = 0
    for i in range(n):
        if left[i] == -1 and right[i] == -1:
            count += 1
    return count

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    left = [0] * n
    right = [0] * n
    for i in range(n):
        _ = data[idx]; idx += 1
        left[i] = int(data[idx]); idx += 1
        right[i] = int(data[idx]); idx += 1
        
    print(count_leaves(n, left, right))

if __name__ == "__main__":
    main()
