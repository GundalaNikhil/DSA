from collections import deque, defaultdict

def ladders(start: str, end: str, dict_words: list[str]) -> list[list[str]]:
    word_set = set(dict_words)
    word_set.add(start)
    word_set.add(end)
    
    def is_vowel(c):
        return c in 'aeiou'
    
    def is_alternating(w1, w2):
        return is_vowel(w1[0]) != is_vowel(w2[0])
    
    def get_neighbors(word):
        neighbors = []
        chars = list(word)
        for i in range(len(chars)):
            original = chars[i]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == original: continue
                chars[i] = c
                new_word = "".join(chars)
                if new_word in word_set and is_alternating(word, new_word):
                    neighbors.append(new_word)
            chars[i] = original
        return neighbors

    # BFS
    parents = defaultdict(list)
    dist = {start: 0}
    queue = deque([start])
    found = False
    
    while queue and not found:
        level_size = len(queue)
        level_visited = set()
        
        for _ in range(level_size):
            curr = queue.popleft()
            if curr == end:
                found = True
            
            cur_dist = dist[curr]
            
            # Optimization: Precompute adjacency or generate on fly
            # Generating on fly is O(26 * L), iterating dict is O(M * L)
            # Given M=3000, L=6, M*L is better than 26*L? No.
            # But checking adjacency against all M is O(M*L). 26*L is small constant.
            # However, we need to check if generated word is in dict.
            
            for neighbor in get_neighbors(curr):
                if neighbor not in dist:
                    if neighbor not in level_visited:
                        dist[neighbor] = cur_dist + 1
                        queue.append(neighbor)
                        level_visited.add(neighbor)
                    parents[neighbor].append(curr)
                elif dist[neighbor] == cur_dist + 1:
                    parents[neighbor].append(curr)
                    
    results = []
    if found:
        def backtrack(curr, path):
            if curr == start:
                results.append(path[::-1])
                return
            for p in parents[curr]:
                path.append(p)
                backtrack(p, path)
                path.pop()
        
        backtrack(end, [end])
        
    results.sort()
    return results


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
