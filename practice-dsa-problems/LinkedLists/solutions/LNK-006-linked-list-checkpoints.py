import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    curr_list = []
    for _ in range(n):
        curr_list.append(int(input_data[ptr]))
        ptr += 1
        
    q_count = int(input_data[ptr])
    ptr += 1
    
    checkpoints = {}
    
    for _ in range(q_count):
        op = input_data[ptr]
        ptr += 1
        
        if op == "INS":
            pos = int(input_data[ptr])
            ptr += 1
            x = int(input_data[ptr])
            ptr += 1
            # Adjust pos for 0-index? Code used `pos - 1`
            curr_list.insert(pos - 1, x)
            
        elif op == "DEL":
            pos = int(input_data[ptr])
            ptr += 1
            if 1 <= pos <= len(curr_list):
                curr_list.pop(pos - 1)
                
        elif op == "CKPT":
            cid = input_data[ptr]
            ptr += 1
            checkpoints[cid] = list(curr_list)
            
        elif op == "ROLL":
            cid = input_data[ptr]
            ptr += 1
            if cid in checkpoints:
                curr_list = list(checkpoints[cid])
                
        elif op == "GET":
            pos = int(input_data[ptr])
            ptr += 1
            if 1 <= pos <= len(curr_list):
                print(curr_list[pos - 1])
            else:
                print("-1")


if __name__ == "__main__":
    solve()
