from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def find_minimum_prefix_lengths(self, words: List[str]) -> List[int]:
        # Build trie with counts
        for word in words:
            self._insert(word)

        # Find minimum prefix length for each word
        result = []
        for word in words:
            result.append(self._find_min_length(word))

        return result

    def _insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True

    def _find_min_length(self, word: str) -> int:
        node = self.root
        for i, char in enumerate(word):
            node = node.children[char]
            if node.count == 1:
                return i + 1
        return len(word)

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])
    words = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.find_minimum_prefix_lengths(words)

    print("[" + ",".join(map(str, result)) + "]")

if __name__ == "__main__":
    main()
