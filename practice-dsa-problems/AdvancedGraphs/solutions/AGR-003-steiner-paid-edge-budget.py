from typing import List
import heapq


class Edge:
    def __init__(self, u: int, v: int, paid: int, a: int):
        self.u = u
        self.v = v
        self.paid = paid
        self.a = a


class Solution:
    def minSteinerActivationCost(self, n: int, m: int, k: int, b: int, terminals: List[int], edges: List[Edge]) -> int:
        """
        Solve Steiner tree problem with budget constraint on paid edges.
        
        Algorithm: Bitmask DP with Dijkstra
        - dp[mask][node][budget] = min activation cost to connect terminals 
          in mask, currently at node, using budget paid edges
        - For each mask:
            1. Merge submasks at each node
            2. Run weighted shortest path to extend connections
        """
        INF = float('inf')
        
        # Convert terminals to 0-indexed
        terminals = [t - 1 for t in terminals]
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge.u - 1, edge.v - 1
            adj[u].append((v, edge.paid, edge.a))
            adj[v].append((u, edge.paid, edge.a))
        
        # DP: dp[mask][node][budget_used] = min activation cost
        dp = [[[INF] * (b + 1) for _ in range(n)] for _ in range(1 << k)]
        
        # Base case: each terminal starts at itself with 0 cost and 0 budget
        for i in range(k):
            dp[1 << i][terminals[i]][0] = 0
        
        # Iterate through all masks
        for mask in range(1, 1 << k):
            # First, try to merge two submasks at each node
            # Enumerate all submasks properly
            sub = mask
            while sub > 0:
                comp = mask ^ sub
                # Process each partition only once (sub should be >= comp to avoid duplicates)
                if comp > 0 and sub >= comp:  # Changed from > to >=
                    for node in range(n):
                        for b1 in range(b + 1):
                            if dp[sub][node][b1] >= INF:
                                continue
                            for b2 in range(b - b1 + 1):
                                if dp[comp][node][b2] >= INF:
                                    continue
                                total_b = b1 + b2
                                total_cost = dp[sub][node][b1] + dp[comp][node][b2]
                                dp[mask][node][total_b] = min(dp[mask][node][total_b], total_cost)
                
                sub = (sub - 1) & mask
            
            # Then, run Dijkstra to propagate connections within this mask
            pq = []
            for node in range(n):
                for budget in range(b + 1):
                    if dp[mask][node][budget] < INF:
                        heapq.heappush(pq, (dp[mask][node][budget], node, budget))
            
            while pq:
                cost, u, used_budget = heapq.heappop(pq)
                
                # Skip if we've found a better path
                if cost > dp[mask][u][used_budget]:
                    continue
                
                # Relax edges
                for v, paid, activation in adj[u]:
                    new_budget = used_budget + paid
                    if new_budget <= b:
                        new_cost = cost + activation
                        if new_cost < dp[mask][v][new_budget]:
                            dp[mask][v][new_budget] = new_cost
                            heapq.heappush(pq, (new_cost, v, new_budget))
        
        # Find minimum cost to connect all terminals
        final_mask = (1 << k) - 1
        ans = INF
        
        for node in range(n):
            for budget in range(b + 1):
                ans = min(ans, dp[final_mask][node][budget])
        
        return ans if ans < INF else -1
