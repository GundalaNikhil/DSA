import random
import yaml

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.history = []
        
    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.history.append((root_j, self.parent[root_j], root_i, self.size[root_i]))
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        else:
            self.history.append(None)
            return False
            
    def rollback(self):
        item = self.history.pop()
        if item:
            child, old_p, parent, old_size = item
            self.parent[child] = old_p
            self.size[parent] = old_size

class DynamicConnectivity:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.tree = [[] for _ in range(4 * m)]
        self.queries = [None] * m
        
    def add_edge_to_tree(self, node, start, end, l, r, edge):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.tree[node].append(edge)
            return
        mid = (start + end) // 2
        self.add_edge_to_tree(2 * node + 1, start, mid, l, r, edge)
        self.add_edge_to_tree(2 * node + 2, mid + 1, end, l, r, edge)
        
    def solve(self):
        dsu = DSU(self.n)
        results = []
        self._dfs(0, 0, self.m - 1, dsu, results)
        return results
        
    def _dfs(self, node, start, end, dsu, results):
        for u, v in self.tree[node]:
            dsu.union(u, v)
            
        if start == end:
            if self.queries[start]:
                u, v = self.queries[start]
                results.append("true" if dsu.find(u) == dsu.find(v) else "false")
        else:
            mid = (start + end) // 2
            self._dfs(2 * node + 1, start, mid, dsu, results)
            self._dfs(2 * node + 2, mid + 1, end, dsu, results)
            
        for _ in self.tree[node]:
            dsu.rollback()

def solve_dynamic_connectivity(n, m, events):
    dc = DynamicConnectivity(n, m)
    edge_start = {}
    for i, (op, u_s, v_s) in enumerate(events):
        u, v = int(u_s), int(v_s)
        if u > v: u, v = v, u
        if op == "ADD":
            edge_start[(u, v)] = i
        elif op == "REMOVE":
            if (u, v) in edge_start:
                dc.add_edge_to_tree(0, 0, m - 1, edge_start[(u, v)], i, (u, v))
                del edge_start[(u, v)]
        else:
            dc.queries[i] = (u, v)
            
    for (u, v), t_start in edge_start.items():
        dc.add_edge_to_tree(0, 0, m - 1, t_start, m - 1, (u, v))
        
    return dc.solve()

def make_test_case(n, m, events):
    input_str = f"{n} {m}\n"
    for op in events:
        input_str += " ".join(map(str, op)) + "\n"
    output_str = "\n".join(solve_dynamic_connectivity(n, m, events))
    return input_str, output_str

def main():
    test_cases = {"samples": [], "public": [], "hidden": []}
    
    # Sample Case
    n, m = 3, 4
    events = [["ADD", 1, 2], ["QUERY", 1, 2], ["REMOVE", 1, 2], ["QUERY", 1, 2]]
    input_str, output_str = make_test_case(n, m, events)
    test_cases["samples"].append({"input": input_str, "output": output_str})

    # Public Cases
    # More complex chain and cycles
    n, m = 4, 6
    events = [
        ["ADD", 1, 2],
        ["ADD", 2, 3],
        ["QUERY", 1, 3],   # true
        ["ADD", 3, 4],
        ["REMOVE", 2, 3],
        ["QUERY", 1, 4]    # false
    ]
    input_str, output_str = make_test_case(n, m, events)
    test_cases["public"].append({"input": input_str, "output": output_str})

    # Hidden Cases
    # Edge Cases
    test_cases["hidden"].append({"input": "1 1\nQUERY 1 1\n", "output": "true", "category": "edge"})
    
    # Fully connected and disconnected
    n, m = 3, 4
    events = [["ADD", 1, 2], ["ADD", 2, 3], ["ADD", 1, 3], ["QUERY", 1, 3]]
    input_str, output_str = make_test_case(n, m, events)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "edge"})

    # Stress Case
    n, m = 5000, 5000
    events = []
    edges = set()
    for _ in range(m):
        r = random.random()
        if r < 0.4:
            u = random.randint(1, n)
            v = random.randint(1, n)
            if u != v:
                if u > v: u, v = v, u
                if (u, v) not in edges:
                    events.append(["ADD", u, v])
                    edges.add((u, v))
                else:
                    events.append(["QUERY", u, v])
            else:
                events.append(["QUERY", u, v])
        elif r < 0.7 and edges:
            edge = random.choice(list(edges))
            events.append(["REMOVE", edge[0], edge[1]])
            edges.remove(edge)
        else:
            u = random.randint(1, n)
            v = random.randint(1, n)
            events.append(["QUERY", u, v])
    input_str, output_str = make_test_case(n, m, events)
    test_cases["hidden"].append({"input": input_str, "output": output_str, "category": "stress"})

    with open("SegmentTree/testcases/SEG-016-dynamic-connectivity-offline.yaml", "w") as f:
        yaml.dump(test_cases, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    main()
