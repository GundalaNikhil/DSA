import sys

class Trie:
    def __init__(self):
        # [left_child, right_child] indices
        self.nodes = [[0, 0]]
        self.count = [0]
    
    def insert(self, x):
        u = 0
        self.count[u] += 1 # Root count
        for i in range(30, -1, -1):
            bit = (x >> i) & 1
            if not self.nodes[u][bit]:
                self.nodes[u][bit] = len(self.nodes)
                self.nodes.append([0, 0])
                self.count.append(0)
            u = self.nodes[u][bit]
            self.count[u] += 1
            
    def count_less_equal(self, val, limit):
        # Count elements y in Trie such that (val ^ y) <= limit
        cnt = 0
        u = 0
        for i in range(30, -1, -1):
            v_bit = (val >> i) & 1
            l_bit = (limit >> i) & 1
            
            desired_bit_for_less = v_bit # yields result 0
            desired_bit_for_equal = 1 - v_bit # yields result 1
            
            if l_bit == 1:
                child_less = self.nodes[u][desired_bit_for_less]
                if child_less:
                    cnt += self.count[child_less]
                    
                u = self.nodes[u][desired_bit_for_equal]
            else:
                u = self.nodes[u][desired_bit_for_less]
                
            if u == 0:
                break
                
        if u != 0:
            cnt += self.count[u]
            
        return cnt

def count_pairs_le(mid, pref, n):
    # Count pairs (i, j) i < j such that pref[i] ^ pref[j] <= mid.
    total = 0
    trie = Trie()
    trie.insert(pref[0]) # usually 0
    
    for i in range(1, n + 1):
        # For current pref[i], count previous pref[j] such that XOR <= mid
        cnt = trie.count_less_equal(pref[i], mid)
        total += cnt
        trie.insert(pref[i])
        
    return total

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        k = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] ^ a[i]
        
    low = 0
    high = (1 << 31) - 1 # 31 bits
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        # Check if rank of mid >= k
        # i.e., at least k subarrays have xor <= mid
        if count_pairs_le(mid, pref, n) >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == "__main__":
    solve()