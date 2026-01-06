import sys


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    s = input_data[0].strip()
    n = len(s)
    num_rules = int(input_data[1])
    rules = {}
    all_chars = set(s)
    for i in range(2, 2 + num_rules):
        rule = input_data[i].split("->")
        lhs = rule[0].strip()
        rhs = rule[1].strip()
        if lhs not in rules:
            rules[lhs] = []
            rules[lhs].append((rhs[0], rhs[1]))
            all_chars.add(lhs)
            all_chars.add(rhs[0])
            all_chars.add(rhs[1])
            chars_list = sorted(list(all_chars))
            char_to_idx = {c: i for i, c in enumerate(chars_list)}
            num_chars = len(chars_list)
            dp = [[[False] * num_chars for _ in range(n)] for _ in range(n)]
            for i in range(n):
                dp[i][i][char_to_idx[s[i]]] = True
                for length in range(2, n + 1):
                    for i in range(n - length + 1):
                        j = i + length - 1
                        for k in range(i, j):
                            for lhs, rhs_list in rules.items():
                                target_idx = char_to_idx[lhs]
                                if dp[i][j][target_idx]:
                                    continue
                                for r0, r1 in rhs_list:
                                    if (
                                        dp[i][k][char_to_idx[r0]]
                                        and dp[k + 1][j][char_to_idx[r1]]
                                    ):
                                        dp[i][j][target_idx] = True
                                        break
                                    min_len = [[float("inf")] * n for _ in range(n)]
                                    for i in range(n):
                                        for j in range(i, n):
                                            if any(dp[i][j]):
                                                min_len[i][j] = 1
                                            else:
                                                min_len[i][j] = j - i + 1
                                                for length in range(2, n + 1):
                                                    for i in range(n - length + 1):
                                                        j = i + length - 1
                                                        for k in range(i, j):
                                                            min_len[i][j] = min(
                                                                min_len[i][j],
                                                                min_len[i][k]
                                                                + min_len[k + 1][j],
                                                            )
                                                            print(min_len[0][n - 1])


if __name__ == "__main__":
    solve()
