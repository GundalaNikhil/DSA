def expressions(s: str, target: int, max_ops: int) -> list[str]:
    results = []
    n = len(s)

    def backtrack(index, current_val, ops_count, flip_used, current_expr):
        if index == n:
            if current_val == target:
                results.append(current_expr)
            return

        for i in range(index, n):
            # Leading zero check
            if i > index and s[index] == '0':
                break
            
            sub = s[index : i+1]
            val = int(sub)

            if index == 0:
                # First term
                # Normal
                backtrack(i + 1, val, 0, flip_used, sub)
                # Flip
                if not flip_used:
                    backtrack(i + 1, -val, 0, True, "-" + sub)
            else:
                if ops_count < max_ops:
                    # +
                    backtrack(i + 1, current_val + val, ops_count + 1, flip_used, current_expr + "+" + sub)
                    if not flip_used:
                        backtrack(i + 1, current_val - val, ops_count + 1, True, current_expr + "+-" + sub)
                    
                    # -
                    backtrack(i + 1, current_val - val, ops_count + 1, flip_used, current_expr + "-" + sub)
                    if not flip_used:
                        backtrack(i + 1, current_val + val, ops_count + 1, True, current_expr + "--" + sub)

    backtrack(0, 0, 0, False, "")
    return sorted(results)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
