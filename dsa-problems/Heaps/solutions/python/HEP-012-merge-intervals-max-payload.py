import sys

class Solution:
    def merge_intervals(self, intervals: list) -> list:
        if not intervals:
            return []
            
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        current = intervals[0]
        
        for i in range(1, len(intervals)):
            next_int = intervals[i]
            
            if next_int[0] <= current[1]:
                # Merge
                current[1] = max(current[1], next_int[1])
                current[2] = max(current[2], next_int[2])
            else:
                merged.append(current)
                current = next_int
                
        merged.append(current)
        return merged

def merge_intervals(intervals: list) -> list:
    solver = Solution()
    return solver.merge_intervals(intervals)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        intervals = []
        for _ in range(n):
            start = int(next(it))
            end = int(next(it))
            payload = int(next(it))
            intervals.append([start, end, payload])
            
        result = merge_intervals(intervals)
        print(len(result))
        for row in result:
            print(f"{row[0]} {row[1]} {row[2]}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
