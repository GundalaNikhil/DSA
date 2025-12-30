class Node:
    def __init__(self, length, link):
        self.len = length
        self.link = link
        self.next = {}

def count_distinct_palindromes(s: str) -> int:
    # Node 0: len -1 (odd root), link 0
    # Node 1: len 0 (even root), link 0
    tree = [Node(-1, 0), Node(0, 0)]
    last = 1
    n = len(s)
    
    for i in range(n):
        char_code = s[i]
        curr = last
        
        # Find node to extend
        while True:
            length = tree[curr].len
            if i - 1 - length >= 0 and s[i - 1 - length] == char_code:
                break
            curr = tree[curr].link
            
        if char_code in tree[curr].next:
            last = tree[curr].next[char_code]
            continue
            
        # Create new node
        new_node_idx = len(tree)
        tree.append(Node(tree[curr].len + 2, 0))
        tree[curr].next[char_code] = new_node_idx
        
        # Find suffix link
        if tree[new_node_idx].len == 1:
            tree[new_node_idx].link = 1
        else:
            temp = tree[curr].link
            while True:
                length = tree[temp].len
                if i - 1 - length >= 0 and s[i - 1 - length] == char_code:
                    break
                temp = tree[temp].link
            tree[new_node_idx].link = tree[temp].next[char_code]
            
        last = new_node_idx
        
    return len(tree) - 2

def main():
    import sys
sys.setrecursionlimit(200000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    print(count_distinct_palindromes(s))

if __name__ == "__main__":
    main()