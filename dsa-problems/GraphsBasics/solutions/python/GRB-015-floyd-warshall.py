import sys

def floyd_warshall(dist: list[list[int]]):
    n = len(dist)
    INF = 10**15
    
    # Preprocess
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == -1:
                dist[i][j] = INF
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
    # Negative Cycle Check
    for i in range(n):
        if dist[i][i] < 0:
            return None
            
    # Postprocess
    for i in range(n):
        for j in range(n):
            if dist[i][j] >= INF // 2:
                dist[i][j] = -1
                
    return dist

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dist[i][j] = int(next(iterator))
                
        ans = floyd_warshall(dist)
        if ans is None:
            print("NEGATIVE CYCLE")
        else:
            out = []
            for i in range(n):
                out.append(" ".join(str(x) for x in ans[i]))
            print("\n".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
