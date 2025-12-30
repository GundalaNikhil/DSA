import sys

def shuttle_shift_blackout(arr: list[int], k: int, blackout: set[int]) -> list[int]:
    """
    Left rotate non-blackout elements by k.
    """
    valid_indices = [i for i in range(len(arr)) if i not in blackout]
    
    if not valid_indices:
        return arr
        
    values = [arr[i] for i in valid_indices]
    count = len(values)
    k %= count
    
    # Left rotate list
    # values[k:] + values[:k] gives elements shifted left
    rotated_values = values[k:] + values[:k]
    
    # Write back
    for i, val in zip(valid_indices, rotated_values):
        arr[i] = val
        
    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    b = int(input())
    blackout = set(map(int, input().split())) if b > 0 else set()

    result = shuttle_shift_blackout(arr, k, blackout)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

