
import random
import heapq
import yaml
from collections import defaultdict

class MedianFinder:
    def __init__(self):
        self.small = [] # Max heap (stored as neg)
        self.large = [] # Min heap
        
    def add(self, num):
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            
    def get_median(self):
        if not self.small:
            return None
        return -self.small[0]

    def get_all(self):
        res = [-x for x in self.small] + self.large
        return res

class GlobalMedianTracker:
    def __init__(self):
        self.small = [] # Max heap
        self.large = [] # Min heap
        self.deleted_small = defaultdict(int)
        self.deleted_large = defaultdict(int)
        self.small_size = 0
        self.large_size = 0
        
    def _move_small_to_large(self):
        if not self.small: return
        val = -heapq.heappop(self.small)
        if self.deleted_small[val] > 0:
            self.deleted_small[val] -= 1
            self.deleted_large[val] += 1
        else:
            self.small_size -= 1
            self.large_size += 1
        heapq.heappush(self.large, val)
        
    def _move_large_to_small(self):
        if not self.large: return
        val = heapq.heappop(self.large)
        if self.deleted_large[val] > 0:
            self.deleted_large[val] -= 1
            self.deleted_small[val] += 1
        else:
            self.large_size -= 1
            self.small_size += 1
        heapq.heappush(self.small, -val)

    def _clean(self):
        while self.small and self.deleted_small[-self.small[0]] > 0:
            val = -heapq.heappop(self.small)
            self.deleted_small[val] -= 1
        while self.large and self.deleted_large[self.large[0]] > 0:
            val = heapq.heappop(self.large)
            self.deleted_large[val] -= 1

    def _balance(self):
        self._clean()
        while self.small and self.large and (-self.small[0] > self.large[0]):
             self._move_small_to_large()
             self._clean()
             
        self._clean()
        while self.small_size > self.large_size + 1:
            self._move_small_to_large()
            self._clean()
            
        while self.large_size > self.small_size:
            self._move_large_to_small()
            self._clean()

    def add(self, num):
        heapq.heappush(self.small, -num)
        self.small_size += 1
        self._balance()
        
    def remove(self, num):
        self._clean()
        # Decide which heap it is in based on current separator
        # If small is empty, it must be in large (if it exists)
        if self.small and num <= -self.small[0]:
            self.deleted_small[num] += 1
            self.small_size -= 1
        else:
            self.deleted_large[num] += 1
            self.large_size -= 1
            
        self._balance()

    def get_median(self):
        self._clean()
        if self.small_size == 0:
            return "EMPTY"
        return -self.small[0]

def solve(operations):
    groups = {} # id -> MedianFinder
    global_tracker = GlobalMedianTracker()
    output = []
    
    for op_line in operations:
        op = op_line[0]
        
        if op == "NEW":
            gid = int(op_line[1])
            vals = list(map(int, op_line[3:])) 
            mf = MedianFinder()
            for v in vals:
                mf.add(v)
            groups[gid] = mf
            
            med = mf.get_median()
            if med is not None:
                global_tracker.add(med)
                
        elif op == "ADD":
            gid = int(op_line[1])
            val = int(op_line[2])
            
            if gid in groups:
                old_med = groups[gid].get_median()
                if old_med is not None:
                    global_tracker.remove(old_med)
                
                groups[gid].add(val)
                new_med = groups[gid].get_median()
                global_tracker.add(new_med)
            else:
                pass
                
        elif op == "MERGE":
            id1 = int(op_line[1])
            id2 = int(op_line[2])
            
            if id1 in groups and id2 in groups:
                med1 = groups[id1].get_median()
                if med1 is not None:
                    global_tracker.remove(med1)
                
                med2 = groups[id2].get_median()
                if med2 is not None:
                    global_tracker.remove(med2)
                
                vals2 = groups[id2].get_all()
                for v in vals2:
                    groups[id1].add(v)
                
                del groups[id2]
                
                new_med1 = groups[id1].get_median()
                if new_med1 is not None:
                    global_tracker.add(new_med1)
                    
        elif op == "QUERY":
            output.append(str(global_tracker.get_median()))
            
    return output

def format_ops(ops):
    res = []
    for line in ops:
        res.append(" ".join(map(str, line)))
    return res

