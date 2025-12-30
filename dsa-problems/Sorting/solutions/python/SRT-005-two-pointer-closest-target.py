def closest_pair(arr: list[int], target: int) -> list[int]:
    n = len(arr)
    left = 0
    right = n - 1
    
    min_diff = float('inf')
    res_pair = []
    
    while left < right:
        current_sum = arr[left] + arr[right]
        diff = abs(current_sum - target)
        
        if diff < min_diff:
            min_diff = diff
            res_pair = [arr[left], arr[right]]
        
        if current_sum < target:
            left += 1
        else:
            right -= 1
            
    return res_pair

def main():
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = closest_pair(arr, target)
    print(result[0], result[1])

if __name__ == "__main__":
    main()
