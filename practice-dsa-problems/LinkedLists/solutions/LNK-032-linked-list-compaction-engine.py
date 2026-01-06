import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    s_limit = int(input_data[ptr])
    ptr += 1
    current_list = []
    current_list = []
    for _ in range(n):
        label = input_data[ptr]
        ptr += 1
        size = int(input_data[ptr])
        ptr += 1
        current_list.append([label, size])
        
    # Compaction logic
    while True:
        merged = False
        new_list = []
        i = 0
        while i < len(current_list):
            if not new_list:
                new_list.append(current_list[i])
                i += 1
            else:
                last_label, last_size = new_list[-1]
                curr_label, curr_size = current_list[i]
                
                if last_label == curr_label and last_size + curr_size <= s_limit:
                    new_list[-1][1] += curr_size
                    merged = True
                    i += 1
                else:
                    new_list.append(current_list[i])
                    i += 1
                    
        current_list = new_list
        if not merged:
            break
            
    print(len(current_list))
    for label, size in current_list:
        print(f"{label} {size}")


if __name__ == "__main__":
    solve()
