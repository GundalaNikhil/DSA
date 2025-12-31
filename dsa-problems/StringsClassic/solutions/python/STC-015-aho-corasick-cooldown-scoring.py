import sys
import collections

# Increase recursion depth
sys.setrecursionlimit(200000)

class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = None
        self.patterns = [] # List of (len, weight) for Cooldown / List of indices/counts for Counting

def build_aho_corasick(patterns, weights=None):
    root = Node()
    for i, p in enumerate(patterns):
        curr = root
        for char in p:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        w = weights[i] if weights else 1
        curr.patterns.append((len(p), w))
    
    queue = collections.deque()
    for char, node in root.children.items():
        node.fail = root
        queue.append(node)
        
    while queue:
        curr = queue.popleft()
        if curr.fail.patterns:
            curr.output = curr.fail
        else:
            curr.output = curr.fail.output
            
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if char in curr.children:
                child = curr.children[char]
                child.fail = curr.fail.children.get(char, root)
                queue.append(child)
            else:
                curr.children[char] = curr.fail.children.get(char, root)
                
    return root

def solve_cooldown(text, patterns, weights, g):
    root = build_aho_corasick(patterns, weights)
    n = len(text)
    dp = [0] * (n + 1)
    curr = root
    
    for i in range(n):
        curr = curr.children.get(text[i], root)
        dp[i + 1] = dp[i]
        
        temp = curr
        while temp != root and temp is not None:
            for length, weight in temp.patterns:
                check_idx = i - length - g + 1
                prev_score = dp[check_idx] if check_idx >= 0 else 0
                if prev_score + weight > dp[i + 1]:
                    dp[i + 1] = prev_score + weight
            temp = temp.output
            
    return dp[n]

def solve_counting(text, patterns):
    root = build_aho_corasick(patterns)
    curr = root
    count = 0
    
    for char in text:
        curr = curr.children.get(char, root)
        
        # Sum matches at this position
        temp = curr
        while temp != root and temp is not None:
            count += len(temp.patterns)
            temp = temp.output
            
    return count

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # Check format
    # MD: k (int) ...
    # YAML: text (string) ...
    
    first_token = input_data[0]
    
    is_md_format = False
    try:
        k = int(first_token)
        is_md_format = True
    except ValueError:
        is_md_format = False
        
    iter_data = iter(input_data)
    
    if is_md_format:
        try:
            k = int(next(iter_data))
            patterns = []
            weights = []
            for _ in range(k):
                patterns.append(next(iter_data))
                weights.append(int(next(iter_data)))
            g = int(next(iter_data))
            text = next(iter_data)
            print(solve_cooldown(text, patterns, weights, g))
        except StopIteration:
            pass
    else:
        # YAML Format: Text, k, patterns...
        try:
            text = next(iter_data)
            k = int(next(iter_data))
            patterns = []
            for _ in range(k):
                patterns.append(next(iter_data))
            
            print(solve_counting(text, patterns))
        except StopIteration:
            pass

if __name__ == "__main__":
    main()
