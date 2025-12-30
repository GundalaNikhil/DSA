def min_inversions_after_swap(arr: list[int]) -> int:
    n = len(arr)
    sorted_arr = sorted(list(set(arr)))
    ranks = {val: i + 1 for i, val in enumerate(sorted_arr)}
    m = len(ranks)
    
    bit = [0] * (m + 2)
    
    def update(i, delta):
        while i <= m:
            bit[i] += delta
            i += i & (-i)
            
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s
        
    initial_inversions = 0
    # Calculate inversions
    for i in range(n - 1, -1, -1):
        rk = ranks[arr[i]]
        initial_inversions += query(rk - 1)
        update(rk, 1)
        
    # Check adjacent swaps for at least reduction of 1
    max_reduction = 0
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            max_reduction = max(max_reduction, 1)
            
    return initial_inversions - max_reduction

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = min_inversions_swap(arr)
    print(result)

if __name__ == "__main__":
    main()
