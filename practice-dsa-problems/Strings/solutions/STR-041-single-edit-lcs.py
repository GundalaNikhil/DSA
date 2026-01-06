import sys


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    a, b = input_data[0], input_data[1]
    n, m = len(a), len(b)
    dp0 = [0] * (m + 1)
    dp1 = [0] * (m + 1)
    for i in range(1, n + 1):
        new_dp0 = [0] * (m + 1)
        new_dp1 = [0] * (m + 1)
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                new_dp0[j] = dp0[j - 1] + 1
            else:
                new_dp0[j] = max(dp0[j], new_dp0[j - 1])
                res_with_prev_edit = max(dp1[j], new_dp1[j - 1])
                if a[i - 1] == b[j - 1]:
                    res_with_prev_edit = max(res_with_prev_edit, dp1[j - 1] + 1)
                    res_using_edit_now = dp0[j - 1] + 1
                    new_dp1[j] = max(res_with_prev_edit, res_using_edit_now)
                    dp0 = new_dp0
                    dp1 = new_dp1
                    
    print(max(dp0[m], dp1[m]))


if __name__ == "__main__":
    solve()
