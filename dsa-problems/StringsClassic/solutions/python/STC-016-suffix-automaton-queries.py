import sys
sys.setrecursionlimit(200000)

class State:
    def __init__(self, length=0, link=-1):
        self.len = length
        self.link = link
        self.next = {}
        self.cnt = 0

def count_occurrences(s: str, queries: list[str]) -> list[int]:
    # Initialize SAM
    st = [State()]
    last = 0
    
    # Extend function
    def extend(c):
        nonlocal last
        cur = len(st)
        st.append(State(st[last].len + 1))
        st[cur].cnt = 1 # Original state
        
        p = last
        while p != -1 and c not in st[p].next:
            st[p].next[c] = cur
            p = st[p].link
            
        if p == -1:
            st[cur].link = 0
        else:
            q = st[p].next[c]
            if st[p].len + 1 == st[q].len:
                st[cur].link = q
            else:
                clone = len(st)
                st.append(State(st[p].len + 1, st[q].link))
                st[clone].next = st[q].next.copy()
                st[clone].cnt = 0 # Clone
                
                while p != -1 and st[p].next.get(c) == q:
                    st[p].next[c] = clone
                    p = st[p].link
                st[q].link = st[cur].link = clone
        last = cur

    # Build SAM
    for char in s:
        extend(char)
        
    # Propagate counts
    # Sort by length descending
    nodes = sorted(range(1, len(st)), key=lambda i: st[i].len, reverse=True)
    for u in nodes:
        if st[u].link != -1:
            st[st[u].link].cnt += st[u].cnt
            
    # Answer queries
    ans = []
    for query in queries:
        curr = 0
        ok = True
        for char in query:
            if char not in st[curr].next:
                ok = False
                break
            curr = st[curr].next[char]
        if ok:
            ans.append(st[curr].cnt)
        else:
            ans.append(0)
            
    return ans

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    q = int(input_data[1])
    queries = input_data[2:2 + q]
    
    ans = count_occurrences(s, queries)
    sys.stdout.write("\n".join(str(x) for x in ans) + "\n")

if __name__ == "__main__":
    main()