def partial_selection_sort(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    for i in range(k):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = partial_selection_sort(arr, k)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
