from typing import List
import sys

def process_operations(k: int, operations: List[List[str]]) -> List[str]:
    buffer = [0] * k
    head = 0
    tail = 0
    count = 0
    result = []

    for op_data in operations:
        cmd = op_data[0]

        if cmd == "ENQ":
            if count == k:
                result.append("false")
            else:
                buffer[tail] = int(op_data[1])
                tail = (tail + 1) % k
                count += 1
                result.append("true")

        elif cmd == "ENQ_OVR":
            val = int(op_data[1])
            if count == k:
                # Overwrite and return the overwritten value
                overwritten = buffer[head]
                buffer[head] = val
                head = (head + 1) % k
                tail = (tail + 1) % k
                result.append(str(overwritten))
            else:
                # Just add
                buffer[tail] = val
                tail = (tail + 1) % k
                count += 1
                result.append("NONE")

        elif cmd == "DEQ":
            if count == 0:
                result.append("EMPTY")
            else:
                result.append(str(buffer[head]))
                head = (head + 1) % k
                count -= 1

        elif cmd == "FRONT":
            if count == 0:
                result.append("EMPTY")
            else:
                result.append(str(buffer[head]))

        elif cmd == "REAR":
            if count == 0:
                result.append("EMPTY")
            else:
                idx = (tail - 1 + k) % k
                result.append(str(buffer[idx]))

        elif cmd == "ISEMPTY":
            result.append("true" if count == 0 else "false")

        elif cmd == "ISFULL":
            result.append("true" if count == k else "false")

        elif cmd == "SIZE":
            result.append(str(count))

        else:
            result.append("NONE")

    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        k = int(next(iterator))
        m = int(next(iterator))
        operations = []
        for _ in range(m):
            op = next(iterator)
            if op in ("ENQ", "ENQ_OVR"):
                val = next(iterator)
                operations.append([op, val])
            else:
                operations.append([op])

        result = process_operations(k, operations)
        print("\n".join(result))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
