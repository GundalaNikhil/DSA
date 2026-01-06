import sys

sys.setrecursionlimit(300000)


def is_mirror(id1, id2, nodes):
    if id1 == 0 and id2 == 0:
        return True
    if id1 == 0 or id2 == 0:
        return False
    val1, l1, r1 = nodes[id1 - 1]
    val2, l2, r2 = nodes[id2 - 1]
    if val1 != val2:
        return False
    return is_mirror(l1, r2, nodes) and is_mirror(r1, l2, nodes)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    nodes = []
    ptr = 1
    for _ in range(n):
        v = int(input_data[ptr])
        ptr += 1
        l = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        nodes.append((v, l, r))
        
    if n == 0:
        print("YES")
        return
        
    val, left, right = nodes[0]
    if is_mirror(left, right, nodes):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
