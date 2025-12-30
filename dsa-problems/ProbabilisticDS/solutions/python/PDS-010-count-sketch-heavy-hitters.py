import sys

def count_sketch_estimate(count, sign):
    estimates = []
    for c, s in zip(count, sign):
        estimates.append(c * s)
    estimates.sort()
    return estimates[len(estimates) // 2]

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        d = int(next(iterator))
        count = []
        sign = []
        for _ in range(d):
            count.append(int(next(iterator)))
            sign.append(int(next(iterator)))
            
        print(count_sketch_estimate(count, sign))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
