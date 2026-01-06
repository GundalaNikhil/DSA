# Maximum Common Substring using Suffix Automaton

import sys

class SAMNode:
    def __init__(self, length=0, link=-1):
        self.len = length
        self.link = link
        self.next = {}

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
                self.nodes.append(SAMNode(self.nodes[p].len + 1, self.nodes[q].link))
                self.nodes[clone].next = self.nodes[q].next.copy()
                
                while p != -1 and self.nodes[p].next.get(char) == q:
                    self.nodes[p].next[char] = clone
                    p = self.nodes[p].link
                    
                self.nodes[q].link = self.nodes[curr].link = clone
                
        self.last = curr

def solve():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        print("")
        return
        
    s1 = input_data[0]
    s2 = input_data[1]
    
    if not s1 or not s2:
        print("")
        return
        
    sam = SAM(s1)
    
    best_len = 0
    best_end_pos = -1 # End position in s2
    
    curr = 0
    length = 0
    
    for i, char in enumerate(s2):
        while curr != 0 and char not in sam.nodes[curr].next:
            curr = sam.nodes[curr].link
            length = sam.nodes[curr].len
            
        if char in sam.nodes[curr].next:
            curr = sam.nodes[curr].next[char]
            length += 1
        else:
            # Should have fallen back to root (curr=0) by while loop logic, and if root fails, length=0
            # If char not in root's next, curr remains 0, length remains 0.
            pass
            
        if length > best_len:
            best_len = length
            best_end_pos = i
            
    if best_len == 0:
        print("")
    else:
        # result is substring of s2 ending at best_end_pos with length best_len
        start_pos = best_end_pos - best_len + 1
        print(s2[start_pos : best_end_pos + 1])

if __name__ == "__main__":
    solve()