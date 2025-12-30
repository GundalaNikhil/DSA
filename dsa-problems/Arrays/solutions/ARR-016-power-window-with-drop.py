import sys

def max_window_sum_with_drop(arr: list[int], k: int) -> int:
    n = len(arr)
    if n < k: return 0
    
    current_sum = sum(arr[:k])
    max_total = current_sum
    
    for i in range(k, n):
        current_sum += arr[i]
        current_sum -= arr[i-k]
        if current_sum > max_total:
            max_total = current_sum
            
    return max_total

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    result = max_window_sum_with_drop(arr, k)
    print(result)

if __name__ == "__main__":
    main()
  
