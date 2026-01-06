import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    a_count = int(input_data[ptr])
    ptr += 1
    k_limit = int(input_data[ptr])
    ptr += 1
    values = []
    for _ in range(a_count):
        values.append(int(input_data[ptr]))
        ptr += 1
    current_sums = {0}
    
    for _ in range(n):
        new_sums = set()
        for s in current_sums:
            for v in values:
                new_sums.add(s + v)
                
        # Pruning based on k_limit
        if len(new_sums) > k_limit:
            sorted_sums = sorted(list(new_sums), reverse=True)
            current_sums = set(sorted_sums[:k_limit])
        else:
            current_sums = new_sums
            
    if not current_sums:
        print(0)
    else:
        print(max(current_sums))


if __name__ == "__main__":
    solve()
