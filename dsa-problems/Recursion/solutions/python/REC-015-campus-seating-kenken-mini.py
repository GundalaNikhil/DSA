def solve_kenken(cages: list[list[int]]) -> list[list[int]]:
    grid = [[0]*4 for _ in range(4)]
    cage_map = {} # (r,c) -> cage_data
    
    for cage in cages:
        target, op_code, length = cage[0], cage[1], cage[2]
        coords = []
        for i in range(length):
            coords.append((cage[3 + 2*i], cage[4 + 2*i]))
        
        cage_data = {'target': target, 'op': chr(op_code), 'coords': coords}
        for r, c in coords:
            cage_map[(r, c)] = cage_data

    def is_valid_placement(r, c, v):
        for j in range(4):
            if grid[r][j] == v: return False
        for i in range(4):
            if grid[i][c] == v: return False
        return True

    def check_cage(r, c):
        data = cage_map[(r, c)]
        values = []
        for rr, cc in data['coords']:
            if grid[rr][cc] == 0: return True # Not full
            values.append(grid[rr][cc])
        
        op = data['op']
        target = data['target']
        
        if op == '+':
            return sum(values) == target
        elif op == '*':
            prod = 1
            for x in values: prod *= x
            return prod == target
        elif op == '-':
            return abs(values[0] - values[1]) == target
        elif op == '/':
            a, b = values[0], values[1]
            return (b != 0 and a % b == 0 and a // b == target) or \
                   (a != 0 and b % a == 0 and b // a == target)
        elif op == '=':
            return values[0] == target
        return False

    def backtrack(r, c):
        if r == 4:
            return True
        
        next_r, next_c = (r, c + 1) if c < 3 else (r + 1, 0)
        
        for v in range(1, 5):
            if is_valid_placement(r, c, v):
                grid[r][c] = v
                if check_cage(r, c):
                    if backtrack(next_r, next_c):
                        return True
                grid[r][c] = 0
        return False

    if backtrack(0, 0):
        return grid
    return []


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
