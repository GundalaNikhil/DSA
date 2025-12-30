from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution:
    MAX_BITS = 30

    def __init__(self):
        self.root = TrieNode()

    def minimize_xor(self, a: List[int], X: int) -> int:
        n = len(a)
        prefix = [0] * (n + 1)

        # Compute prefix XORs
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ a[i]

        min_xor = float('inf')

        # Process each prefix
        for j in range(n + 1):
            if self.root.children[0] is not None or self.root.children[1] is not None:
                # Query for best match
                target = prefix[j] ^ X
                closest = self._query(target)
                min_xor = min(min_xor, closest ^ target)
            # Insert current prefix
            self._insert(prefix[j])

        return min_xor

    def _insert(self, num: int):
        node = self.root
        for i in range(self.MAX_BITS, -1, -1):
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def _query(self, num: int) -> int:
        node = self.root
        result = 0

        for i in range(self.MAX_BITS, -1, -1):
            bit = (num >> i) & 1

            # Prefer same bit (to minimize XOR)
            if node.children[bit] is not None:
                node = node.children[bit]
            else:
                # Take opposite bit
                result |= (1 << i)
                node = node.children[1 - bit]

        return result

def main():
    import sys
    input_data = sys.stdin.read().strip().split()

    n = int(input_data[0])
    X = int(input_data[1])
    a = [int(input_data[i + 2]) for i in range(n)]

    solution = Solution()
    result = solution.minimize_xor(a, X)

    print(result)

if __name__ == "__main__":
    main()
