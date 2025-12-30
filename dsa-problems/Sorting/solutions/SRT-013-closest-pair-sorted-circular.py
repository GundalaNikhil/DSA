def closest_pair_circular(arr: list[int], target: int) -> list[int]:
    n = len(arr)
    if n == 0:
        return []
        
    # Find pivot
    pivot = 0
    for i in range(1, n):
        if arr[i] < arr[pivot]:
            pivot = i
            
    l, r = 0, n - 1
    min_diff = float('inf')
    res = []
    
    while l < r:
        pL = (pivot + l) % n
        pR = (pivot + r) % n
        
        curr_sum = arr[pL] + arr[pR]
        diff = abs(curr_sum - target)
        
        if diff < min_diff:
            min_diff = diff
            res = [arr[pL], arr[pR]]
            
        if curr_sum < target:
            l += 1
        else:
            r -= 1
            
    return res

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    result = closest_pair(arr, target)
    print(result[0], result[1])

if __name__ == "__main__":
    main()
