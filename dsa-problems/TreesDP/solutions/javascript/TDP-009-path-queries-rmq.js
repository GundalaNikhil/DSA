const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const n = parseInt(lines[idx++]);

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v, w] = lines[idx++].split(" ").map(Number);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const first = Array(n + 1).fill(0);
  const depth = Array(n + 1).fill(0);
  const euler = [];

  function dfs(u, p, d) {
    depth[u] = d;
    first[u] = euler.length;
    euler.push(u);

    for (const [v, w] of adj[u]) {
      if (v !== p) {
        dfs(v, u, d + w);
        euler.push(u);
      }
    }
  }

  dfs(1, 0, 0);

  // Build sparse table
  const size = euler.length;
  const logSize = Math.floor(Math.log2(size)) + 1;
  const st = Array.from({ length: size }, () => Array(logSize).fill(0));

  for (let i = 0; i < size; i++) {
    st[i][0] = i;
  }

  for (let j = 1; j < logSize; j++) {
    for (let i = 0; i + (1 << j) <= size; i++) {
      const left = st[i][j - 1];
      const right = st[i + (1 << (j - 1))][j - 1];
      st[i][j] = depth[euler[left]] <= depth[euler[right]] ? left : right;
    }
  }

  function queryLCA(u, v) {
    let l = first[u],
      r = first[v];
    if (l > r) [l, r] = [r, l];

    const len = r - l + 1;
    const k = Math.floor(Math.log2(len));

    const left = st[l][k];
    const right = st[r - (1 << k) + 1][k];

    const lcaIdx = depth[euler[left]] <= depth[euler[right]] ? left : right;
    return euler[lcaIdx];
  }

  function queryDistance(u, v) {
    const lca = queryLCA(u, v);
    return depth[u] + depth[v] - 2 * depth[lca];
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    console.log(queryDistance(u, v));
  }
});
