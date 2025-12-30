import sys

def max_or_subarray_leq_k(a: list[int], K: int) -> int:
    n = len(a)
    bit_counts = [0] * 32
    current_or = 0
    left = 0
    max_len = 0
    
    for right in range(n):
        val = a[right]
        # Add to window
        for i in range(31):
            if (val >> i) & 1:
                bit_counts[i] += 1
                if bit_counts[i] == 1:
                    current_or |= (1 << i)
                    
        # Shrink
        while left <= right and current_or > K:
            remove_val = a[left]
            for i in range(31):
                if (remove_val >> i) & 1:
                    bit_counts[i] -= 1
                    if bit_counts[i] == 0:
                        current_or &= ~(1 << i)
            left += 1
            
        if current_or <= K:
            max_len = max(max_len, right - left + 1)
            
    return max_len

def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    if not data: return

    ptr = 0
    n = int(data[ptr]); ptr += 1
    a = []
    for _ in range(n):
        a.append(int(data[ptr])); ptr += 1

    K = int(data[ptr]); ptr += 1

    result = max_or_subarray_leq_k(a, K)
    print(result)

if __name__ == "__main__":
    main()
