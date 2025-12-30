import sys
import math
import heapq

class Solution:
    def process_operations(self, d: int, k: int, operations: list) -> list:
        ln2 = math.log(2.0)
        # key -> (count, bucket, score, version)
        state = {}
        heap = []
        results = []

        for op in operations:
            if op[0] == "ADD":
                key = op[1]
                t = int(op[2])
                bucket = t // d

                if key in state:
                    count, last_bucket, score, version = state[key]
                    if bucket > last_bucket:
                        count *= 0.5 ** (bucket - last_bucket)
                    last_bucket = bucket
                    count += 1.0
                else:
                    count, last_bucket, version = 1.0, bucket, 0

                score = math.log(count) + last_bucket * ln2
                version += 1
                state[key] = (count, last_bucket, score, version)
                heapq.heappush(heap, (-score, key, version))
            else:
                out = []
                used = []
                while heap and len(out) < k:
                    neg_score, key, ver = heapq.heappop(heap)
                    cur = state.get(key)
                    if cur is None or cur[3] != ver:
                        continue
                    out.append(key)
                    used.append((neg_score, key, ver))

                for item in used:
                    heapq.heappush(heap, item)
                results.append("EMPTY" if not out else " ".join(out))

        return results

def process_operations(d: int, k: int, operations: list) -> list:
    solver = Solution()
    return solver.process_operations(d, k, operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        q = int(next(it))
        d = int(next(it))
        k = int(next(it))
        operations = []
        for _ in range(q):
            op = next(it)
            if op == "ADD":
                key = next(it)
                t = next(it)
                operations.append([op, key, t])
            else:
                t = next(it)
                operations.append([op, t])
        
        result = process_operations(d, k, operations)
        print("\n".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
