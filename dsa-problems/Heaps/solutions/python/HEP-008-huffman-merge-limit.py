import sys
import heapq

class Solution:
    def huffman_cost(self, freq: list, m: int) -> int:
        pq = [x for x in freq]
        heapq.heapify(pq)
        
        # Padding
        # (len - 1) % (m - 1) == 0
        while (len(pq) - 1) % (m - 1) != 0:
            heapq.heappush(pq, 0)
            
        total_cost = 0
        
        while len(pq) > 1:
            current_sum = 0
            for _ in range(m):
                current_sum += heapq.heappop(pq)
            
            total_cost += current_sum
            heapq.heappush(pq, current_sum)
            
        return total_cost

def huffman_cost(freq: list, m: int) -> int:
    solver = Solution()
    return solver.huffman_cost(freq, m)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        freq = []
        for _ in range(n):
            freq.append(int(next(it)))
            
        print(huffman_cost(freq, m))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
