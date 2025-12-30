import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            self.count -= 1

class Solution:
    def count_near_anagram_groups(self, words: list) -> int:
        n = len(words)
        uf = UnionFind(n)
        groups = {}
        
        for i, word in enumerate(words):
            sorted_word = "".join(sorted(word))
            length = len(sorted_word)
            
            # Generate reduced forms
            # Using a set to avoid processing duplicate reduced forms for the same word
            # e.g. "aba" -> remove 'a' -> "ba", remove 'a' -> "ba"
            seen_reduced = set()
            
            for j in range(length):
                reduced = sorted_word[:j] + sorted_word[j+1:]
                if reduced in seen_reduced:
                    continue
                seen_reduced.add(reduced)
                
                if reduced not in groups:
                    groups[reduced] = []
                groups[reduced].append(i)
                
        for indices in groups.values():
            first = indices[0]
            for k in range(1, len(indices)):
                uf.union(first, indices[k])
                
        return uf.count

def count_near_anagram_groups(words: list) -> int:
    solver = Solution()
    return solver.count_near_anagram_groups(words)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        words = []
        for _ in range(n):
            words.append(next(iterator))
            
        print(count_near_anagram_groups(words))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
