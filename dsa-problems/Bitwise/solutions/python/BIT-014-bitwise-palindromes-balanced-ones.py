import sys

def make_palindrome(half, length):
    res = half
    temp = half
    if length % 2 == 1:
        temp >>= 1

    lower = 0
    for _ in range(length // 2):
        lower = (lower << 1) | (temp & 1)
        temp >>= 1

    return (res << (length // 2)) | lower

def count_for_len(N, length, is_limit):
    half_len = (length + 1) // 2
    min_half = 1 << (half_len - 1)
    max_half = (1 << half_len) - 1

    if is_limit:
        prefix = N >> (length - half_len)
        max_half = min(max_half, prefix)

    limit_val = max_half
    valid_below = 0

    if limit_val > min_half:
        if length % 2 == 0:
            valid_below = limit_val - min_half
        else:
            # Count evens in [min_half, limit_val - 1]
            # min_half is even
            valid_below = (limit_val - min_half + 1) // 2

    # Check boundary
    check_boundary = True
    if length % 2 == 1 and (limit_val % 2 != 0):
        check_boundary = False

    if check_boundary:
        p = make_palindrome(limit_val, length)
        # When not at limit, we can construct the full range for the given length
        # When at limit, verify the palindrome doesn't exceed N
        if not is_limit or p <= N:
            valid_below += 1

    return valid_below

def solve(N):
    if N < 0: return 0
    if N == 0: return 1

    L = N.bit_length()
    total = 1 # count 0

    for length in range(1, L):
        total += count_for_len(2**63, length, False)

    total += count_for_len(N, L, True)
    return total

def count_bitwise_palindromes_balanced_ones(L: int, R: int) -> int:
    return solve(R) - solve(L - 1)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return

    L = int(data[0])
    R = int(data[1])

    result = count_bitwise_palindromes_balanced_ones(L, R)
    print(result)

if __name__ == "__main__":
    main()
