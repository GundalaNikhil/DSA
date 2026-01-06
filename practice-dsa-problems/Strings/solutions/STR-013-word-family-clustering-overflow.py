import sys
from collections import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    words = input_data[2:]
    families = defaultdict(list)
    appearance_order = []
    for word in words:
        key = "".join(sorted(word))
        if key not in families:
            appearance_order.append(key)
            families[key].append(word)
    
    # Process grouping and printing
    all_groups = []
    for key in appearance_order:
        family_words = families[key]
        num_full_groups = len(family_words) // k
        
        for i in range(num_full_groups):
            group = family_words[i * k : (i + 1) * k]
            all_groups.append(" ".join(group))
            
        leftovers = family_words[num_full_groups * k :]
        if leftovers:
            all_groups.append("".join(leftovers))
            
    print(len(all_groups))
    for group in all_groups:
        print(group)


if __name__ == "__main__":
    solve()
