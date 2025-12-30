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
    input_data = sys.stdin.read().strip().split('\n')

    n = int(input_data[0])
    dictionary = {}
    for i in range(1, n + 1):
        parts = input_data[i].rsplit(' ', 1)
        root = parts[0]
        rarity = int(parts[1])
        dictionary[root] = rarity

    sentence = input_data[n + 1]
    result = replace_naive(dictionary, sentence)
    print(result)

if __name__ == "__main__":
    main()
