import sys

def max_gap_after_removals(seats: list[int], remove_indices: list[int]) -> int:
    n = len(seats)
    removed = [False] * n

    for idx in remove_indices:
        # Bounds check to avoid index errors
        if 0 <= idx < n:
            removed[idx] = True

    max_gap = 0
    last_pos = None

    for i in range(n):
        if not removed[i]:
            current_pos = seats[i]
            if last_pos is not None:
                max_gap = max(max_gap, current_pos - last_pos)
            last_pos = current_pos

    return max_gap

def main():
    n = int(input())
    seats = list(map(int, input().split()))
    r = int(input())
    remove_indices = list(map(int, input().split()))

    result = max_gap_after_removals(seats, remove_indices)
    print(result)

if __name__ == "__main__":
    main()