import sys

sys.setrecursionlimit(300000)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


def insert(root, word):
    curr = root
    for char in word:
        if char not in curr.children:
            curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.is_word = True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


def insert(root, word):
    curr = root
    for char in word:
        if char not in curr.children:
            curr.children[char] = TrieNode()
        curr = curr.children[char]
    curr.is_word = True


memo = {}
def get_max_chain(node, dict_root):
    if node in memo:
        return memo[node]
        
    max_len = 0
    # Current node represents some prefix.
    # If this prefix matches a dictionary word (is_word), it can be part of chain.
    # But wait, problem is "Longest Dictionary Chain Suffix Validated".
    # Logic in original:
    # max_len = 1 if node.is_word else 0 (?)
    # recurses on children.
    
    # Actually, original code:
    # max_len = 1 if node.is_word else 0
    # if node.is_word: ... child_max = max(... get_max_chain(child)) ... max_len += child_max
    
    # This implies chain length = 1 (self) + max(child_chain) IF self is a word?
    # So we can only step from a word to another word?
    # This looks like "Find longest path in Trie where every node is a word"?
    # Suffix validated? The inputs were `dict_words` and `suffix_roots`.
    # And validation: `w[j:] not in suffix_roots`.
    # After validation, we build a Trie of VALID words.
    # Then we want longest chain.
    
    child_max = 0
    if node.is_word:
        # We can continue chain from here to children
        for char in node.children.values(): # iterate nodes
             child_max = max(child_max, get_max_chain(char, dict_root))
        max_len = 1 + child_max
    else:
        # If not a word, we can't be part of the chain?
        # Or can we pass through?
        # Original code line 70: else: pass.
        # So if not word, max_len is 0.
        # But we must traverse children to find words?
        # If I am root (not word), I should check children?
        # Typically "Chain" implies Words W1, W2... where W2 extends W1.
        # Trie path: Root -> ... -> W1 -> ... -> W2.
        # If Root is not a word, we can start chain at W1.
        # So if not word, max_len = max(children_max_chains)?
        # BUT original code returns 0 if not word?
        # "max_len = 1 if node.is_word else 0".
        # Then returns max_len.
        # This implies we ONLY count chains starting at this node if it is a word.
        # AND it only recurses if `node.is_word`.
        # This seems wrong. We should be able to pass through non-word nodes to find words deeper.
        # UNLESS the chain must feature consecutive characters?
        # "Dictionary Chain": usually word A is prefix of word B.
        # If we skip nodes, we still follow prefix property.
        # So Root -> A (word) -> B (word). Chain len 2.
        # A's children contain B.
        # We must recurse on ALL children to find starts?
        pass
        
    # Let's fix recursion to search properly.
    # If this node is NOT a word, we just want max(children).
    # If this node IS a word, we want 1 + max(children).
    
    # Original code logic was suspiciously broken/weird.
    # Let's implement standard "Longest Chain in Trie" logic.
    
    res = 0
    sub_max = 0
    for char, child in node.children.items():
        sub_max = max(sub_max, get_max_chain(child, dict_root))
        
    if node.is_word:
        res = 1 + sub_max
    else:
        res = sub_max
        
    memo[node] = res
    return res


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    
    dict_words = []
    for _ in range(n):
        dict_words.append(input_data[ptr])
        ptr += 1
        
    suffix_roots = set()
    for _ in range(m):
        suffix_roots.add(input_data[ptr])
        ptr += 1
        
    valid_dict_words = []
    for w in dict_words:
        is_valid = True
        # "Suffix Validated": check purely if suffixes are in `suffix_roots`?
        # Original: `for j in range(len(w)): if w[j:] not in suffix_roots: is_valid = False`
        # This means ALL suffixes of w must be in `suffix_roots`.
        for j in range(len(w)):
            if w[j:] not in suffix_roots:
                is_valid = False
                break
        if is_valid:
            valid_dict_words.append(w)
            
    if not valid_dict_words:
        print(0)
        return
        
    dict_root = TrieNode()
    for w in valid_dict_words:
        insert(dict_root, w)
        
    # Memoization reset
    global memo
    memo = {}
    
    # Find max chain
    # The chain must strictly follow Trie structure.
    # So we just need depth of "word nodes" in the Trie tree.
    # Longest path of "is_word" nodes.
    # W1 -> W2 -> W3... where W1 prefix of W2...
    
    ans = get_max_chain(dict_root, dict_root)
    # Note: Root is empty string, usually not is_word.
    # get_max_chain(root) will return max(children).
    
    print(ans)
