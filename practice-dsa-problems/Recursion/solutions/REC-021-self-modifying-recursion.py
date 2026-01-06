import sys

sys.setrecursionlimit(1000000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    d_limit = int(input_data[ptr])
    ptr += 1
    s_start = int(input_data[ptr])
    ptr += 1
    MOD = 1_000_000_007
    weights = [0] * (n + 1)
    toggles = [0] * (n + 1)
    lists0 = [[] for _ in range(n + 1)]
    lists1 = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        weights[i] = int(input_data[ptr])
        ptr += 1
        toggles[i] = int(input_data[ptr])
        ptr += 1
        c0 = int(input_data[ptr])
        ptr += 1
        for _ in range(c0):
            lists0[i].append(int(input_data[ptr]))
            ptr += 1
        c1 = int(input_data[ptr])
        ptr += 1
        for _ in range(c1):
            lists1[i].append(int(input_data[ptr]))
            ptr += 1
            
    memo = {}

    def eval_node(u, depth, mode):
        if depth == 0:
            return weights[u]
            
        state = (u, depth, mode)
        if state in memo:
            return memo[state]
            
        curr_list = lists0[u] if mode == 0 else lists1[u]
        
        if not curr_list:
            res = weights[u]
        else:
            next_mode = mode ^ toggles[u]
            res = 0
            for v in curr_list:
                res = (res + eval_node(v, depth - 1, next_mode)) % MOD
                
        memo[state] = res
        return res

    print(eval_node(s_start, d_limit, 0))


if __name__ == "__main__":
    solve()
