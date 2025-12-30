def find_subset(arr: list[int], k: int, target: int) -> list[int]:
    n = len(arr)
    result = []

    def backtrack(index, count, current_sum):
        if count == k:
            return current_sum == target
        
        if index == n:
            return False
        
        # Pruning
        if n - index < k - count:
            return False

        # Option 1: Include
        result.append(arr[index])
        if backtrack(index + 1, count + 1, current_sum + arr[index]):
            return True
        result.pop()

        # Option 2: Exclude
        if backtrack(index + 1, count, current_sum):
            return True
            
        return False

    if backtrack(0, 0, 0):
        return result
    return []


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
