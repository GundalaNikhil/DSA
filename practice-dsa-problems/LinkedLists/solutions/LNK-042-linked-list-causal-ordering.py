import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
    
    executed = [False] * (q + 1)
    tasks = []
    
    for _ in range(q):
        k = int(input_data[ptr])
        ptr += 1
        deps = []
        for _ in range(k):
            deps.append(int(input_data[ptr]))
            ptr += 1
        tasks.append(deps)
        
    for i in range(1, q + 1):
        deps = tasks[i - 1]
        for d in deps:
            if d >= i or not executed[d]:
                print(i)
                return
        executed[i] = True
        
    print(0)


if __name__ == "__main__":
    solve()
