import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    ptr = 0
    capacity = int(input_data[ptr])
    ptr += 1
    decay = int(input_data[ptr])
    ptr += 1
    q = int(input_data[ptr])
    ptr += 1
    cache = {}
    for _ in range(q):
        op = input_data[ptr]
        ptr += 1
        if op == 'GET':
            key = input_data[ptr]
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            if key in cache:
                val, _ = cache[key]
                cache[key] = (val, t)
                print(val)
            else:
                print("-1")
        elif op == 'PUT':
            key = input_data[ptr]
            ptr += 1
            val = int(input_data[ptr])
            ptr += 1
            t = int(input_data[ptr])
            ptr += 1
            if key in cache:
                cache[key] = (val, t)
            else:
                if len(cache) >= capacity:
                    to_evict = None
                    min_t = float('inf')
                    for k, (v, last_t) in cache.items():
                        if last_t < min_t:
                            min_t = last_t
                            to_evict = k
                    if to_evict:
                        del cache[to_evict]
                cache[key] = (val, t)
if __name__ == '__main__':
    solve()