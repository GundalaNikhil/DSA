const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, terminal: false });

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const n = parseInt(lines[idx++]);
  const LOG = 20;
  const color = [0, ...lines[idx++].split(" ").map(Number)];

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const up = Array.from({ length: n + 1 }, () => Array(LOG).fill(0));

  function dfs(u, p) {
    up[u][0] = p;
    for (let i = 1; i < LOG; i++) {
      up[u][i] = up[up[u][i - 1]][i - 1];
    }
    for (const v of adj[u]) {
      if (v !== p) dfs(v, u);
    }
  }

  dfs(1, 0);

  function findKth(v, c, k) {
    let count = 0;
    while (v !== 0) {
      if (color[v] === c) {
        count++;
        if (count === k) return v;
      }
      v = up[v][0];
    }
    return -1;
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [v, c, k] = lines[idx++].split(" ").map(Number);
    console.log(findKth(v, c, k));
  }
});
