import sys

class Task:
    def __init__(self, tid, count, priority):
        self.id = tid
        self.count = count
        self.priority = priority
        self.x = count

class Solution:
    def max_priority(self, T: int, cooldown: int, ids: list, count: list, priority: list) -> int:
        tasks = []
        for i in range(len(ids)):
            tasks.append(Task(ids[i], count[i], priority[i]))
            
        # 1. Clamp
        limit = (T + cooldown) // (cooldown + 1)
        for t in tasks:
            t.x = min(t.count, limit)
            
        # 2. Schedule Constraint
        while True:
            max_x = 0
            for t in tasks:
                max_x = max(max_x, t.x)
            
            if max_x == 0:
                break
                
            at_max = [t for t in tasks if t.x == max_x]
            required = (max_x - 1) * (cooldown + 1) + len(at_max)
            
            if required <= T:
                break
                
            allowed = T - (max_x - 1) * (cooldown + 1)
            # Sort by priority desc
            at_max.sort(key=lambda x: x.priority, reverse=True)
            
            for i in range(int(allowed), len(at_max)):
                at_max[i].x -= 1
                
        # 3. Sum Constraint
        sum_x = sum(t.x for t in tasks)
        if sum_x > T:
            to_remove = sum_x - T
            # Sort by priority asc
            tasks.sort(key=lambda x: x.priority)
            
            for t in tasks:
                if to_remove <= 0:
                    break
                rem = min(t.x, to_remove)
                t.x -= rem
                to_remove -= rem
                
        return sum(t.x * t.priority for t in tasks)

def max_priority(T: int, cooldown: int, ids: list, count: list, priority: list) -> int:
    solver = Solution()
    return solver.max_priority(T, cooldown, ids, count, priority)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        m = int(next(it))
        cooldown = int(next(it))
        T = int(next(it))
        ids = []
        count = []
        priority = []
        for _ in range(m):
            ids.append(next(it))
            count.append(int(next(it)))
            priority.append(int(next(it)))
            
        print(max_priority(T, cooldown, ids, count, priority))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
