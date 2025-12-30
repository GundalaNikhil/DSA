import sys

def min_overtime_cost(n: int, H: int, shifts: list) -> int:
    total_standard = 0
    min_rate = float('inf')
    
    for l, p in shifts:
        total_standard += l
        if p < min_rate:
            min_rate = p
            
    if total_standard >= H:
        return 0
        
    needed = H - total_standard
    return needed * min_rate

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
        
    iterator = iter(data)
    n = int(next(iterator))
    H = int(next(iterator))
    
    shifts = []
    for _ in range(n):
        l = int(next(iterator))
        p = int(next(iterator))
        shifts.append([l, p])

    result = min_overtime_cost(n, H, shifts)
    print(result)

if __name__ == "__main__":
    main()
