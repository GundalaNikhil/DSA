def find_first_occurrence(arr: list[int], x: int) -> int:
    """Find the first occurrence of x in the array"""
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    result = find_first_occurrence(arr, x)
    print(result)

if __name__ == "__main__":
    main()
