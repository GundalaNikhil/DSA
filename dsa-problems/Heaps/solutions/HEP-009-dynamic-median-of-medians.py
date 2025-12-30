import sys
import heapq

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
        
        # Global heaps
        g_left = [] # Max heap
        g_right = [] # Min heap
        g_deleted = {}
        g_left_size = 0
        g_right_size = 0
        
        def clean_global():
            while g_left and g_deleted.get(-g_left[0], 0) > 0:
                val = -heapq.heappop(g_left)
                g_deleted[val] -= 1
                if g_deleted[val] == 0: del g_deleted[val]
            while g_right and g_deleted.get(g_right[0], 0) > 0:
                val = heapq.heappop(g_right)
                g_deleted[val] -= 1
                if g_deleted[val] == 0: del g_deleted[val]
                
        def add_to_global(val):
            nonlocal g_left_size, g_right_size
            clean_global()
            if not g_left or val <= -g_left[0]:
                heapq.heappush(g_left, -val)
                g_left_size += 1
            else:
                heapq.heappush(g_right, val)
                g_right_size += 1
            rebalance_global()
            
        def remove_from_global(val):
            nonlocal g_left_size, g_right_size
            g_deleted[val] = g_deleted.get(val, 0) + 1
            clean_global()
            # Infer location
            if g_left and val <= -g_left[0]:
                g_left_size -= 1
            else:
                g_right_size -= 1
            rebalance_global()
            
        def rebalance_global():
            nonlocal g_left_size, g_right_size
            clean_global()
            while g_left_size > g_right_size + 1:
                val = -heapq.heappop(g_left)
                heapq.heappush(g_right, val)
                g_left_size -= 1
                g_right_size += 1
                clean_global()
            while g_right_size > g_left_size:
                val = heapq.heappop(g_right)
                heapq.heappush(g_left, -val)
                g_left_size += 1
                g_right_size -= 1
                clean_global()
                
        results = []
        
        for op in operations:
            type = op[0]
            if type == "NEW":
                gid = op[1]
                g = Group()
                for x in op[2:]:
                    g.add(int(x))
                groups[gid] = g
                add_to_global(g.get_median())
                
            elif type == "ADD":
                gid = op[1]
                x = int(op[2])
                if gid in groups:
                    g = groups[gid]
                    remove_from_global(g.get_median())
                    g.add(x)
                    add_to_global(g.get_median())
                    
            elif type == "MERGE":
                gid1 = op[1]
                gid2 = op[2]
                if gid1 in groups and gid2 in groups:
                    g1 = groups[gid1]
                    g2 = groups[gid2]
                    
                    remove_from_global(g1.get_median())
                    remove_from_global(g2.get_median())
                    
                    # Small to large
                    if g1.size() < g2.size():
                        # Move g1 to g2
                        for x in g1.get_elements():
                            g2.add(x)
                        groups[gid1] = g2
                    else:
                        for x in g2.get_elements():
                            g1.add(x)
                        # g1 is updated
                        
                    del groups[gid2]
                    add_to_global(groups[gid1].get_median())
                    
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
                operations.append([op, gid] + vals)
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
