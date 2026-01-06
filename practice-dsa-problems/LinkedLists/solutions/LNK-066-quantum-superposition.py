import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    nodes = []
    for _ in range(n):
        a = int(input_data[ptr])
        ptr += 1
        b = int(input_data[ptr])
        ptr += 1
        nodes.append([a, b, None])
        
    q = int(input_data[ptr])
    ptr += 1
    
    for _ in range(q):
        pos = int(input_data[ptr])
        ptr += 1
        t = int(input_data[ptr])
        ptr += 1
        
        node = nodes[pos - 1]
        
        # Superposition collapse logic?
        if node[2] is None:
            if t % 2 == 0:
                node[2] = node[0]
            else:
                node[2] = node[1]
                
        print(node[2])


if __name__ == "__main__":
    solve()
