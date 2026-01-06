import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    quantum = int(input_data[ptr])
    ptr += 1
    processes = []
    for _ in range(n):
        pid = int(input_data[ptr])
        ptr += 1
        arrival = int(input_data[ptr])
        ptr += 1
        burst = int(input_data[ptr])
        ptr += 1
        processes.append([pid, arrival, burst])
        
    processes.sort(key=lambda x: x[1])
    ready_queue = deque()
    completion_times = {}
    time = 0
    p_idx = 0
    
    while p_idx < n or ready_queue:
        if not ready_queue:
            time = max(time, processes[p_idx][1])
            while p_idx < n and processes[p_idx][1] <= time:
                ready_queue.append(processes[p_idx])
                p_idx += 1
                
        if ready_queue:
            curr = ready_queue.popleft()
            pid, arrival, burst = curr
            exec_time = min(burst, quantum)
            time += exec_time
            burst -= exec_time
            
            while p_idx < n and processes[p_idx][1] <= time:
                ready_queue.append(processes[p_idx])
                p_idx += 1
                
            if burst > 0:
                ready_queue.append([pid, arrival, burst])
            else:
                completion_times[pid] = time
                
    for i in range(1, n + 1):
        if i in completion_times:
            print(f"{i} {completion_times[i]}")


if __name__ == "__main__":
    solve()
