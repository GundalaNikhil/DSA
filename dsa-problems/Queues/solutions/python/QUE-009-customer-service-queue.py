def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')
    
    n = int(input_data[0])
    operations = []
    for i in range(1, n + 1):
        operations.append(input_data[i])
    
    queue = []
    for op in operations:
        parts = op.split()
        if parts[0] == 'PUSH':
            queue.append(int(parts[1]))
        elif parts[0] == 'POP':
            if queue:
                queue.pop(0)
        elif parts[0] == 'FRONT':
            print(queue[0] if queue else -1)

if __name__ == "__main__":
    main()
