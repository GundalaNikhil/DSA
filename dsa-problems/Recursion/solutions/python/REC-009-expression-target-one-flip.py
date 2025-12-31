def find_flip_index(nums: list[int], ops: str, target: int) -> int:
    for flip_idx in range(len(ops)):
        current_sum = nums[0]
        for i in range(len(ops)):
            if i == flip_idx:
                op = '-' if ops[i] == '+' else '+'
            else:
                op = ops[i]
            if op == '+':
                current_sum += nums[i + 1]
            else:
                current_sum -= nums[i + 1]
        if current_sum == target:
            return flip_idx
    return -1

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    if len(lines) < 4:
        return
    n = int(lines[0].strip())
    nums = list(map(int, lines[1].split()))
    ops = lines[2].strip()
    target = int(lines[3].strip())
    result = find_flip_index(nums, ops, target)
    print(result)

if __name__ == "__main__":
    main()