def generate_test_cases():
    test_cases = []
    
    # 1. SAMPLE
    ops_sample = [
        ["NEW", "1", "2", "1", "3"],
        ["NEW", "2", "1", "2"],
        ["MERGE", "1", "2"],
        ["QUERY"]
    ]
    test_cases.append({
        "input": f"{len(ops_sample)}\n" + "\n".join(format_ops(ops_sample)),
        "output": "\n".join(solve(ops_sample)),
        "category": "sample",
        "description": "Sample case from problem statement"
    })
    
    # 2. EDGE
    ops_edge1 = [["QUERY"]]
    test_cases.append({
        "input": f"{len(ops_edge1)}\n" + "\n".join(format_ops(ops_edge1)),
        "output": "\n".join(solve(ops_edge1)),
        "category": "edge",
        "description": "Query on empty set"
    })
    
    ops_edge2 = [["NEW", "1", "1", "10"], ["QUERY"]]
    test_cases.append({
        "input": f"{len(ops_edge2)}\n" + "\n".join(format_ops(ops_edge2)),
        "output": "\n".join(solve(ops_edge2)),
        "category": "edge",
        "description": "Single group query"
    })
    
    ops_edge3 = [
        ["NEW", "10", "1", "5"],
        ["NEW", "20", "1", "15"],
        ["MERGE", "10", "20"], 
        ["QUERY"], 
        ["ADD", "10", "20"], 
        ["QUERY"] 
    ]
    test_cases.append({
        "input": f"{len(ops_edge3)}\n" + "\n".join(format_ops(ops_edge3)),
        "output": "\n".join(solve(ops_edge3)),
        "category": "edge",
        "description": "Merge and updates"
    })

    # 3. BOUNDARY
    ops_bound1 = [
        ["NEW", "1", "2", "1", "2"],
        ["NEW", "2", "3", "3", "4", "5"],
        ["NEW", "3", "1", "6"],
        ["QUERY"]
    ]
    test_cases.append({
        "input": f"{len(ops_bound1)}\n" + "\n".join(format_ops(ops_bound1)),
        "output": "\n".join(solve(ops_bound1)),
        "category": "boundary",
        "description": "Mixed group sizes"
    })

    # 4. STRESS
    ops_stress = []
    active_ids = []
    next_id = 1
    
    for _ in range(50):
        m = random.randint(1, 5)
        vals = [str(random.randint(1, 1000)) for _ in range(m)]
        ops_stress.append(["NEW", str(next_id), str(m)] + vals)
        active_ids.append(next_id)
        next_id += 1
        
    for _ in range(500):
        action = random.choice(["ADD", "MERGE", "QUERY", "NEW"])
        if action == "NEW":
            m = random.randint(1, 5)
            vals = [str(random.randint(1, 1000)) for _ in range(m)]
            ops_stress.append(["NEW", str(next_id), str(m)] + vals)
            active_ids.append(next_id)
            next_id += 1
        elif action == "ADD":
            if active_ids:
                gid = random.choice(active_ids)
                val = str(random.randint(1, 1000))
                ops_stress.append(["ADD", str(gid), val])
            else:
                ops_stress.append(["QUERY"])
        elif action == "MERGE":
            if len(active_ids) >= 2:
                idx1 = random.randint(0, len(active_ids)-1)
                idx2 = random.randint(0, len(active_ids)-1)
                while idx1 == idx2:
                    idx2 = random.randint(0, len(active_ids)-1)
                id1 = active_ids[idx1]
                id2 = active_ids[idx2]
                ops_stress.append(["MERGE", str(id1), str(id2)])
                active_ids.pop(idx2) 
            else:
                ops_stress.append(["QUERY"])
        elif action == "QUERY":
            ops_stress.append(["QUERY"])
            
    test_cases.append({
        "input": f"{len(ops_stress)}\n" + "\n".join(format_ops(ops_stress)),
        "output": "\n".join(solve(ops_stress)),
        "category": "stress",
        "description": "Stress test"
    })
    
    return test_cases

def main():
    test_cases = generate_test_cases()
    
    yaml_output = {
        "problem_id": "HEP-009",
        "test_cases": test_cases
    }
    
    class BlockDumper(yaml.Dumper):
        def increase_indent(self, flow=False, indentless=False):
            return super(BlockDumper, self).increase_indent(flow, False)

    def str_presenter(dumper, data):
        if '\n' in data:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    yaml.add_representer(str, str_presenter, Dumper=BlockDumper)
    
    output_path = "HEP-009-dynamic-median-of-medians.yaml"
    with open(output_path, 'w') as f:
        yaml.dump(yaml_output, f, Dumper=BlockDumper, default_flow_style=False, sort_keys=False)
    
    print(f"Generated {len(test_cases)} test cases in {output_path}")

if __name__ == "__main__":
    main()
