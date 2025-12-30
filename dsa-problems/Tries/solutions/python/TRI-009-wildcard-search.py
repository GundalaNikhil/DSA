from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, pattern: str) -> bool:
        return self._dfs(self.root, pattern, 0)

    def _dfs(self, node: TrieNode, pattern: str, index: int) -> bool:
        if index == len(pattern):
            return node.is_end

        char = pattern[index]

        if char == '?':
            # Match any single character
            for child in node.children.values():
                if self._dfs(child, pattern, index + 1):
                    return True
            return False
        elif char == '*':
            # Match zero or more characters
            # Try matching 0 characters
            if self._dfs(node, pattern, index + 1):
                return True
            # Try matching 1+ characters
            for child in node.children.values():
                if self._dfs(child, pattern, index):
                    return True
            return False
        else:
            # Regular character
            if char not in node.children:
                return False
            return self._dfs(node.children[char], pattern, index + 1)

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])

    solution = Solution()
    for i in range(1, n + 1):
        solution.insert_word(lines[i].strip())

    pattern = lines[n + 1].strip()
    result = solution.search(pattern)

    print('true' if result else 'false')

if __name__ == "__main__":
    main()
