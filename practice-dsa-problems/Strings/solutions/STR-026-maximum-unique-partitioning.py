import sys


def solve():
    s = sys.stdin.read().strip()
    if not s:
        print(0)
        print("")
        return
    n = len(s)
    best_partition = []


def backtrack(start, current_set, current_list):
    nonlocal best_partition
    if start == n:
        if len(current_list) > len(best_partition):
            best_partition = list(current_list)
            return
        if len(current_list) + (n - start) <= len(best_partition):
            return
        for length in range(1, n - start + 1):
            sub = s[start : start + length]
            if sub not in current_set:
                current_set.add(sub)
                current_list.append(sub)
                backtrack(start + length, current_set, current_list)
                current_list.pop()
                current_set.remove(sub)
                
    backtrack(0, set(), [])
    print(len(best_partition))
    print(" ".join(best_partition))


if __name__ == "__main__":
    solve()
