def find_peak(arr: list[int], q_limit: int) -> int:
    n = len(arr)
    low = 0
    high = n - 1
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid+1]:
            low = mid + 1
        else:
            high = mid
            
    return low

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    result = find_peak(arr, q)
    print(result)

if __name__ == "__main__":
    main()
