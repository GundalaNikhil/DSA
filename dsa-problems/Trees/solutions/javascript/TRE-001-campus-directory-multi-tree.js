const readline = require("readline");

class Solution {
  traverseAll(n, nodes) {
    if (n === 0) return [[], [], []];
    
    const pre = [];
    const inOrder = [];
    const post = [];
    
    const dfs = (u) => {
      if (u === -1) return;
      const [val, left, right] = nodes[u];
      
      pre.push(val);
      dfs(left);
      inOrder.push(val);
      dfs(right);
      post.push(val);
    };
    
    dfs(0);
    return [pre, inOrder, post];
  }

  structuralIdentical(n1, t1, n2, t2) {
    if (n1 === 0 && n2 === 0) return true;
    if (n1 === 0 || n2 === 0) return false;
    
    const check = (u1, u2) => {
      if (u1 === -1 && u2 === -1) return true;
      if (u1 === -1 || u2 === -1) return false;
      
      const l1 = t1[u1][1] !== -1;
      const l2 = t2[u2][1] !== -1;
      if (l1 !== l2) return false;
      
      const r1 = t1[u1][2] !== -1;
      const r2 = t2[u2][2] !== -1;
      if (r1 !== r2) return false;
      
      return check(t1[u1][1], t2[u2][1]) && check(t1[u1][2], t2[u2][2]);
    };
    
    return check(0, 0);
  }

  matchingTraversals(t1, t2) {
    const matches = [];
    
    const eq = (a, b) => {
      if (a.length !== b.length) return false;
      for (let i = 0; i < a.length; i++) {
        if (a[i] !== b[i]) return false;
      }
      return true;
    };
    
    if (eq(t1[0], t2[0])) matches.push("preorder");
    if (eq(t1[1], t2[1])) matches.push("inorder");
    if (eq(t1[2], t2[2])) matches.push("postorder");
    
    return matches;
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
  let idx = 0;
  
  let n1 = 0, t1 = [];
  if (idx < data.length) {
      n1 = parseInt(data[idx++], 10);
      for (let i = 0; i < n1; i++) {
        const v = parseInt(data[idx++], 10);
        const l = parseInt(data[idx++], 10);
        const r = parseInt(data[idx++], 10);
        t1.push([v, l, r]);
      }
  }

  let n2 = 0, t2 = [];
  if (idx < data.length) {
      n2 = parseInt(data[idx++], 10);
      for (let i = 0; i < n2; i++) {
        const v = parseInt(data[idx++], 10);
        const l = parseInt(data[idx++], 10);
        const r = parseInt(data[idx++], 10);
        t2.push([v, l, r]);
      }
  }

  const solution = new Solution();
  const trav1 = solution.traverseAll(n1, t1);
  const trav2 = solution.traverseAll(n2, t2);
  const same = solution.structuralIdentical(n1, t1, n2, t2);
  const matches = solution.matchingTraversals(trav1, trav2);

  const out = [];
  for (let i = 0; i < 3; i++) out.push(trav1[i].join(" "));
  for (let i = 0; i < 3; i++) out.push(trav2[i].join(" "));
  out.push(same ? "true" : "false");
  out.push(matches.length === 0 ? "NONE" : matches.join(" "));
  console.log(out.join("\n"));
});
