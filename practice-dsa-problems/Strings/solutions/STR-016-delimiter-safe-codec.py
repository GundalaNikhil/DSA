import sys
def encode(strings):
    encoded_parts = []
    for s in strings:
        s_esc = s.replace('\\', '\\\\').replace('|', '\\|')
        encoded_parts.append(s_esc)
    return '|'.join(encoded_parts)

def decode(encoded_string):
    parts = []
    current_part = []
    i = 0
    n = len(encoded_string)
    while i < n:
        if encoded_string[i] == '\\':
            if i + 1 < n:
                parts_char = encoded_string[i + 1]
                current_part.append(parts_char)
                i += 2
            else:
                i += 1
        elif encoded_string[i] == '|':
            parts.append("".join(current_part))
            current_part = []
            i += 1
        else:
            current_part.append(encoded_string[i])
            i += 1
            
    parts.append("".join(current_part))
    return parts

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    q = int(input_data[0])
    ptr = 1
    for _ in range(q):
        if ptr >= len(input_data):
            break
        line = input_data[ptr].split()
        if not line:
            ptr += 1
            continue
        op = line[0]
        if op == 'ENCODE':
            k = int(line[1])
            ptr += 1
            strings_to_encode = []
            for _ in range(k):
                strings_to_encode.append(input_data[ptr])
                ptr += 1
            print(encode(strings_to_encode))
        elif op == 'DECODE':
            encoded_str = line[1] if len(line) > 1 else ""
            ptr += 1
            decoded_parts = decode(encoded_str)
            print(f"{len(decoded_parts)} {' '.join(decoded_parts)}")

if __name__ == '__main__':
    solve()