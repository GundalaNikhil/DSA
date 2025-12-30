const readline = require("readline");

class Node {
  constructor(len, link) {
    this.len = len;
    this.link = link;
    this.next = new Map();
  }
}

class Solution {
  countDistinctPalindromes(s) {
    const tree = [];
    tree.push(new Node(-1, 0)); // Node 0: odd root
    tree.push(new Node(0, 0));  // Node 1: even root
    
    let last = 1;
    const n = s.length;
    
    for (let i = 0; i < n; i++) {
      const c = s[i];
      let curr = last;
      
      while (true) {
        const len = tree[curr].len;
        if (i - 1 - len >= 0 && s[i - 1 - len] === c) {
          break;
        }
        curr = tree[curr].link;
      }
      
      if (tree[curr].next.has(c)) {
        last = tree[curr].next.get(c);
        continue;
      }
      
      const newNodeIdx = tree.length;
      tree.push(new Node(tree[curr].len + 2, 0));
      tree[curr].next.set(c, newNodeIdx);
      
      if (tree[newNodeIdx].len === 1) {
        tree[newNodeIdx].link = 1;
      } else {
        let temp = tree[curr].link;
        while (true) {
          const len = tree[temp].len;
          if (i - 1 - len >= 0 && s[i - 1 - len] === c) {
            break;
          }
          temp = tree[temp].link;
        }
        tree[newNodeIdx].link = tree[temp].next.get(c);
      }
      
      last = newNodeIdx;
    }
    
    return tree.length - 2;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  console.log(solution.countDistinctPalindromes(s).toString());
});
