import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    initial_list = []
    initial_list = []
    for _ in range(n):
        initial_list.append(int(input_data[ptr]))
        ptr += 1
        
    p_count = int(input_data[ptr])
    ptr += 1
    
    winners = {}
    for _ in range(p_count):
        pos = int(input_data[ptr])
        ptr += 1
        val = int(input_data[ptr])
        ptr += 1
        prio = int(input_data[ptr])
        ptr += 1
        time = int(input_data[ptr])
        ptr += 1
        pid = int(input_data[ptr])
        ptr += 1
        
        new_proposal = (prio, -time, -pid, val)
        if pos not in winners or new_proposal > winners[pos]:
            winners[pos] = new_proposal
            
    result = []
    for i in range(1, n + 2):
        if i in winners:
            result.append(winners[i][3])
        if i <= n:
            result.append(initial_list[i - 1])
            
    print(*(result))


if __name__ == "__main__":
    solve()
