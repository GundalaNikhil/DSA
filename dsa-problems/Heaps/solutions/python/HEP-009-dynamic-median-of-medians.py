import sys
import heapq
from collections import defaultdict

class Group:
    def __init__(self):
        self.left = [] # Max heap (negated)
        self.right = [] # Min heap
        
    def add(self, val):
        if not self.left or val <= -self.left[0]:
            heapq.heappush(self.left, -val)
        else:
            heapq.heappush(self.right, val)
        self.rebalance()
        
    def rebalance(self):
        while len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        while len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
            
    def get_median(self):
        if not self.left: return 0
        return -self.left[0]
        
    def size(self):
        return len(self.left) + len(self.right)
        
    def get_elements(self):
        return [-x for x in self.left] + self.right

class Solution:
    def process_operations(self, operations: list) -> list:
        groups = {}
        
        g_left = []
        g_right = []
        g_in_left = defaultdict(int)
        g_in_right = defaultdict(int)
        g_deleted_left = defaultdict(int)
        g_deleted_right = defaultdict(int)
        g_left_size = 0
        g_right_size = 0
        
        def clean_global():
            while g_left:
                val = -g_left[0]
                if g_deleted_left[val] > 0:
                    g_deleted_left[val] -= 1
                    heapq.heappop(g_left)
                else:
                    break
            while g_right:
                val = g_right[0]
                if g_deleted_right[val] > 0:
                    g_deleted_right[val] -= 1
                    heapq.heappop(g_right)
                else:
                    break
                
        def add_to_global(val):
            nonlocal g_left_size, g_right_size
            if val is None: return
            if not g_left or val <= -g_left[0]:
                heapq.heappush(g_left, -val)
                g_in_left[val] += 1
                g_left_size += 1
            else:
                heapq.heappush(g_right, val)
                g_in_right[val] += 1
                g_right_size += 1
            rebalance_global()
            
        def remove_from_global(val):
            nonlocal g_left_size, g_right_size
            if val is None: return
            if g_in_left[val] > 0:
                g_in_left[val] -= 1
                g_deleted_left[val] += 1
                g_left_size -= 1
            else:
                g_in_right[val] -= 1
                g_deleted_right[val] += 1
                g_right_size -= 1
            rebalance_global()
            
        def rebalance_global():
            nonlocal g_left_size, g_right_size
            while g_left_size > g_right_size + 1:
                clean_global()
                val = -heapq.heappop(g_left)
                g_in_left[val] -= 1
                # We don't need to increment deleted here because we popped it
                heapq.heappush(g_right, val)
                g_in_right[val] += 1
                g_left_size -= 1
                g_right_size += 1
            while g_right_size > g_left_size:
                clean_global()
                val = heapq.heappop(g_right)
                g_in_right[val] -= 1
                heapq.heappush(g_left, -val)
                g_in_left[val] += 1
                g_left_size += 1
                g_right_size -= 1
                
        results = []
        
        for op in operations:
            type = op[0]
            if type == "NEW":
                gid, m = op[1], int(op[2])
                g = Group()
                for x in op[3:]:
                    g.add(int(x))
                groups[gid] = g
                add_to_global(g.get_median() if g.size() > 0 else None)
                
            elif type == "ADD":
                gid = op[1]
                if gid in groups:
                    x = int(op[2])
                    g = groups[gid]
                    old_med = g.get_median() if g.size() > 0 else None
                    remove_from_global(old_med)
                    g.add(x)
                    add_to_global(g.get_median())
                    
            elif type == "MERGE":
                gid1, gid2 = op[1], op[2]
                if gid1 in groups and gid2 in groups:
                    g1, g2 = groups[gid1], groups[gid2]
                    remove_from_global(g1.get_median() if g1.size() > 0 else None)
                    remove_from_global(g2.get_median() if g2.size() > 0 else None)
                    
                    if g1.size() < g2.size():
                        for x in g1.get_elements(): g2.add(x)
                        groups[gid1] = g2
                    else:
                        for x in g2.get_elements(): g1.add(x)
                    del groups[gid2]
                    add_to_global(groups[gid1].get_median() if groups[gid1].size() > 0 else None)
                    
            elif type == "QUERY":
                clean_global()
                if g_left_size == 0:
                    results.append("EMPTY")
                else:
                    results.append(str(-g_left[0]))
                    
        return results

def process_operations(operations: list) -> list:
    solver = Solution()
    return solver.process_operations(operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        operations = []
        for _ in range(q):
            op = next(it)
            if op == "NEW":
                gid = next(it)
                m = int(next(it))
                vals = [next(it) for _ in range(m)]
                operations.append([op, gid, m] + vals)
            elif op == "ADD":
                gid = next(it)
                x = next(it)
                operations.append([op, gid, x])
            elif op == "MERGE":
                gid1 = next(it)
                gid2 = next(it)
                operations.append([op, gid1, gid2])
            else:
                operations.append([op])
        
        result = process_operations(operations)
        print("\n".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
