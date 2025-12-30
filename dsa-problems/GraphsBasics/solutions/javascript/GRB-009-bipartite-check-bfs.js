const readline = require("readline");

class Solution {
  bipartiteColors(n, adj) {
    const colors = new Int32Array(n).fill(-1);

    for (let i = 0; i < n; i++) {
      if (colors[i] === -1) {
        const queue = [i];
        colors[i] = 0;
        let head = 0;
        
        while (head < queue.length) {
          const u = queue[head++];
          
          for (const v of adj[u]) {
            if (colors[v] === -1) {
              colors[v] = 1 - colors[u];
              queue.push(v);
            } else if (colors[v] === colors[u]) {
              return null;
            }
          }
        }
      }
    }
    return colors;
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
  const colors = solution.bipartiteColors(n, adj);
  
  if (colors === null) {
    console.log("false");
  } else {
    console.log("true");
    console.log(colors.join(" "));
  }
});
