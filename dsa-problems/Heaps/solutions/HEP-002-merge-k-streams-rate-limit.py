import sys
import heapq

class Solution:
    def merge_streams(self, streams: list, r: int) -> list:
        k = len(streams)
        indices = [0] * k
        usage = [0] * k
        
        # Min-heap stores (value, stream_index)
        pq = []
        
        # Initial population
        for i in range(k):
            if streams[i]:
                heapq.heappush(pq, (streams[i][0], i))
                indices[i] += 1
                
        result = []
        blocked = []
        
        while pq:
            val, s_idx = heapq.heappop(pq)
            result.append(val)
            
            usage[s_idx] += 1
            
            if usage[s_idx] < r:
                # Still active in round
                if indices[s_idx] < len(streams[s_idx]):
                    next_val = streams[s_idx][indices[s_idx]]
                    heapq.heappush(pq, (next_val, s_idx))
                    indices[s_idx] += 1
            else:
                # Blocked
                blocked.append(s_idx)
                
            # Check if round ended
            if not pq and blocked:
                # Start new round
                for idx in blocked:
                    usage[idx] = 0
                    if indices[idx] < len(streams[idx]):
                        next_val = streams[idx][indices[idx]]
                        heapq.heappush(pq, (next_val, idx))
                        indices[idx] += 1
                blocked = []
                
        return result

def merge_streams(streams: list, r: int) -> list:
    solver = Solution()
    return solver.merge_streams(streams, r)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        k = int(next(it))
        r = int(next(it))
        streams = []
        for _ in range(k):
            m = int(next(it))
            stream = []
            for _ in range(m):
                stream.append(int(next(it)))
            streams.append(stream)
            
        result = merge_streams(streams, r)
        print(" ".join(map(str, result)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
