def chocolate_cut(R: int, C: int) -> str:
    area = R * C
    return "First" if area % 2 == 0 else "Second"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        R = int(next(iterator))
        C = int(next(iterator))
            
        print(chocolate_cut(R, C))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
