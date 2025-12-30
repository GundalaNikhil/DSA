def longest_after_change(arr: list[int]) -> int:
    n = len(arr)
    if n <= 1:
        return n
        
    L = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            L[i] = L[i-1] + 1
            
    R = [1] * n
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i+1]:
            R[i] = R[i+1] + 1
            
    max_len = max(L) # Original max
    
    for i in range(n):
        # Change arr[i]
        
        # Extend left
        if i > 0:
            max_len = max(max_len, L[i-1] + 1)
            
        # Extend right
        if i < n - 1:
            max_len = max(max_len, R[i+1] + 1)
            
        # Bridge
        if i > 0 and i < n - 1 and arr[i+1] - arr[i-1] >= 2:
            max_len = max(max_len, L[i-1] + 1 + R[i+1])
            
    return max_len

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_after_change(arr)
    print(result)

if __name__ == "__main__":
    main()
