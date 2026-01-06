import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    r_count = int(input_data[ptr])
    ptr += 1
    s_target = int(input_data[ptr])
    ptr += 1
    rules = []
    prereq_to_rules = {}
    rule_prereq_count = []
    rule_total_cost = []
    rule_head = []
    symbol_cost = {}
    for i in range(r_count):
        head = int(input_data[ptr])
        ptr += 1
        k = int(input_data[ptr])
        ptr += 1
        rule_head.append(head)
        rule_prereq_count.append(k)
        rule_total_cost.append(0)
        
        if k == 0:
            pass
        else:
            for _ in range(k):
                prereq = int(input_data[ptr])
                ptr += 1
                if prereq not in prereq_to_rules:
                    prereq_to_rules[prereq] = []
                prereq_to_rules[prereq].append(i)
                
    heap = []
    
    # Initialize basic facts (rules with 0 prereqs)
    for i in range(r_count):
        if rule_prereq_count[i] == 0:
            h = rule_head[i]
            cost = 1 # Rule cost
            if h not in symbol_cost or cost < symbol_cost[h]:
                symbol_cost[h] = cost
                heapq.heappush(heap, (cost, h))
                
    # Dijkstra
    while heap:
        d, u = heapq.heappop(heap)
        
        if d > symbol_cost.get(u, float("inf")):
            continue
            
        if u in prereq_to_rules:
            for r_idx in prereq_to_rules[u]:
                rule_prereq_count[r_idx] -= 1
                rule_total_cost[r_idx] += d # Accumulate cost of prerequisites
                
                if rule_prereq_count[r_idx] == 0:
                    h = rule_head[r_idx]
                    new_cost = 1 + rule_total_cost[r_idx]
                    
                    if (h not in symbol_cost or new_cost < symbol_cost[h]):
                        symbol_cost[h] = new_cost
                        heapq.heappush(heap, (new_cost, h))
                        
    if s_target in symbol_cost:
        print(symbol_cost[s_target])
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    solve()
