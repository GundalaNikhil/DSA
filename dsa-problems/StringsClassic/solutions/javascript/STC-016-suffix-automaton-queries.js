const readline = require("readline");

class State {
  constructor(len = 0, link = -1) {
    this.len = len;
    this.link = link;
    this.next = new Map();
    this.cnt = 0n;
  }
}

class Solution {
  countOccurrences(s, queries) {
    const st = [new State()];
    let last = 0;
    
    const extend = (c) => {
      const cur = st.length;
      st.push(new State(st[last].len + 1));
      st[cur].cnt = 1n;
      
      let p = last;
      while (p !== -1 && !st[p].next.has(c)) {
        st[p].next.set(c, cur);
        p = st[p].link;
      }
      
      if (p === -1) {
        st[cur].link = 0;
      } else {
        const q = st[p].next.get(c);
        if (st[p].len + 1 === st[q].len) {
          st[cur].link = q;
        } else {
          const clone = st.length;
          const cloneState = new State(st[p].len + 1, st[q].link);
          cloneState.next = new Map(st[q].next);
          cloneState.cnt = 0n;
          st.push(cloneState);
          
          while (p !== -1 && st[p].next.get(c) === q) {
            st[p].next.set(c, clone);
            p = st[p].link;
          }
          st[q].link = st[cur].link = clone;
        }
      }
      last = cur;
    };
    
    for (const char of s) {
      extend(char);
    }
    
    // Propagate
    const nodes = Array.from({length: st.length}, (_, i) => i);
    nodes.sort((a, b) => st[b].len - st[a].len);
    
    for (const u of nodes) {
      if (u === 0) continue;
      if (st[u].link !== -1) {
        st[st[u].link].cnt += st[u].cnt;
      }
    }
    
    const ans = [];
    for (const q of queries) {
      let curr = 0;
      let ok = true;
      for (const char of q) {
        if (!st[curr].next.has(char)) {
          ok = false;
          break;
        }
        curr = st[curr].next.get(char);
      }
      if (ok) ans.push(st[curr].cnt.toString());
      else ans.push("0");
    }
    
    return ans;
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
  const q = parseInt(data[1], 10);
  const queries = data.slice(2, 2 + q);
  const solution = new Solution();
  const ans = solution.countOccurrences(s, queries);
  console.log(ans.join("\n"));
});
