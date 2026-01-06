import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    actions = []
    for _ in range(a_count):
        d = int(input_data[ptr])
        ptr += 1
        t = int(input_data[ptr])
        ptr += 1
        s = int(input_data[ptr])
        ptr += 1
        actions.append((d, t, s))
        dp = {(0, 0, 0, 0, 0): 0}
        for step in range(n):
            new_dp = {}
            for dk, total_dmg in dp.items():
                active_dmg = sum(dk)
                new_base_dk = (0, dk[0], dk[1], dk[2], dk[3])
                for d_i, t_i, s_i in actions:
                    immediate = d_i
                    final_dk = list(new_base_dk)
                    if t_i > 0:
                        idx = 5 - t_i
                        final_dk[idx] += s_i
                        fd_tuple = tuple(final_dk)
                        new_dp[fd_tuple] = max(
                            new_dp.get(fd_tuple, -float("inf")),
                            total_dmg + active_dmg + immediate,
                        )
                        dp = new_dp
                        print(max(dp.values()))


if __name__ == "__main__":
    solve()
