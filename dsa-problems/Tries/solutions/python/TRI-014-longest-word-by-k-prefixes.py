from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def longest_word_with_k_prefixes(self, words: List[str], k: int) -> str:
        # Build trie
        for word in words:
            self._insert(word)

        result = ""
        max_len = 0

        # Check each word
        for word in words:
            prefix_count = self._count_prefixes(word)
            if prefix_count >= k:
                # Update if longer or same length but lexicographically smaller
                if len(word) > max_len or (len(word) == max_len and word < result):
                    result = word
                    max_len = len(word)

        return result

    def _insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def _count_prefixes(self, word: str) -> int:
        node = self.root
        count = 0

        for i, char in enumerate(word):
            node = node.children[char]
            # Count END markers excluding the final position
            if i < len(word) - 1 and node.is_end:
                count += 1

        return count

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n, k = map(int, lines[0].split())
    words = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.longest_word_with_k_prefixes(words, k)

    print(result if result else "")

if __name__ == "__main__":
    main()
