import sys

def hit_probability(a: int, b: int, T: int) -> float:
    if a == 0 and b == 0:
        return 1.0

    # Use a dictionary for dynamic storage
    prob = {}
    prob[(0, 0)] = 1.0

    target = (a, b)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for t in range(T):
        next_prob = {}

        for (x, y), p in prob.items():
            if (x, y) == target:
                # Already at target, stay there
                next_prob[(x, y)] = next_prob.get((x, y), 0) + p
            else:
                # Move to one of 4 neighbors with equal probability
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    next_prob[(nx, ny)] = next_prob.get((nx, ny), 0) + p * 0.25

        prob = next_prob

    return prob.get(target, 0.0)

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    a = int(data[0])
    b = int(data[1])
    T = int(data[2])
    print(f"{hit_probability(a, b, T):.6f}")

if __name__ == "__main__":
    main()
