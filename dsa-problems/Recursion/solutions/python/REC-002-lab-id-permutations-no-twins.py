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
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
