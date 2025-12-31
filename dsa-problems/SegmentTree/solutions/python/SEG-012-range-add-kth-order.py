import sys
from bisect import bisect_right

def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    n = len(arr)
    # Heuristic block size
    block_size = int((n * 10) ** 0.5) # Slightly larger block size
    if block_size < 100: block_size = 100
    
    blocks = []
    # Each block: [sorted_vals, lazy]
    # We also need original arr updated lazily?
    
    # Initialize blocks
    for i in range(0, n, block_size):
        chunk = arr[i : i + block_size]
        blocks.append([sorted(chunk), 0])
        
    results = []
    
    def update(l, r, x):
        start_block = l // block_size
        end_block = r // block_size
        
        if start_block == end_block:
            # Partial
            b = blocks[start_block]
            # Push lazy to arr
            if b[1] != 0:
                for i in range(start_block * block_size, min(n, (start_block + 1) * block_size)):
                    arr[i] += b[1]
                b[1] = 0
            
            # Update arr
            for i in range(l, r + 1):
                arr[i] += x
                
            # Rebuild sorted
            chunk = arr[start_block * block_size : min(n, (start_block + 1) * block_size)]
            b[0] = sorted(chunk)
            
        else:
            # Start partial
            b = blocks[start_block]
            if b[1] != 0:
                for i in range(start_block * block_size, (start_block + 1) * block_size):
                    arr[i] += b[1]
                b[1] = 0
            for i in range(l, (start_block + 1) * block_size):
                arr[i] += x
            b[0] = sorted(arr[start_block * block_size : (start_block + 1) * block_size])
            
            # Middle full
            for i in range(start_block + 1, end_block):
                blocks[i][1] += x
                
            # End partial
            b = blocks[end_block]
            if b[1] != 0:
                for i in range(end_block * block_size, min(n, (end_block + 1) * block_size)):
                    arr[i] += b[1]
                b[1] = 0
            for i in range(end_block * block_size, r + 1):
                arr[i] += x
            b[0] = sorted(arr[end_block * block_size : min(n, (end_block + 1) * block_size)])

    def count_le(l, r, val):
        count = 0
        start_block = l // block_size
        end_block = r // block_size
        
        if start_block == end_block:
            lazy = blocks[start_block][1]
            for i in range(l, r + 1):
                if arr[i] + lazy <= val:
                    count += 1
        else:
            lazy = blocks[start_block][1]
            for i in range(l, (start_block + 1) * block_size):
                if arr[i] + lazy <= val:
                    count += 1
            
            for i in range(start_block + 1, end_block):
                b = blocks[i]
                target = val - b[1]
                count += bisect_right(b[0], target)
                
            lazy = blocks[end_block][1]
            for i in range(end_block * block_size, r + 1):
                if arr[i] + lazy <= val:
                    count += 1
        return count

    for op in ops:
        if op[0] == "ADD":
            update(int(op[1]), int(op[2]), int(op[3]))
        else:
            l, r, k = int(op[1]), int(op[2]), int(op[3])
            low = -2 * 10**14
            high = 2 * 10**14
            ans = high
            
            while low <= high:
                mid = (low + high) // 2
                if count_le(l, r, mid) >= k:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            results.append(ans)
            
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
    ops = []
    for _ in range(q):
        type = next(it)
        if type == "ADD":
            ops.append([type, next(it), next(it), next(it)])
        else:
            ops.append([type, next(it), next(it), next(it)])
    
    results = process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
