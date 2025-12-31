def kth_triple_sum(arr: list[int], k: int) -> int:
    n = len(arr)
    arr.sort()
    
    def count_less_equal(target):
        count = 0
        for i in range(n - 2):
            # Optimizations
            if arr[i] + arr[i+1] + arr[i+2] > target:
                break
            if arr[i] + arr[n-2] + arr[n-1] <= target:
                rem_len = n - 1 - i
                count += rem_len * (rem_len - 1) // 2
                continue
                
            rem = target - arr[i]
            l, r = i + 1, n - 1
            while l < r:
                if arr[l] + arr[r] <= rem:
                    count += (r - l)
                    l += 1
                else:
                    r -= 1
        return count

    low = arr[0] + arr[1] + arr[2]
    high = arr[n-1] + arr[n-2] + arr[n-3]
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if count_less_equal(mid) >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = kth_triple_sum(arr, k)
    print(result)

if __name__ == "__main__":
    main()
