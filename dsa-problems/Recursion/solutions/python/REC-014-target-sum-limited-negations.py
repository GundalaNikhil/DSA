def count_assignments(nums: list[int], K: int, target: int) -> int:
    n = len(nums)

    def backtrack(index, current_sum, negations):
        if index == n:
            return 1 if current_sum == target else 0
        
        count = 0
        
        # Option 1: +
        count += backtrack(index + 1, current_sum + nums[index], negations)
        
        # Option 2: -
        if negations < K:
            count += backtrack(index + 1, current_sum - nums[index], negations + 1)
            
        return count

    return backtrack(0, 0, 0)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
