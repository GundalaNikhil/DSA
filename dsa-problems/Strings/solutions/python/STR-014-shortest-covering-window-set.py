def shortest_covering_window(arr: list[str], T: set[str]) -> tuple[int, list[str]]:
    if not arr or not T:
        return (0, [])

    required = {s: 1 for s in T}
    window_counts = {}

    left = 0
    formed = 0  # Unique T elements covered
    min_len = float('inf')
    result_left, result_right = 0, 0

    for right in range(len(arr)):
        char = arr[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if this char is in T and newly covered
        if char in required and window_counts[char] == 1:
            formed += 1

        # Contract window while all elements covered
        while formed == len(T) and left <= right:
            # Update result if better
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result_left, result_right = left, right

            # Remove leftmost element
            left_char = arr[left]
            window_counts[left_char] -= 1
            if left_char in required and window_counts[left_char] == 0:
                formed -= 1

            left += 1

    if min_len == float('inf'):
        return (0, [])

    return (min_len, arr[result_left:result_right + 1])


def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    parts = input_data.split()
    if not parts:
        return

    iterator = iter(parts)
    try:
        # Read Array
        N = int(next(iterator))
        arr = []
        for _ in range(N):
            arr.append(next(iterator))
            
        # Read Set T
        K = int(next(iterator))
        T = set()
        for _ in range(K):
            T.add(next(iterator))
            
        length, window = shortest_covering_window(arr, T)
        
        print(length)
        for item in window:
            print(item)
            
    except StopIteration:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    main()
