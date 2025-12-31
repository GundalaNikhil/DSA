def smallest_range(lists: list[list[int]]) -> list[int]:
    k = len(lists)

    # Check if each list has at least 2 elements or handle single element lists
    # For single element list, we need that element in the range
    # For multi-element list, we need at least 2 elements in the range

    events = []
    required = [0] * k

    for i in range(k):
        if not lists[i]:
            return []
        # If list has only 1 element, we need 1. Otherwise we need 2
        required[i] = 1 if len(lists[i]) == 1 else 2
        for val in lists[i]:
            events.append((val, i))

    events.sort()

    counts = [0] * k
    satisfied = 0  # how many lists have met their requirement
    left = 0
    min_len = float('inf')
    res = []

    for right in range(len(events)):
        val, list_id = events[right]
        counts[list_id] += 1

        # When a list reaches its requirement count for the first time
        if counts[list_id] == required[list_id]:
            satisfied += 1

        while satisfied == k:
            # All lists have met requirements
            start_val = events[left][0]
            end_val = events[right][0]
            curr_len = end_val - start_val

            if curr_len < min_len:
                min_len = curr_len
                res = [start_val, end_val]

            # Try to shrink from left
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
