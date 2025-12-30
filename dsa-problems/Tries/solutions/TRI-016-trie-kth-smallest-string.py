from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}  # Will maintain alphabetical order through sorted()
        self.is_end = False
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.result = ""
        self.remaining = 0

    def kth_smallest(self, words: List[str], k: int) -> str:
        # Build trie with counts
        for word in words:
            self._insert(word)

        self.remaining = k
        self._dfs(self.root, [])

        return self.result

    def _insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True

    def _dfs(self, node: TrieNode, path: List[str]) -> bool:
        if node.is_end:
            self.remaining -= 1
            if self.remaining == 0:
                self.result = ''.join(path)
                return True

        # Traverse children in alphabetical order
        for char in sorted(node.children.keys()):
            child = node.children[char]

            if child.count >= self.remaining:
                path.append(char)
                if self._dfs(child, path):
                    return True
                path.pop()
            else:
                self.remaining -= child.count

        return False

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n, k = map(int, lines[0].split())
    words = [lines[i+1].strip() for i in range(n)]

    solution = Solution()
    result = solution.kth_smallest(words, k)

    print(result if result else "")

if __name__ == "__main__":
    main()
