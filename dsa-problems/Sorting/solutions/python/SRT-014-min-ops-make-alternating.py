from collections import Counter

def min_changes(arr: list[int]) -> int:
    n = len(arr)
    if n <= 1:
        return 0
        
    even_counts = Counter(arr[i] for i in range(0, n, 2))
    odd_counts = Counter(arr[i] for i in range(1, n, 2))
    
    def get_top_two(counts):
        # Returns [(val, count), (val, count)]
        # Add dummy values to ensure at least 2 elements
        most = counts.most_common(2)
        if not most:
            return [(-1, 0), (-1, 0)]
        if len(most) == 1:
            return [most[0], (-1, 0)]
        return most
        
    e_top = get_top_two(even_counts)
    o_top = get_top_two(odd_counts)
    
    e1_val, e1_count = e_top[0]
    e2_val, e2_count = e_top[1]
    o1_val, o1_count = o_top[0]
    o2_val, o2_count = o_top[1]
    
    if e1_val != o1_val:
        return n - (e1_count + o1_count)
    else:
        opt1 = n - (e1_count + o2_count)
        opt2 = n - (e2_count + o1_count)
        return min(opt1, opt2)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = min_ops(arr)
    print(result)

if __name__ == "__main__":
    main()
