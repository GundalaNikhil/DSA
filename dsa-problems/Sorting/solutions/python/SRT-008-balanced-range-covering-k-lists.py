def smallest_range(lists: list[list[int]]) -> list[int]:
    events = []
    k = len(lists)
    required = [0] * k
    
    for i in range(k):
        if not lists[i]:
            return []
        required[i] = 1  # need at least 1 from each list
        for val in lists[i]:
            events.append((val, i))
            
    events.sort(key=lambda x: x[0])
    
    counts = [0] * k
    satisfied = 0
    left = 0
    min_len = float('inf')
    res = []
    
    for right in range(len(events)):
        val, list_id = events[right]
        counts[list_id] += 1
        
        if counts[list_id] == required[list_id]:
            satisfied += 1
        elif counts[list_id] > required[list_id]:
            # Already satisfied, shouldn't increment again
            pass
            
        while satisfied == k:
            start_val = events[left][0]
            end_val = val
            curr_len = end_val - start_val
            
            if curr_len < min_len:
                min_len = curr_len
                res = [start_val, end_val]
                
            left_list_id = events[left][1]
            counts[left_list_id] -= 1
            if counts[left_list_id] < required[left_list_id]:
                satisfied -= 1
            left += 1
            
    return res

def main():
    k = int(input())
    lists = []
    for _ in range(k):
        m = int(input())
        lst = list(map(int, input().split()))
        lists.append(lst)
    result = smallest_range(lists)
    if result:
        print(result[0], result[1])
    else:
        print('NONE')

if __name__ == "__main__":
    main()
