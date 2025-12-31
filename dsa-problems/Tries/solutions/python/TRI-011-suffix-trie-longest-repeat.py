class TrieNode:
    def __init__(self):
        self.children = {}
        self.suffix_count = 0  # Number of suffixes passing through this node

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.max_length = 0

    def longest_repeated_substring(self, s: str) -> int:
        # Build suffix trie
        for i in range(len(s)):
            self._insert_suffix(s[i:])

        # Find longest path where suffix_count >= 2
        self._dfs(self.root, 0)
        return self.max_length

    def _insert_suffix(self, suffix: str):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.suffix_count += 1  # Increment count for each suffix passing through

    def _dfs(self, node: TrieNode, depth: int):
        # A repeated substring exists if 2+ suffixes pass through this node
        if node.suffix_count >= 2 and depth > 0:
            self.max_length = max(self.max_length, depth)

        for child in node.children.values():
            self._dfs(child, depth + 1)

def main():
    import sys
    s = sys.stdin.read().strip()

    solution = Solution()
    result = solution.longest_repeated_substring(s)
    print(result)

if __name__ == "__main__":
    main()
