#!/usr/bin/env python3
"""
Test Case Generators for Critical Problems:
- QUE-002: Circular Shuttle Buffer Overwrite
- HEP-001: Running Median with Delete Threshold
- SEG-001: Range Sum Point Updates Undo

Based on actual problem specifications and editorial solutions.
"""

import random
import heapq
from collections import deque, Counter

def format_testcase_yaml(data):
    """Format test cases in proper YAML with |- syntax."""
    lines = []
    lines.append(f"problem_id: {data['problem_id']}")
    
    for section_name in ['samples', 'public', 'hidden']:
        if section_name not in data or not data[section_name]:
            continue
        lines.append(f"{section_name}:")
        for case in data[section_name]:
            lines.append("- input: |-")
            for line in case['input'].strip().split('\n'):
                lines.append(f"    {line}")
            lines.append("  output: |-")
            for line in case['output'].strip().split('\n'):
                lines.append(f"    {line}")
    
    return '\n'.join(lines)


# ============================================================================
# QUE-002: Circular Shuttle Buffer Overwrite
# ============================================================================

class CircularBuffer:
    """Circular buffer with overwrite support."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [0] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0
    
    def enq(self, x):
        """ENQ: Add to rear if not full."""
        if self.count == self.capacity:
            return "false"
        self.buffer[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1
        return "true"
    
    def enq_ovr(self, x):
        """ENQ_OVR: Add to rear, overwrite oldest if full."""
        if self.count < self.capacity:
            self.buffer[self.tail] = x
            self.tail = (self.tail + 1) % self.capacity
            self.count += 1
            return "NONE"
        else:
            # Overwrite
            old_val = self.buffer[self.head]
            self.buffer[self.tail] = x
            self.head = (self.head + 1) % self.capacity
            self.tail = (self.tail + 1) % self.capacity
            return str(old_val)
    
    def deq(self):
        """DEQ: Remove from front."""
        if self.count == 0:
            return "EMPTY"
        val = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return str(val)
    
    def front(self):
        """FRONT: Peek at front."""
        if self.count == 0:
            return "EMPTY"
        return str(self.buffer[self.head])
    
    def rear(self):
        """REAR: Peek at rear."""
        if self.count == 0:
            return "EMPTY"
        rear_idx = (self.tail - 1 + self.capacity) % self.capacity
        return str(self.buffer[rear_idx])
    
    def isempty(self):
        """ISEMPTY: Check if empty."""
        return "true" if self.count == 0 else "false"
    
    def isfull(self):
        """ISFULL: Check if full."""
        return "true" if self.count == self.capacity else "false"


def solve_que002(capacity, commands):
    """Solve QUE-002: Circular Buffer operations."""
    cb = CircularBuffer(capacity)
    outputs = []
    
    for cmd in commands:
        parts = cmd.split()
        op = parts[0]
        
        if op == "ENQ":
            x = int(parts[1])
            outputs.append(cb.enq(x))
        elif op == "ENQ_OVR":
            x = int(parts[1])
            outputs.append(cb.enq_ovr(x))
        elif op == "DEQ":
            outputs.append(cb.deq())
        elif op == "FRONT":
            outputs.append(cb.front())
        elif op == "REAR":
            outputs.append(cb.rear())
        elif op == "ISEMPTY":
            outputs.append(cb.isempty())
        elif op == "ISFULL":
            outputs.append(cb.isfull())
    
    return outputs


def generate_que002_cases():
    """Generate test cases for QUE-002."""
    cases = {'problem_id': 'QUE_CIRCULAR_SHUTTLE_BUFFER_OVERWRITE__7314', 'samples': [], 'public': [], 'hidden': []}
    
    # Sample 1: From problem description
    capacity = 2
    commands = ["ENQ 5", "ENQ 6", "ENQ 7", "ENQ_OVR 8", "FRONT", "REAR"]
    outputs = solve_que002(capacity, commands)
    inp = f"{capacity}\n{len(commands)}\n" + "\n".join(commands)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Sample 2: Test DEQ and empty
    capacity = 3
    commands = ["ENQ 1", "ENQ 2", "DEQ", "FRONT", "DEQ", "ISEMPTY"]
    outputs = solve_que002(capacity, commands)
    inp = f"{capacity}\n{len(commands)}\n" + "\n".join(commands)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Sample 3: Test overwrite multiple times
    capacity = 2
    commands = ["ENQ 10", "ENQ 20", "ENQ_OVR 30", "ENQ_OVR 40", "DEQ", "DEQ", "ISEMPTY"]
    outputs = solve_que002(capacity, commands)
    inp = f"{capacity}\n{len(commands)}\n" + "\n".join(commands)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Generate public and hidden test cases
    random.seed(100)
    
    for idx in range(35):
        capacity = random.randint(2, 20)
        num_commands = random.randint(5, 50)
        commands = []
        
        for _ in range(num_commands):
            op_type = random.choice(['ENQ', 'ENQ_OVR', 'DEQ', 'FRONT', 'REAR', 'ISEMPTY', 'ISFULL'])
            
            if op_type in ['ENQ', 'ENQ_OVR']:
                val = random.randint(-1000, 1000)
                commands.append(f"{op_type} {val}")
            else:
                commands.append(op_type)
        
        outputs = solve_que002(capacity, commands)
        inp = f"{capacity}\n{len(commands)}\n" + "\n".join(commands)
        output = "\n".join(outputs)
        
        test_case = {'input': inp, 'output': output}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# HEP-001: Running Median with Delete Threshold
# ============================================================================

def solve_hep001(operations, threshold):
    """
    Solve HEP-001: Running Median with threshold.
    Uses sorted list for simplicity (can optimize with two heaps).
    """
    multiset = []
    outputs = []
    
    for op in operations:
        parts = op.split()
        cmd = parts[0]
        
        if cmd == "ADD":
            x = int(parts[1])
            # Insert in sorted order
            import bisect
            bisect.insort(multiset, x)
        elif cmd == "DEL":
            x = int(parts[1])
            # Remove one occurrence
            if x in multiset:
                multiset.remove(x)
        elif cmd == "MEDIAN":
            if len(multiset) == 0:
                outputs.append("EMPTY")
            elif len(multiset) < threshold:
                outputs.append("NA")
            else:
                # Lower middle (for even size)
                mid_idx = (len(multiset) - 1) // 2
                outputs.append(str(multiset[mid_idx]))
    
    return outputs


def generate_hep001_cases():
    """Generate test cases for HEP-001."""
    cases = {'problem_id': 'HEP_RUNNING_MEDIAN_DELETE_THRESHOLD__4217', 'samples': [], 'public': [], 'hidden': []}
    
    # Sample 1: From problem description
    threshold = 2
    operations = ["ADD 1", "ADD 5", "DEL 1", "MEDIAN"]
    outputs = solve_hep001(operations, threshold)
    inp = f"{len(operations)} {threshold}\n" + "\n".join(operations)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Sample 2: Test with threshold met
    threshold = 2
    operations = ["ADD 3", "ADD 7", "ADD 1", "MEDIAN", "DEL 7", "MEDIAN"]
    outputs = solve_hep001(operations, threshold)
    inp = f"{len(operations)} {threshold}\n" + "\n".join(operations)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Sample 3: Test empty
    threshold = 0
    operations = ["MEDIAN", "ADD 5", "MEDIAN", "DEL 5", "MEDIAN"]
    outputs = solve_hep001(operations, threshold)
    inp = f"{len(operations)} {threshold}\n" + "\n".join(operations)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Generate public and hidden test cases
    random.seed(200)
    
    for idx in range(35):
        threshold = random.randint(0, 10)
        num_ops = random.randint(10, 50)
        operations = []
        
        # Build operations
        current_values = set()
        for _ in range(num_ops):
            op_type = random.choice(['ADD', 'DEL', 'MEDIAN'])
            
            if op_type == 'ADD':
                val = random.randint(-100, 100)
                operations.append(f"ADD {val}")
                current_values.add(val)
            elif op_type == 'DEL' and current_values:
                val = random.choice(list(current_values))
                operations.append(f"DEL {val}")
            else:
                operations.append("MEDIAN")
        
        outputs = solve_hep001(operations, threshold)
        inp = f"{len(operations)} {threshold}\n" + "\n".join(operations)
        output = "\n".join(outputs) if outputs else ""
        
        test_case = {'input': inp, 'output': output}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# SEG-001: Range Sum Point Updates Undo
# ============================================================================

class SegmentTreeWithUndo:
    """Segment tree with undo support."""
    
    def __init__(self, arr, mod):
        self.n = len(arr)
        self.arr = arr[:]
        self.mod = mod
        self.update_history = []  # Stack of (index, old_value)
    
    def update(self, i, x):
        """UPDATE: Set arr[i] = x."""
        self.update_history.append((i, self.arr[i]))
        self.arr[i] = x
    
    def query(self, l, r):
        """QUERY: Sum of arr[l..r] modulo M."""
        total = sum(self.arr[l:r+1])
        return total % self.mod
    
    def undo(self, k):
        """UNDO: Revert last k updates."""
        k = min(k, len(self.update_history))
        for _ in range(k):
            if self.update_history:
                idx, old_val = self.update_history.pop()
                self.arr[idx] = old_val


def solve_seg001(n, arr, mod, operations):
    """Solve SEG-001: Range sum with undo."""
    seg = SegmentTreeWithUndo(arr, mod)
    outputs = []
    
    for op in operations:
        parts = op.split()
        cmd = parts[0]
        
        if cmd == "UPDATE":
            i = int(parts[1])
            x = int(parts[2])
            seg.update(i, x)
        elif cmd == "QUERY":
            l = int(parts[1])
            r = int(parts[2])
            result = seg.query(l, r)
            outputs.append(str(result))
        elif cmd == "UNDO":
            k = int(parts[1])
            seg.undo(k)
    
    return outputs


def generate_seg001_cases():
    """Generate test cases for SEG-001."""
    cases = {'problem_id': 'SEG_RANGE_SUM_POINT_UPDATES_UNDO__5472', 'samples': [], 'public': [], 'hidden': []}
    
    # Sample 1: From problem description
    n, mod = 5, 1000
    arr = [1, 2, 3, 4, 5]
    operations = [
        "QUERY 1 3",
        "UPDATE 2 10",
        "QUERY 0 4",
        "UNDO 1",
        "QUERY 0 4"
    ]
    outputs = solve_seg001(n, arr, mod, operations)
    inp = f"{n} {len(operations)} {mod}\n"
    inp += " ".join(map(str, arr)) + "\n"
    inp += "\n".join(operations)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Sample 2: Multiple updates and undo
    n, mod = 4, 100
    arr = [10, 20, 30, 40]
    operations = [
        "QUERY 0 3",
        "UPDATE 0 5",
        "UPDATE 1 15",
        "QUERY 0 3",
        "UNDO 2",
        "QUERY 0 3"
    ]
    outputs = solve_seg001(n, arr, mod, operations)
    inp = f"{n} {len(operations)} {mod}\n"
    inp += " ".join(map(str, arr)) + "\n"
    inp += "\n".join(operations)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Sample 3: Test edge cases
    n, mod = 3, 50
    arr = [5, 10, 15]
    operations = [
        "QUERY 0 2",
        "UPDATE 1 100",
        "QUERY 0 2",
        "UNDO 1",
        "QUERY 0 2"
    ]
    outputs = solve_seg001(n, arr, mod, operations)
    inp = f"{n} {len(operations)} {mod}\n"
    inp += " ".join(map(str, arr)) + "\n"
    inp += "\n".join(operations)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Generate public and hidden test cases
    random.seed(300)
    
    for idx in range(35):
        n = random.randint(5, 30)
        mod = random.randint(100, 10000)
        arr = [random.randint(-100, 100) for _ in range(n)]
        
        num_ops = random.randint(5, 40)
        operations = []
        
        for _ in range(num_ops):
            op_type = random.choice(['UPDATE', 'QUERY', 'UNDO'])
            
            if op_type == 'UPDATE':
                i = random.randint(0, n-1)
                x = random.randint(-100, 100)
                operations.append(f"UPDATE {i} {x}")
            elif op_type == 'QUERY':
                l = random.randint(0, n-1)
                r = random.randint(l, n-1)
                operations.append(f"QUERY {l} {r}")
            else:
                k = random.randint(1, 5)
                operations.append(f"UNDO {k}")
        
        outputs = solve_seg001(n, arr, mod, operations)
        
        inp = f"{n} {len(operations)} {mod}\n"
        inp += " ".join(map(str, arr)) + "\n"
        inp += "\n".join(operations)
        output = "\n".join(outputs) if outputs else ""
        
        test_case = {'input': inp, 'output': output}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


# ============================================================================
# Main Generation
# ============================================================================

def main():
    """Generate test cases for all three critical problems."""
    print("=" * 80)
    print("CRITICAL PROBLEMS TEST CASE GENERATION")
    print("=" * 80)
    
    base_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems"
    
    problems = [
        ("QUE-002", "circular-shuttle-buffer-overwrite", "Queues", generate_que002_cases),
        ("HEP-001", "running-median-with-delete-threshold", "Heaps", generate_hep001_cases),
        ("SEG-001", "range-sum-point-updates-undo", "SegmentTree", generate_seg001_cases),
    ]
    
    total_tests = 0
    
    for prob_id, slug, topic, generator_func in problems:
        print(f"\n[{prob_id}] Generating {slug}...")
        
        cases = generator_func()
        yaml_content = format_testcase_yaml(cases)
        
        output_path = f"{base_path}/{topic}/testcases/{prob_id}-{slug}.yaml"
        with open(output_path, 'w') as f:
            f.write(yaml_content)
        
        count = len(cases['samples']) + len(cases['public']) + len(cases['hidden'])
        total_tests += count
        
        print(f"✅ {prob_id}: {count} test cases")
        print(f"   Samples: {len(cases['samples'])}, Public: {len(cases['public'])}, Hidden: {len(cases['hidden'])}")
        print(f"   Saved to: {output_path}")
    
    print("\n" + "=" * 80)
    print(f"✅ COMPLETE: 3 files, {total_tests} test cases generated")
    print("=" * 80)


if __name__ == "__main__":
    main()
