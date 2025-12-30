import sys

class Solution:
    def max_final_strength(self, strengths: list, priority: list) -> int:
        total_sum = sum(strengths)
        has1 = False
        has2 = False
        has3 = False
        
        for p in priority:
            if p == 1: has1 = True
            elif p == 2: has2 = True
            elif p == 3: has3 = True
            
        penalty = 0
        if has1 and has2 and has3:
            penalty = 2
        elif has1 and has2:
            penalty = 1
        elif has2 and has3:
            penalty = 1
        elif has1 and has3:
            penalty = 2
            
        return total_sum - penalty

def max_final_strength(strengths: list, priority: list) -> int:
    solver = Solution()
    return solver.max_final_strength(strengths, priority)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        strengths = []
        for _ in range(n):
            strengths.append(int(next(iterator)))
        priority = []
        for _ in range(n):
            priority.append(int(next(iterator)))
            
        print(max_final_strength(strengths, priority))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
