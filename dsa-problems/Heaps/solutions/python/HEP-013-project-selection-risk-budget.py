import sys
import heapq

class Solution:
    def maximize_capital(self, k: int, C: int, R: int, cost: list, profit: list, risk: list) -> int:
        n = len(cost)
        projects = []
        for i in range(n):
            projects.append((cost[i], profit[i], risk[i]))
            
        # Sort by cost
        projects.sort(key=lambda x: x[0])
        
        # Max-Heap (store -profit)
        pq = []
        ptr = 0
        current_c = C
        remaining_r = R
        
        for _ in range(k):
            # Add affordable
            while ptr < n and projects[ptr][0] <= current_c:
                # Push (-profit, risk)
                heapq.heappush(pq, (-projects[ptr][1], projects[ptr][2]))
                ptr += 1
                
            # Pick best
            picked = False
            while pq:
                p, r = pq[0] # Peek
                p = -p
                
                if r <= remaining_r:
                    heapq.heappop(pq)
                    current_c += p
                    remaining_r -= r
                    picked = True
                    break
                else:
                    # Too risky
                    heapq.heappop(pq)
            
            if not picked:
                break
                
        return current_c

def maximize_capital(k: int, C: int, R: int, cost: list, profit: list, risk: list) -> int:
    solver = Solution()
    return solver.maximize_capital(k, C, R, cost, profit, risk)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        k = int(next(it))
        C = int(next(it))
        R = int(next(it))
        cost = []
        profit = []
        risk = []
        for _ in range(n):
            cost.append(int(next(it)))
            profit.append(int(next(it)))
            risk.append(int(next(it)))
            
        print(maximize_capital(k, C, R, cost, profit, risk))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
