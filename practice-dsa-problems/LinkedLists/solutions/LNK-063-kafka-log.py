import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
    
    log = []
    
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        
        if op == "APPEND":
            key = int(input_data[ptr])
            ptr += 1
            val = int(input_data[ptr])
            ptr += 1
            time = int(input_data[ptr])
            ptr += 1
            log.append((key, val, time))
        elif op == "COMPACT":
            latest = {}
            # Identify latest indices for each key
            for i, (k, v, t) in enumerate(log):
                latest[k] = i
                
            new_log = []
            for i, record in enumerate(log):
                if latest[record[0]] == i:
                    new_log.append(record)
            log = new_log
        elif op == "READ":
            offset = int(input_data[ptr])
            ptr += 1
            if 1 <= offset <= len(log):
                k, v, t = log[offset - 1]
                print(f"{k} {v} {t}")
            else:
                print("-1")

if __name__ == "__main__":
    solve()
