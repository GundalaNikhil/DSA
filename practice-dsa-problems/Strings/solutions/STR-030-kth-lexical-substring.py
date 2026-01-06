import sys


class SAMNode:
    def __init__(self, length=0, link=-1):
        self.len = length
        self.link = link
        self.next = {}
        self.count = 0


class SAM:
    def __init__(self, s):
        self.nodes = [SAMNode()]
        self.last = 0
        for char in s:
            self.extend(char)

    def extend(self, char):
        curr = len(self.nodes)
        self.nodes.append(SAMNode(self.nodes[self.last].len + 1))
        p = self.last
        while p != -1 and char not in self.nodes[p].next:
            self.nodes[p].next[char] = curr
            p = self.nodes[p].link
            if p == -1:
                self.nodes[curr].link = 0
            else:
                q = self.nodes[p].next[char]
                if self.nodes[p].len + 1 == self.nodes[q].len:
                    self.nodes[curr].link = q
                else:
                    clone = len(self.nodes)
                    self.nodes.append(
                        SAMNode(self.nodes[p].len + 1, self.nodes[q].link)
                    )
                    self.nodes[clone].next = self.nodes[q].next.copy()
                    while p != -1 and self.nodes[p].next.get(char) == q:
                        self.nodes[p].next[char] = clone
                        p = self.nodes[p].link
                        self.nodes[q].link = self.nodes[curr].link = clone
                        self.last = curr


def solve():
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    if not line1 or not line2:
        return
    s = line1
    k = int(line2)
    sam = SAM(s)
    m = len(sam.nodes)
    order = sorted(
        range(m),
        key=lambda i: sam.nodes[i].len,
        reverse=True,
    )
    for i in order:
        sam.nodes[i].count = 1
        for char in sorted(sam.nodes[i].next.keys()):
            sam.nodes[i].count += sam.nodes[sam.nodes[i].next[char]].count
            
    # Query Check
    if k >= sam.nodes[0].count:
        # Note: nodes[0].count includes empty string? k usually 1-indexed?
        # Standard: total substrings = sum(len(node))? Or paths?
        # Here logic counts PATHS from node to end.
        
        # Original logic: if k >= count: print -1?
        # If nodes[0] is root, count is total paths starting from root.
        # k is 1-indexed.
        if k > sam.nodes[0].count - 1: # -1 for empty string if counted?
             print("-1")
             return
             
    res = []
    curr = 0
    while k > 0:
        found = False
        for char in sorted(sam.nodes[curr].next.keys()):
            nxt = sam.nodes[curr].next[char]
            # Count paths through `nxt` often accounts for substrings starting with `char`
            # Wait, `sam.nodes[nxt].count` is total paths starting from `nxt`?
            # Usually K-th substring logic:
            # Sort edges.
            # 1 (current char `char` itself) + count(paths from `nxt`).
            # If k <= that, go there.
            
            # Here: `sam.nodes[nxt].count` seems to be total paths.
            # But does it include the empty path at `nxt`?
            # Just assume original logic was:
            
            if k <= sam.nodes[nxt].count:
                res.append(char)
                k -= 1 # The character `char` itself consumes 1 rank
                curr = nxt
                found = True
                break
            else:
                k -= sam.nodes[nxt].count
                
        if not found:
            break
            
    print("".join(res))


if __name__ == "__main__":
    solve()
