def count_within_threshold(arr: list[int], T: int) -> list[int]:
    n = len(arr)
    counts = [0] * n
    pairs = [(arr[i], i) for i in range(n)]
    
    def merge_sort(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr
            
        mid = len(sub_arr) // 2
        left = merge_sort(sub_arr[:mid])
        right = merge_sort(sub_arr[mid:])
        
        # Count step
        q = 0
        for p in range(len(left)):
            threshold = left[p][0] - T
            while q < len(right) and right[q][0] < threshold:
                q += 1
            counts[left[p][1]] += (len(right) - q)
            
        # Merge step
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
        
    merge_sort(pairs)
    return counts

def main():
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    result = count_threshold(arr, t)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
