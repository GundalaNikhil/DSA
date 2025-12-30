def min_swaps_to_sort(arr: list[int]) -> int:
    n = len(arr)
    # Create pairs (value, original_index)
    pairs = [(arr[i], i) for i in range(n)]
    
    # Sort pairs to know where each element belongs
    # If duplicates exist, Python's stable sort preserves relative order
    # which is optimal for minimizing swaps (don't swap identicals)
    pairs.sort(key=lambda x: x[0])
    
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        if visited[i] or pairs[i][1] == i:
            continue
            
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            # The element that belongs at j is currently at pairs[j][1]
            # This forms the cycle j -> pairs[j][1] -> ...
            j = pairs[j][1]
            cycle_size += 1
            
        if cycle_size > 0:
            swaps += (cycle_size - 1)
            
    return swaps

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = min_swaps_k_sorted(arr, k)
    print(result)

if __name__ == "__main__":
    main()
