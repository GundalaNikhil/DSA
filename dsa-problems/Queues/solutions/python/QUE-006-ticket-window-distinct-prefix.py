from collections import deque

def first_non_repeating(s):
    """Find first non-repeating character after each prefix"""
    count = {}
    queue = deque()
    result = []
    
    for char in s:
        count[char] = count.get(char, 0) + 1
        queue.append(char)
        
        # Remove characters from front if they have count > 1
        while queue and count[queue[0]] > 1:
            queue.popleft()
        
        # Output the first non-repeating character
        if queue:
            result.append(queue[0])
        else:
            result.append('#')
    
    return result

def main():
    import sys
    s = sys.stdin.read().strip()
    result = first_non_repeating(s)
    print(' '.join(result))

if __name__ == "__main__":
    main()
