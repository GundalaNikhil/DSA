from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.node_count = 1  # Start with root

    def count_trie_nodes(self, words: List[str]) -> int:
        for word in words:
            self._insert(word)
        return self.node_count

    def _insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                self.node_count += 1
            node = node.children[char]
        node.is_end = True

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])
    words = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.count_trie_nodes(words)

    print(result)

if __name__ == "__main__":
    main()
