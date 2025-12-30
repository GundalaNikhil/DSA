from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None, None]  # Index 0 for '0', index 1 for '1'
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def find_shortest_absent(self, binary_strings: List[str], L: int) -> str:
        # Early exit if all possible strings exist
        if len(binary_strings) == 2 ** L:
            return ""

        # Build trie
        for s in binary_strings:
            self._insert(s)

        # DFS to find first missing
        return self._dfs(self.root, "", L)

    def _insert(self, s: str):
        node = self.root
        for char in s:
            idx = int(char)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def _dfs(self, node: TrieNode, path: str, L: int) -> str:
        # Reached target length
        if len(path) == L:
            return None if node.is_end else path

        # Try '0' first (lexicographically smaller)
        if node.children[0] is None:
            # Missing '0' path - fill rest with '0's
            return path + '0' * (L - len(path))

        result = self._dfs(node.children[0], path + '0', L)
        if result is not None:
            return result

        # Try '1'
        if node.children[1] is None:
            # Missing '1' path - fill rest with '0's
            return path + '1' + '0' * (L - len(path) - 1)

        return self._dfs(node.children[1], path + '1', L)

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    L = int(lines[0].split()[0])
    n = int(lines[0].split()[1])

    binary_strings = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.find_shortest_absent(binary_strings, L)

    print(result if result else "")

if __name__ == "__main__":
    main()
