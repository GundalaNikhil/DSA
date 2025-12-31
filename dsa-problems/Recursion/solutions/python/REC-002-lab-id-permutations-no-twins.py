def generate_permutations(s: str) -> list[str]:
    chars = sorted(list(s))
    n = len(chars)
    used = [False] * n
    result = []

    def backtrack(current):
        if len(current) == n:
            result.append("".join(current))
            return

        for i in range(n):
            if used[i]:
                continue
            
            # Skip duplicates
            if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
                continue
            
            # Constraint: No adjacent twins
            if current and current[-1] == chars[i]:
                continue
            
            used[i] = True
            current.append(chars[i])
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    return result


def main():
    import sys
    s = sys.stdin.read().strip()
    if not s:
        return

    perms = generate_permutations(s)
    if perms:
        for perm in perms:
            print(perm)
    else:
        print("NONE")

if __name__ == "__main__":
    main()
