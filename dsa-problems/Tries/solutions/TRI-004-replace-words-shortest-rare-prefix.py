def replace_naive(dictionary, sentence):
    words = sentence.split()
    result = []

    for word in words:
        best_root = word
        best_rarity = float('inf')

        for root, rarity in dictionary.items():
            if word.startswith(root):
                if rarity < best_rarity or (rarity == best_rarity and len(root) < len(best_root)):
                    best_root = root
                    best_rarity = rarity

        result.append(best_root)

    return ' '.join(result)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
