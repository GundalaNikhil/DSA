#!/usr/bin/env python3
"""
QUE-001: Campus Service Line - Test Case Generator
Based on actual problem specification and editorial solution.
"""

import random
from collections import deque

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


def solve_que001(commands):
    """
    Simulate queue operations and return output.
    
    Commands:
    - ENQUEUE x: add x to back
    - DEQUEUE: remove from front and output
    - FRONT: peek front and output
    
    Returns list of outputs for DEQUEUE and FRONT commands.
    """
    queue = deque()
    outputs = []
    
    for cmd in commands:
        parts = cmd.split()
        op = parts[0]
        
        if op == "ENQUEUE":
            x = parts[1]
            queue.append(x)
        elif op == "DEQUEUE":
            if queue:
                outputs.append(queue.popleft())
            else:
                outputs.append("EMPTY")
        elif op == "FRONT":
            if queue:
                outputs.append(queue[0])
            else:
                outputs.append("EMPTY")
    
    return outputs


def generate_que001_cases():
    """Generate test cases for QUE-001: Campus Service Line"""
    cases = {'problem_id': 'QUE_CAMPUS_SERVICE_LINE__4821', 'samples': [], 'public': [], 'hidden': []}
    
    # Sample 1: From problem description
    commands = [
        "ENQUEUE 12",
        "ENQUEUE -5",
        "FRONT",
        "DEQUEUE",
        "FRONT",
        "DEQUEUE"
    ]
    outputs = solve_que001(commands)
    inp = f"{len(commands)}\n" + "\n".join(commands)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Sample 2: Empty queue operations
    commands = [
        "DEQUEUE",
        "FRONT",
        "ENQUEUE 100",
        "FRONT",
        "DEQUEUE",
        "FRONT"
    ]
    outputs = solve_que001(commands)
    inp = f"{len(commands)}\n" + "\n".join(commands)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Sample 3: Multiple operations
    commands = [
        "ENQUEUE 1",
        "ENQUEUE 2",
        "ENQUEUE 3",
        "DEQUEUE",
        "DEQUEUE",
        "ENQUEUE 4",
        "FRONT",
        "DEQUEUE"
    ]
    outputs = solve_que001(commands)
    inp = f"{len(commands)}\n" + "\n".join(commands)
    output = "\n".join(outputs)
    cases['samples'].append({'input': inp, 'output': output})
    
    # Generate public and hidden test cases
    random.seed(42)
    
    for idx in range(35):
        # Generate random command sequence
        num_commands = random.randint(5, 50)
        commands = []
        
        # Balance between enqueues and dequeues
        enqueue_prob = 0.6  # 60% chance to enqueue
        
        for _ in range(num_commands):
            if random.random() < enqueue_prob:
                # ENQUEUE with random student ID
                student_id = random.randint(-1000, 1000)
                commands.append(f"ENQUEUE {student_id}")
            else:
                # DEQUEUE or FRONT
                if random.random() < 0.7:
                    commands.append("DEQUEUE")
                else:
                    commands.append("FRONT")
        
        # Solve
        outputs = solve_que001(commands)
        
        inp = f"{len(commands)}\n" + "\n".join(commands)
        output = "\n".join(outputs) if outputs else ""
        
        test_case = {'input': inp, 'output': output}
        
        if idx < 5:
            cases['public'].append(test_case)
        else:
            cases['hidden'].append(test_case)
    
    return cases


def main():
    """Generate test cases for QUE-001."""
    print("=" * 80)
    print("QUE-001: Campus Service Line - Test Case Generation")
    print("=" * 80)
    
    cases = generate_que001_cases()
    yaml_content = format_testcase_yaml(cases)
    
    output_path = "/Users/nikhilgundala/Desktop/NTB/DSA/dsa-problems/Queues/testcases/QUE-001-campus-service-line.yaml"
    with open(output_path, 'w') as f:
        f.write(yaml_content)
    
    count = len(cases['samples']) + len(cases['public']) + len(cases['hidden'])
    print(f"\n✅ Generated {count} test cases")
    print(f"   Samples: {len(cases['samples'])}")
    print(f"   Public: {len(cases['public'])}")
    print(f"   Hidden: {len(cases['hidden'])}")
    print(f"\n📁 Saved to: {output_path}")
    print("=" * 80)


if __name__ == "__main__":
    main()
