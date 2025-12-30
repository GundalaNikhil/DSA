def stable_sort(records: list[list[int]]) -> list[list[int]]:
    # Python's sort is stable (Timsort)
    # We can use a tuple key. For descending key2, we can negate it.
    records.sort(key=lambda x: (x[0], -x[1]))
    return records

def main():
    n = int(input())
    records = []
    for _ in range(n):
        k1, k2 = map(int, input().split())
        records.append([k1, k2])

    result = stable_sort(records)
    for k1, k2 in result:
        print(k1, k2)

if __name__ == "__main__":
    main()
