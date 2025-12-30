class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, number: str) -> bool:
        node = self.root
        for char in number:
            if node.is_end:
                return False
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        if len(node.children) > 0:
            return False
        
        node.is_end = True
        return True

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    
    solution = Solution()
    results = []
    for i in range(1, n + 1):
        results.append(solution.insert(lines[i].strip()))
    
    print("[" + ",".join(str(r).lower() for r in results) + "]")

if __name__ == "__main__":
    main()
