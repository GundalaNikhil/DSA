import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    k = int(input_data[ptr])
    ptr += 1
    a = []
    for _ in range(n):
        a.append(int(input_data[ptr]))
        ptr += 1
        
    b = []
    for x in a:
        if x >= 0:
            b.append(x)
        else:
            b.append(-((abs(x) + 1) // 2))
            
   
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + b[i]
        
    ans = -float("inf")
    min_pref = float("inf") 
    
    
    for j in range(k, n + 1):
        if j - k == 0:
            min_pref = 0 
        else:
            pass
            
    min_pref = 0 
    
    for j in range(k, n + 1):
        current_split = prefix[j-k]
        if current_split < min_pref:
            min_pref = current_split
            
        current_val = prefix[j] - min_pref
        if current_val > ans:
            ans = current_val
            
    print(ans)

if __name__ == "__main__":
    solve()
