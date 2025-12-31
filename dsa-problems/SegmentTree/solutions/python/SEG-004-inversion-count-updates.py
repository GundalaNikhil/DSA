import bisect

def process(arr: list[int], updates: list[tuple[int, int]]) -> list[int]:
    n = len(arr)
    # Heuristic block size
    block_size = int((n * 0.5) ** 0.5) + 1
    if block_size < 50: block_size = 50
    
    blocks = []
    for i in range(0, n, block_size):
        chunk = arr[i : i + block_size]
        blocks.append(sorted(chunk))
        
    # Initial inversions
    def count_inversions(a):
        res = 0
        temp = [0] * len(a)
        def merge_sort(left, right):
            nonlocal res
            if left >= right: return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            
            i, j, k = left, mid + 1, left
            while i <= mid and j <= right:
                if a[i] <= a[j]:
                    temp[k] = a[i]
                    i += 1
                else:
                    temp[k] = a[j]
                    j += 1
                    res += (mid - i + 1)
                k += 1
            while i <= mid:
                temp[k] = a[i]
                i += 1
                k += 1
            while j <= right:
                temp[k] = a[j]
                j += 1
                k += 1
            for x in range(left, right + 1):
                a[x] = temp[x]
                
        merge_sort(0, len(a) - 1)
        return res

    current_inversions = count_inversions(list(arr))
    results = []
    
    for idx, val in updates:
        old_val = arr[idx]
        if val == old_val:
            results.append(current_inversions)
            continue
            
        b_idx = idx // block_size
        
        # Remove old_val contribution
        # Left blocks
        for i in range(b_idx):
            b = blocks[i]
            # Count > old_val
            pos = bisect.bisect_right(b, old_val)
            current_inversions -= (len(b) - pos)
            
        # Left in same block
        start = b_idx * block_size
        for i in range(start, idx):
            if arr[i] > old_val:
                current_inversions -= 1
                
        # Right in same block
        end = min((b_idx + 1) * block_size, n)
        for i in range(idx + 1, end):
            if arr[i] < old_val:
                current_inversions -= 1
                
        # Right blocks
        for i in range(b_idx + 1, len(blocks)):
            b = blocks[i]
            # Count < old_val
            pos = bisect.bisect_left(b, old_val)
            current_inversions -= pos
            
        # Update
        arr[idx] = val
        block = blocks[b_idx]
        # Remove one instance of old_val
        # bisect doesn't remove, list.remove is O(B)
        block.remove(old_val)
        bisect.insort(block, val)
        
        # Add val contribution
        # Left blocks
        for i in range(b_idx):
            b = blocks[i]
            pos = bisect.bisect_right(b, val)
            current_inversions += (len(b) - pos)
            
        # Left in same block
        for i in range(start, idx):
            if arr[i] > val:
                current_inversions += 1
                
        # Right in same block
        for i in range(idx + 1, end):
            if arr[i] < val:
                current_inversions += 1
                
        # Right blocks
        for i in range(b_idx + 1, len(blocks)):
            b = blocks[i]
            pos = bisect.bisect_left(b, val)
            current_inversions += pos
            
        results.append(current_inversions)
        
    return results

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    updates = []
    for _ in range(q):
        op = next(it) # SET
        updates.append((int(next(it)), int(next(it))))
    
    results = process(arr, updates)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
