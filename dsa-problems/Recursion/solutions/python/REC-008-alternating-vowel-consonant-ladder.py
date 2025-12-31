def get_alternating_permutations(s: str) -> list[str]:
    def is_vowel(c):
        return c in 'aeiou'

    results = set()  # Use set to avoid duplicates
    used = [False] * len(s)

    def backtrack(current):
        if len(current) == len(s):
            results.add(current)
            return
        for i in range(len(s)):
            if not used[i]:
                if len(current) == 0 or is_vowel(current[-1]) != is_vowel(s[i]):
                    used[i] = True
                    backtrack(current + s[i])
                    used[i] = False

    backtrack("")
    return sorted(list(results))

def main():
    import sys
    s = sys.stdin.read().strip()
    results = get_alternating_permutations(s)
    if results:
        for perm in results:
            print(perm)
    else:
        print("NONE")

if __name__ == "__main__":
    main()
