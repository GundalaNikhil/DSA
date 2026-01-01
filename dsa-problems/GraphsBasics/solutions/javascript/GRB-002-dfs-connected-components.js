const readline = require("readline");

class Solution {
  components(n, adj) {
    const comp = new Int32Array(n).fill(0);
    let count = 0;
    const stack = [];

    for (let i = 0; i < n; i++) {
      if (comp[i] !== 0) continue;
      count++;
      stack.length = 0;
      stack.push(i);
      comp[i] = count;
      while (stack.length > 0) {
        const u = stack.pop();
        for (const v of adj[u]) {
          if (comp[v] === 0) {
            comp[v] = count;
            stack.push(v);
          }
        }
      }
    }
    return comp;
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
  const m = parseInt(data[idx++], 10);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
    adj[v].push(u);
  }

  const solution = new Solution();
  const comp = solution.components(n, adj);
  let maxComp = 0;
  for (let i = 0; i < n; i++) {
    if (comp[i] > maxComp) maxComp = comp[i];
  }
  console.log(maxComp.toString());
});
