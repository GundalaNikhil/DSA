import bisect

def process(arr: list[int], ops: list[list[str]]) -> list[int]:
    n = len(arr)
    block_size = int((n * 0.5) ** 0.5) + 1
    if block_size < 50: block_size = 50
    
    blocks = []
    for i in range(0, n, block_size):
        chunk = arr[i : i + block_size]
        blocks.append(sorted(chunk))
        
    results = []
    
    for op in ops:
        if op[0] == "SET":
            idx = int(op[1])
            val = int(op[2])
            old_val = arr[idx]
            arr[idx] = val
            
            b_idx = idx // block_size
            block = blocks[b_idx]
            
            # Remove old_val (one instance)
            # bisect doesn't remove. list.remove is O(B)
            # We can use bisect to find index to remove faster?
            # list.pop(index) is O(B).
            idx_in_block = bisect.bisect_left(block, old_val)
            block.pop(idx_in_block)
            
            # Insert val
            bisect.insort(block, val)
            
        else:
            l = int(op[1])
            r = int(op[2])
            x = int(op[3])
            y = int(op[4])
            
            count = 0
            start_block = l // block_size
            end_block = r // block_size
            
            if start_block == end_block:
                for i in range(l, r + 1):
                    if x <= arr[i] <= y:
                        count += 1
            else:
                # Left partial
                for i in range(l, (start_block + 1) * block_size):
                    if x <= arr[i] <= y:
                        count += 1
                
                # Full blocks
                for i in range(start_block + 1, end_block):
                    b = blocks[i]
                    # Count in [x, y]
                    # bisect_right(y) - bisect_left(x)
                    upper = bisect.bisect_right(b, y)
                    lower = bisect.bisect_left(b, x)
                    count += (upper - lower)
                    
                # Right partial
                for i in range(end_block * block_size, r + 1):
                    if x <= arr[i] <= y:
                        count += 1
                        
            results.append(count)
            
    return results

def main():
    import sys
    def input_gen():

        for line in sys.stdin:

            for token in line.split():

                yield token

    it = input_gen()
    n = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    ops = []
    for _ in range(q):
        type = next(it)
        if type == "SET":
            ops.append([type, next(it), next(it)])
        else:
            ops.append([type, next(it), next(it), next(it), next(it)])
    
    results = process(arr, ops)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
