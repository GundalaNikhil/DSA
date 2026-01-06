import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        start_node = int(next(iterator)) - 1
        target_node = int(next(iterator)) - 1
        k_stops = int(next(iterator))
        cap = int(next(iterator))
        
        node_costs = []
        for _ in range(n):
            node_costs.append(int(next(iterator)))
            
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator)) - 1
            v = int(next(iterator)) - 1
            f_req = int(next(iterator))
            adj[u].append((v, f_req))
    except StopIteration:
        return

    # Dijkstra
    # State: (cost, u, stops, fuel)
    # Minimizing cost.
    # Constraints: stops <= k_stops, fuel <= cap (implied max capacity?) or strictly needed?
    # Logic from original code suggest 'cap' is max fuel capacity?
    # Original: `if f < cap: ... f+1` (checking max capacity for refuel)
    # Original: `if f >= fuel_req:` (checking sufficient fuel for travel)
    
    INF = float("inf")
    # dist map: (u, stops, fuel) -> min_cost
    # Using a dict is safer than array due to potentially sparse reachable states, though states are bounded.
    # stops: 0 to k_stops
    # fuel: 0 to cap
    # Size: N * K * Cap approx 100 * 100 * 100 = 10^6 states. Manageable.
    
    dist = {}
    
    # Priority Queue
    # Start: cost=0, node=start_node, stops=0, fuel=0.
    # Assumption: Start with 0 fuel? Original code initialized `dist[(start_node, 0, 0)] = 0`.
    pq = [(0, start_node, 0, 0)]
    dist[(start_node, 0, 0)] = 0
    
    final_ans = INF
    
    while pq:
        c, u, s, f = heapq.heappop(pq)
        
        if c > dist.get((u, s, f), INF):
            continue
        
        if u == target_node:
            final_ans = min(final_ans, c)
            # We can continue to find cheaper paths? Dijkstra guarantees first time we pop target is optimal?
            # Not necessarily if state includes other constraints. 
            # Standard Dijkstra on expanded state graph guarantees optimality.
            # So `return` or `break` is allowed IF we don't care about other specific end states.
            # But since we minimize C, yes.
            # However, we might reach target with high cost but low stops, which might extend further?
            # No, if we reached target, that's a path. We just want min cost.
            # BUT, we pop based on C.
            # So the first time we pop any state `(cost, target, ...)` it is the minimal cost to reach target?
            # Yes, because edge weights (refuel costs) are non-negative.
            print(c)
            return

        # Option 1: Refuel at current node (1 unit)
        # Cost: node_costs[u]
        # Condition: f < cap
        if f < cap:
            new_c = c + node_costs[u]
            # Next state: same node, same stops, fuel + 1
            state_refuel = (u, s, f + 1)
            if new_c < dist.get(state_refuel, INF):
                dist[state_refuel] = new_c
                heapq.heappush(pq, (new_c, u, s, f + 1))
        
        # Option 2: Travel to neighbor
        # Condition: s < k_stops?
        # IMPORTANT: "k_stops" usually means max intermediate nodes.
        # If we move u -> v, stops increases by 1?
        # Original code: `if s < k_stops:` then `(v, s + 1, ...)`
        # This implies `s` counts hops?
        # If `s` includes the destination hop?
        # Usually k stops means at most k intermediate nodes.
        # Edges = k + 1.
        # If limit is on edges, then `s` counts edges?
        # Assume `s` is edges traversed.
        # Constraint is `k_stops`. If `s` counts edges, max edges = k_stops + 1?
        # The original code used `if s < k_stops`.
        # So if `s` reaches `k_stops`, we can't move further.
        # This implies max hops = k_stops.
        
        if s <= k_stops: # Or k_stops + 1? adhering to strict reading of original "s < k_stops" -> max hops k_stops
             # Original: if s < k_stops: ... push(s+1) -> effectively stops at s+1 <= k_stops.
             # So max `s` in queue is `k_stops`.
             
             for v, fuel_req in adj[u]:
                if f >= fuel_req:
                    new_f = f - fuel_req
                    # Cost doesn't increase on travel (only on refuel)
                    state_move = (v, s + 1, new_f)
                    if c < dist.get(state_move, INF):
                        dist[state_move] = c
                        heapq.heappush(pq, (c, v, s + 1, new_f))

    print("-1")


if __name__ == "__main__":
    solve()
