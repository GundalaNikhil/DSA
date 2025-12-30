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

    def has_edit_distance_1(self, query: str) -> bool:
        return self._dfs(self.root, query, 0, 0)

    def _dfs(self, node: TrieNode, query: str, index: int, edits: int) -> bool:
        if edits > 1:
            return False

        if index == len(query):
            if node.is_end and edits == 1:
                return True
            if edits == 0:
                for child in node.children.values():
                    if child.is_end:
                        return True
            return False

        char = query[index]

        # Match without edit
        if char in node.children:
            if self._dfs(node.children[char], query, index + 1, edits):
                return True

        if edits < 1:
            # Substitution
            for ch, child in node.children.items():
                if ch != char:
                    if self._dfs(child, query, index + 1, edits + 1):
                        return True

            # Deletion from query (insertion)
            if self._dfs(node, query, index + 1, edits + 1):
                return True

            # Insertion into query (deletion)
            for child in node.children.values():
                if self._dfs(child, query, index, edits + 1):
                    return True

        return False

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')

    n = int(lines[0])

    solution = Solution()
    for i in range(1, n + 1):
        solution.insert_word(lines[i].strip())

    query = lines[n + 1].strip()
    result = solution.has_edit_distance_1(query)

    print('true' if result else 'false')

if __name__ == "__main__":
    main()
