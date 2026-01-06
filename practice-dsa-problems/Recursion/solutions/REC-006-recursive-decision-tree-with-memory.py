import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    l_limit = int(input_data[ptr])
    ptr += 1
    f_count = int(input_data[ptr])
    ptr += 1
    forbidden = set()
    for _ in range(f_count):
        forbidden.add(input_data[ptr])
        ptr += 1
        v_count = int(input_data[ptr])
        ptr += 1
    values = {}
    for _ in range(v_count):
        s = input_data[ptr]
        ptr += 1
        v = int(input_data[ptr])
        ptr += 1
        values[s] = v
        
    forbidden_masks = set()
    for s in forbidden:
        forbidden_masks.add(int(s, 2))
        
    ans = -float("inf")

    def search(curr_n, curr_mask, curr_str_list):
        nonlocal ans
        if curr_n == n:
            s_res = "".join(curr_str_list)
            val = values.get(s_res, 0)
            ans = max(ans, val)
            return

        # Try adding '0'
        nm0 = ((curr_mask << 1) | 0) & ((1 << l_limit) - 1)
        valid0 = True
        if curr_n + 1 >= l_limit:
            if nm0 in forbidden_masks:
                valid0 = False
        
        if valid0:
            curr_str_list.append("0")
            search(curr_n + 1, nm0, curr_str_list)
            curr_str_list.pop()

        # Try adding '1'
        nm1 = ((curr_mask << 1) | 1) & ((1 << l_limit) - 1)
        valid1 = True
        if curr_n + 1 >= l_limit:
            if nm1 in forbidden_masks:
                valid1 = False
                
        if valid1:
            curr_str_list.append("1")
            search(curr_n + 1, nm1, curr_str_list)
            curr_str_list.pop()

    search(0, 0, [])
    print(ans if ans != -float("inf") else 0)


if __name__ == "__main__":
    solve()
