import sys

def orientation(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> str:
    cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if cross == 0:
        return "collinear"
    return "counterclockwise" if cross > 0 else "clockwise"

def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    data = input_data.split()
    x1, y1, x2, y2, x3, y3 = map(int, data)

    result = orientation(x1, y1, x2, y2, x3, y3)
    print(result)

if __name__ == "__main__":
    main()
