import sys

sys.setrecursionlimit(300000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    nodes = {}
    for i in range(1, n + 1):
        v = int(input_data[ptr])
        ptr += 1
        l = int(input_data[ptr])
        ptr += 1
        r = int(input_data[ptr])
        ptr += 1
        nodes[i] = [v, l, r]
        
    total_sum = 0

    def traverse(u):
        nonlocal total_sum
        if u == 0 or u not in nodes:
            return
            
        val, left, right = nodes[u]
        total_sum += val
        
        if val % 2 == 0:
            right = 0
            if left != 0:
                traverse(left)
            # Original code logic: if right=0, we don't traverse right anyway.
        else:
            left, right = right, left
            # Swap happens locally?
            # Original code said: left, right = right, left
            # then traverse(left) [which was old right]
            # then traverse(right) [which was old left]
            
            if left != 0:
                traverse(left)
            if right != 0:
                traverse(right)
                
    traverse(1)
    print(total_sum)


if __name__ == "__main__":
    solve()
