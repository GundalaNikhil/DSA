class TrieNode:
    def __init__(self):
        self.children = {}
        self.strings = []  # Strings passing through this node

def minimal_removal_unique_prefixes(L: int, strings: list[str]) -> int:
    # Build trie with all strings
    root = TrieNode()

    for s in strings:
        node = root
        for i, c in enumerate(s):
            if i == L:  # Only care about first L characters
                break
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.strings.append(s)

    # Find conflicts at depth L
    total_deletions = 0

    def find_conflicts(node, depth):
        nonlocal total_deletions

        if depth == L:
            # Check if multiple strings at this node (conflict)
            if len(node.strings) > 1:
                # Keep longest, delete others
                node.strings.sort(key=lambda x: -len(x))
                for s in node.strings[1:]:
                    # Delete to length L-1 (so prefix length < L)
                    if len(s) >= L:
                        total_deletions += len(s) - (L - 1)
            return

        for child in node.children.values():
            find_conflicts(child, depth + 1)

    find_conflicts(root, 0)
    return total_deletions


def main():
    import sys


    # Read input
    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return
        
    parts = input_data.split()
    if not parts:
        return
        
    iterator = iter(parts)
    try:
        L = int(next(iterator))
        N = int(next(iterator))
        strings = []
        for _ in range(N):
            strings.append(next(iterator))
            
        print(minimal_removal_unique_prefixes(L, strings))
    except StopIteration:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    main()
