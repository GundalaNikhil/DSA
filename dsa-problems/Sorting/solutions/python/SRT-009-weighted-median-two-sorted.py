def weighted_median(A: list[int], B: list[int], wA: int, wB: int) -> str:
    n = len(A)
    m = len(B)
    total = n * wA + m * wB
    
    def upper_bound(arr, val):
        l, r = 0, len(arr) - 1
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= val:
                res = mid + 1
                l = mid + 1
            else:
                r = mid - 1
        return res

    def count_less_equal(val):
        c = 0
        c += upper_bound(A, val) * wA
        c += upper_bound(B, val) * wB
        return c

    def find_kth(k):
        low, high = -2 * 10**9, 2 * 10**9
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if count_less_equal(mid) > k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    if total % 2 == 1:
        val = find_kth(total // 2)
        return str(val)
    else:
        val1 = find_kth(total // 2 - 1)
        val2 = find_kth(total // 2)
        s = val1 + val2
        if s % 2 == 0:
            return str(s // 2)
        else:
            return f"{s // 2}.5"

def main():
    n, wa = map(int, input().split())
    a = list(map(int, input().split()))
    m, wb = map(int, input().split())
    b = list(map(int, input().split()))
    result = weighted_median(a, b, wa, wb)
    print(result)

if __name__ == "__main__":
    main()
