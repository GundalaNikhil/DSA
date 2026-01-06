import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    costs = [int(x) for x in input_data[1:]]
    total_cost = 0
    clean_s = []
    clean_costs = []
    for char in s:
        if "a" <= char <= "z":
            total_cost += costs[ord(char) - ord("a")]
        elif char == "(":
            clean_s.append("(")
            clean_costs.append(costs[26])
        elif char == ")":
            clean_s.append(")")
            clean_costs.append(costs[27])
            pq = []
            balance = 0
            n = len(clean_s)
            kept_indices = [True] * n
            for i in range(n):
                if clean_s[i] == "(":
                    balance += 1
                else:
                    balance -= 1
                    heapq.heappush(pq, (clean_costs[i], i))
                    if balance < 0:
                        c, idx = heapq.heappop(pq)
                        total_cost += c
                        kept_indices[idx] = False
                        balance += 1
            if balance < 0:
                c, idx = heapq.heappop(pq)
                total_cost += c
                kept_indices[idx] = False
                balance += 1
                
    # Second pass: Right to Left
    pq = []
    balance = 0
    for i in range(n - 1, -1, -1):
        if not kept_indices[i]:
            continue
        if clean_s[i] == ")":
            balance += 1
        else:
            balance -= 1
            heapq.heappush(pq, (clean_costs[i], i))
            if balance < 0:
                c, idx = heapq.heappop(pq)
                total_cost += c
                kept_indices[idx] = False
                balance += 1
                
    print(total_cost)


if __name__ == "__main__":
    solve()
