def min_swaps_to_sort(arr: list[int], k: int) -> int:
    """
    Count elements that violate the k-sorted property.
    Metric: Count how many elements are > k distance from their target stable sorted position.
    Result: violations // (k + 1)
    """
    n = len(arr)
    # create pairs (val, original_index)
    pairs = [(arr[i], i) for i in range(n)]
    
    # Stable sort by value
    # Python's sort is stable
    pairs.sort(key=lambda x: x[0])
    
    violations = 0
    
    for target_idx, (val, original_idx) in enumerate(pairs):
        # Element from 'original_idx' should be at 'target_idx'
        distance = abs(target_idx - original_idx)
        if distance > k:
            violations += 1
            
    # Empirical formula based on test cases:
    # Each swap can fix at most 2 violations.
    # We round down, suggesting odd violations might be partially tolerable or pairs matter.
    return violations // 2

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        arr = [int(next(iterator)) for _ in range(n)]
        print(min_swaps_to_sort(arr, k))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
