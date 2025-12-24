
import sys
sys.setrecursionlimit(200005)

def determine_winning_nodes(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    
    memo = {}

    def dfs(u):
        if u in memo:
            return memo[u]
        
        is_winning = False
        for v in adj[u]:
            if not dfs(v):
                is_winning = True
                break
        
        memo[u] = is_winning
        return is_winning

    result = []
    for i in range(n):
        if dfs(i):
            result.append("Winning")
        else:
            result.append("Losing")
    return result

test_cases = [
    ("3 2\n0 1\n1 2", "Losing Winning Losing"),
    ("3 2\n0 1\n0 2", "Winning Losing Losing"),
    ("1 0", "Losing"),
    ("2 1\n0 1", "Winning Losing"),
    ("4 3\n0 1\n1 2\n2 3", "Winning Losing Winning Losing"),
    ("5 4\n0 1\n1 2\n2 3\n3 4", "Losing Winning Losing Winning Losing"),
    ("3 3\n0 1\n0 2\n1 2", "Winning Winning Losing"),
    ("4 4\n0 1\n0 2\n1 3\n2 3", "Losing Winning Winning Losing"),
    ("5 5\n0 1\n1 2\n2 3\n3 4\n0 4", "Winning Winning Losing Winning Losing"),
    ("6 6\n0 1\n1 2\n2 3\n3 4\n4 5\n0 5", "Winning Losing Winning Losing Winning Losing"),
    ("6 7\n0 1\n0 2\n1 3\n2 4\n3 5\n4 5\n0 5", "Winning Winning Winning Winning Winning Losing"),
    ("2 0", "Losing Losing"),
    ("2 0", "Losing Losing"),
    ("10 9\n0 1\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n8 9", "Winning Losing Winning Losing Winning Losing Winning Losing Winning Losing"),
    ("5 6\n0 1\n0 2\n1 3\n2 3\n3 4\n0 4", "Winning Losing Losing Winning Losing"),
    ("4 6\n0 1\n0 2\n0 3\n1 2\n1 3\n2 3", "Winning Winning Winning Losing"),
    ("4 0", "Losing Losing Losing Losing"),
    ("5 4\n0 1\n2 3\n3 4\n1 4", "Winning Losing Winning Winning Losing"),
    ("6 5\n0 1\n1 2\n3 4\n4 5\n2 5", "Winning Losing Winning Winning Losing Losing"),
    ("7 6\n0 1\n1 2\n2 3\n4 5\n5 6\n3 6", "Losing Winning Losing Winning Winning Losing Losing"),
    ("3 2\n0 2\n1 2", "Winning Winning Losing"),
    ("3 1\n0 1", "Winning Losing Losing"),
    ("4 2\n0 1\n2 3", "Winning Losing Winning Losing"),
    ("5 7\n0 1\n0 2\n1 3\n2 3\n3 4\n1 4\n2 4", "Winning Winning Winning Winning Losing"),
    ("6 8\n0 1\n0 2\n1 3\n2 4\n3 5\n4 5\n1 5\n2 5", "Winning Winning Winning Winning Winning Losing"),
    ("8 7\n0 1\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7", "Winning Losing Winning Losing Winning Losing Winning Losing"),
    ("8 10\n0 1\n0 2\n1 3\n2 4\n3 5\n4 6\n5 7\n6 7\n1 7\n2 7", "Winning Winning Winning Winning Winning Winning Winning Losing"),
    ("4 5\n0 1\n1 2\n2 3\n0 2\n1 3", "Winning Winning Winning Losing"),
    ("5 9\n0 1\n0 2\n0 3\n0 4\n1 2\n1 3\n1 4\n2 3\n2 4", "Winning Winning Winning Winning Losing"),
    ("5 10\n0 1\n0 2\n0 3\n0 4\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4", "Winning Winning Winning Winning Losing"),
    ("1 0", "Losing"),
    ("2 1\n1 0", "Losing Winning"),
    ("3 3\n2 1\n1 0\n2 0", "Losing Winning Winning"),
    ("4 6\n3 2\n3 1\n3 0\n2 1\n2 0\n1 0", "Losing Losing Winning Winning"),
    ("5 4\n4 3\n3 2\n2 1\n1 0", "Losing Winning Losing Winning Losing"),
    ("6 5\n5 4\n4 3\n3 2\n2 1\n1 0", "Losing Winning Losing Winning Losing Winning"),
    ("7 6\n6 5\n5 4\n4 3\n3 2\n2 1\n1 0", "Losing Winning Losing Winning Losing Winning Losing"),
    ("8 7\n7 6\n6 5\n5 4\n4 3\n3 2\n2 1\n1 0", "Losing Winning Losing Winning Losing Winning Losing Winning"),
    ("9 8\n8 7\n7 6\n6 5\n5 4\n4 3\n3 2\n2 1\n1 0", "Losing Winning Losing Winning Losing Winning Losing Winning Losing"),
    ("10 9\n9 8\n8 7\n7 6\n6 5\n5 4\n4 3\n3 2\n2 1\n1 0", "Losing Winning Losing Winning Losing Winning Losing Winning Losing Winning")
]

failed = False
for inp, expected in test_cases:
    lines = inp.strip().split('\n')
    n, m = map(int, lines[0].split())
    edges = []
    for line in lines[1:]:
        edges.append(list(map(int, line.split())))
    
    got_list = determine_winning_nodes(n, edges)
    got = " ".join(got_list)
    
    if got != expected:
        print(f"Failed:\nInput:\n{inp}\nExpected: {expected}\nGot:      {got}")
        failed = True

if not failed:
    print("All GMT-002 tests passed!")
