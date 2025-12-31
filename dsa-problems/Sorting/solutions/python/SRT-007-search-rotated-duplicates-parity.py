def count_even_indices(arr: list[int], x: int) -> int:
    n = len(arr)
    
    def find_pivot(low, high):
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            elif arr[mid] < arr[high]:
                high = mid
            else:
                high -= 1
        return low
        
    def search_range(low, high, target):
        start, end = -1, -1

        # Find leftmost occurrence
        l, r = low, high
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                start = mid
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if start == -1:
            return -1, -1

        # Find rightmost occurrence
        l, r = low, high
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                end = mid
                l = mid + 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return start, end
        
    def count_evens(L, R):
        if L > R: return 0
        length = R - L + 1
        if length % 2 == 0:
            return length // 2
        return (length + 1) // 2 if L % 2 == 0 else (length - 1) // 2

    pivot = find_pivot(0, n - 1)
    count = 0
    
    if pivot > 0:
        s, e = search_range(0, pivot - 1, x)
        if s != -1:
            count += count_evens(s, e)
            
    s, e = search_range(pivot, n - 1, x)
    if s != -1:
        count += count_evens(s, e)
        
    return count

def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    result = count_even_indices(arr, x)
    print(result)

if __name__ == "__main__":
    main()
