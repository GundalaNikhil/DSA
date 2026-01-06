import sys
from collections import defaultdict
sys.setrecursionlimit(300000)
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m_mod = int(input_data[ptr])
    ptr += 1
    t_target = int(input_data[ptr])
    ptr += 1
    props = []
    adj = defaultdict(list)
    root = -1
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        coef = int(input_data[ptr])
        ptr += 1
        p = int(input_data[ptr])
        ptr += 1
        props.append((v, coef))
        if p == 0:
            root = i
        else:
            adj[p].append(i)
            
    def get_chk(u):
        v, coef = props[u - 1]
        term = (v * coef) % m_mod
        child_sum = 0
        for v_child in adj[u]:
            child_sum = (child_sum + get_chk(v_child)) % m_mod
            
        return (term + child_sum) % m_mod

    if root != -1:
        res = get_chk(root)
        if (res + m_mod) % m_mod == (t_target + m_mod) % m_mod:
            print("YES")
        else:
            print("NO")
    else:
        # No root, sum is 0?
        if 0 == (t_target + m_mod) % m_mod:
            print("YES")
        else:
            print("NO")
if __name__ == '__main__':
    solve()