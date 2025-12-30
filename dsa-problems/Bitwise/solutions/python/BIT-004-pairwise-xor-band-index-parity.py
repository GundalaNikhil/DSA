import sys

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

def insert(root, num):
    curr = root
    for i in range(29, -1, -1):
        bit = (num >> i) & 1
        if curr.children[bit] is None:
            curr.children[bit] = TrieNode()
        curr = curr.children[bit]
        curr.count += 1

def count_less_equal(root, num, K):
    if K < 0:
        return 0
    curr = root
    count = 0
    for i in range(29, -1, -1):
        if curr is None: break
        bit_num = (num >> i) & 1
        bit_k = (K >> i) & 1

        if bit_k == 1:
            # Case 0 < 1: Add all from "same bit" branch
            if curr.children[bit_num]:
                count += curr.children[bit_num].count
            # Traverse "diff bit" branch
            curr = curr.children[1 - bit_num]
        else:
            # Case 0 == 0: Must match
            curr = curr.children[bit_num]

    if curr:
        count += curr.count
    return count

def solve_for_list(nums, L, U):
    root_u = TrieNode()
    root_l = TrieNode()

    count_u = 0
    count_l = 0

    # Build trie and query for both bounds efficiently
    # For each element, query count with XOR <= U and XOR <= (L-1)
    # The difference gives us count in range [L, U]
    # Insert element after querying to count pairs (i, j) where j > i

    root = TrieNode()
    total = 0
    limit_l = L - 1

    for x in nums:
        c_u = count_less_equal(root, x, U)
        c_l = count_less_equal(root, x, limit_l)
        total += (c_u - c_l)
        insert(root, x)

    return total

def count_pairwise_xor_band_parity(a: list[int], L: int, U: int) -> int:
    evens = a[0::2]
    odds = a[1::2]
    return solve_for_list(evens, L, U) + solve_for_list(odds, L, U)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return

    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1

    L = int(data[ptr]); ptr += 1
    U = int(data[ptr]); ptr += 1

    result = count_pairwise_xor_band_parity(a, L, U)
    print(result)

if __name__ == "__main__":
    main()
