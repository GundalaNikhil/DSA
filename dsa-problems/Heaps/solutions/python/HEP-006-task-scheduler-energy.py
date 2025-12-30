import sys
import heapq

class Solution:
    def max_tasks(self, E: int, duration: list, gain: list) -> int:
        positive = []
        negative = []
        
        for d, g in zip(duration, gain):
            if g >= d:
                positive.append((d, g))
            else:
                negative.append((d, g))
                
        # Positive: Sort by duration asc
        positive.sort(key=lambda x: x[0])
        
        count = 0
        current_e = E
        
        for d, g in positive:
            if current_e >= d:
                current_e += (g - d)
                count += 1
            else:
                break
                
        peak_e = current_e

        # Negative: Sort by gain desc
        negative.sort(key=lambda x: x[1], reverse=True)
        
        # Max heap for losses (use negative values for min-heap to simulate max-heap)
        pq = []
        current_loss_sum = 0
        
        for d, g in negative:
            loss = d - g
            current_loss_sum += loss
            heapq.heappush(pq, -loss)
            if current_loss_sum + g > peak_e:
                current_loss_sum += heapq.heappop(pq)
                
        return count + len(pq)

def max_tasks(E: int, duration: list, gain: list) -> int:
    solver = Solution()
    return solver.max_tasks(E, duration, gain)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        E = int(next(it))
        duration = []
        gain = []
        for _ in range(n):
            duration.append(int(next(it)))
            gain.append(int(next(it)))
            
        print(max_tasks(E, duration, gain))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
