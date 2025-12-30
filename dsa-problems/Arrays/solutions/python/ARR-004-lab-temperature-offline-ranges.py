import sys

def process_temperature_queries(temps: list[int], queries: list[tuple]) -> list[int]:
    n = len(temps)
    diff = [0] * (n + 1)
    sum_queries = []
    
    # 1. Process Updates
    for q in queries:
        if q[0] == "add":
            l, r, x = q[1], q[2], q[3]
            diff[l] += x
            if r + 1 < n:
                diff[r + 1] -= x
        else:
            sum_queries.append(q)
            
    # 2. Reconstruct & Build Prefix Sums
    # P[i] = sum(final_temps[:i])
    P = [0] * (n + 1)
    current_add = 0
    
    for i in range(n):
        current_add += diff[i]
        final_val = temps[i] + current_add
        P[i + 1] = P[i] + final_val
        
    # 3. Answer Sum Queries
    results = []
    for q in sum_queries:
        l, r = q[1], q[2]
        results.append(P[r + 1] - P[l])
        
    return results

def main():
    n = int(input())
    temps = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        parts = input().split()
        if parts[0] == "add":
            queries.append((parts[0], int(parts[1]), int(parts[2]), int(parts[3])))
        else:
            queries.append((parts[0], int(parts[1]), int(parts[2])))

    result = process_temperature_queries(temps, queries)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()


