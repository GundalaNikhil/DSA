from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_ids = set()

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.longest_prefix = ""

    def longest_common_prefix_after_one_deletion(self, words: List[str]) -> str:
        n = len(words)

        # Insert all variants into trie
        for word_id, word in enumerate(words):
            # Insert original word
            self._insert_word(word, word_id)

            # Insert all single-deletion variants
            for i in range(len(word)):
                variant = word[:i] + word[i+1:]
                self._insert_word(variant, word_id)

        # DFS to find longest prefix with all word IDs
        self._dfs(self.root, "", n)

        return self.longest_prefix

    def _insert_word(self, word: str, word_id: int):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_ids.add(word_id)

    def _dfs(self, node: TrieNode, prefix: str, total_words: int):
        # If all words are represented at this node, update longest prefix
        if len(node.word_ids) == total_words:
            if len(prefix) > len(self.longest_prefix):
                self.longest_prefix = prefix

        # Continue DFS
        for char, child in node.children.items():
            self._dfs(child, prefix + char, total_words)

def main():
    import sys
    input_data = sys.stdin.read().strip().split()

    n = int(input_data[0])
    words = input_data[1:n+1]

    solution = Solution()
    result = solution.longest_common_prefix_after_one_deletion(words)

    print(result)

if __name__ == "__main__":
    main()
