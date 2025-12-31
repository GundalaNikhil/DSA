const readline = require("readline");

class Solution {
  mirrorCheck(n, values, colors, left, right) {
    if (n === 0) return true;
    
    // Helper for symmetry
    const isMirror = (u, v) => {
      if (u === -1 && v === -1) return true;
      if (u === -1 || v === -1) return false;
      if (values[u] !== values[v]) return false;
      return isMirror(left[u], right[v]) && isMirror(right[u], left[v]);
    };
    
    if (left[0] === -1 && right[0] === -1) return true;
    if (!isMirror(left[0], right[0])) return false;
    
    // Helper for color balance
    const qL = [left[0]];
    const qR = [right[0]];
    
    while (qL.length > 0 && qR.length > 0) {
      if (qL.length !== qR.length) return false;
      
      const size = qL.length;
      let sumL = 0;
      for (let i = 0; i < size; i++) {
        const u = qL.shift();
        sumL += colors[u];
        if (left[u] !== -1) qL.push(left[u]);
        if (right[u] !== -1) qL.push(right[u]);
      }
      
      let sumR = 0;
      for (let i = 0; i < size; i++) {
        const v = qR.shift();
        sumR += colors[v];
        if (left[v] !== -1) qR.push(left[v]);
        if (right[v] !== -1) qR.push(right[v]);
      }
      
      if (sumL !== sumR) return false;
    }
    
    return qL.length === 0 && qR.length === 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const values = new Array(n);
  const colors = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    colors[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.mirrorCheck(n, values, colors, left, right) ? "true" : "false");
});
