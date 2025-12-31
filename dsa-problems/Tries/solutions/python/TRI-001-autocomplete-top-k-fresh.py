import math
from typing import List, Tuple
from collections import defaultdict
import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.metadata = {}  # word -> (frequency, lastUsed)

    def insert_word(self, word: str, frequency: int, timestamp: int):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        self.metadata[word] = (frequency, timestamp)

    def autocomplete(self, prefix: str, current_time: int, D: int, k: int) -> List[str]:
        # Navigate to prefix node
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # Collect all words with this prefix
        matches = []
        self._collect_words(node, prefix, matches)

        # Compute decay scores
        scores = []
        for word in matches:
            freq, last_used = self.metadata[word]
            decay = math.exp(-(current_time - last_used) / D)
            score = freq * decay
            # Negative score for max-heap behavior, word for lexicographic tie-breaking
            scores.append((-score, word))

        # Sort and get top k
        scores.sort()
        result = [word for _, word in scores[:k]]

        return result

    def _collect_words(self, node: TrieNode, prefix: str, result: List[str]):
        if node.is_end_of_word:
            result.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, result)

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    idx = 0

    n = int(input_data[idx])
    idx += 1

    solution = Solution()
    for _ in range(n):
        word = input_data[idx]
        freq = int(input_data[idx + 1])
        time = int(input_data[idx + 2])
        idx += 3
        solution.insert_word(word, freq, time)

    prefix = input_data[idx]
    current_time = int(input_data[idx + 1])
    D = int(input_data[idx + 2])
    k = int(input_data[idx + 3])

    result = solution.autocomplete(prefix, current_time, D, k)
    print(result)

if __name__ == "__main__":
    main()
