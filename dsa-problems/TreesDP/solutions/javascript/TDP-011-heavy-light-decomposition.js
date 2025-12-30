const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, terminal: false });

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const n = parseInt(lines[idx++]);
  const values = [0, ...lines[idx++].split(" ").map(Number)];

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  const parent = Array(n + 1).fill(0);
  const depth = Array(n + 1).fill(0);
  const heavy = Array(n + 1).fill(-1);
  const head = Array(n + 1).fill(0);
  const pos = Array(n + 1).fill(0);
  let timer = 0;

  function dfs1(u, p) {
    let size = 1,
      maxSize = 0;
    parent[u] = p;
    depth[u] = p === 0 ? 0 : depth[p] + 1;

    for (const v of adj[u]) {
      if (v === p) continue;
      const subtreeSize = dfs1(v, u);
      size += subtreeSize;
      if (subtreeSize > maxSize) {
        maxSize = subtreeSize;
        heavy[u] = v;
      }
    }
    return size;
  }

  function dfs2(u, h) {
    head[u] = h;
    pos[u] = timer++;

    if (heavy[u] !== -1) dfs2(heavy[u], h);

    for (const v of adj[u]) {
      if (v !== parent[u] && v !== heavy[u]) {
        dfs2(v, v);
      }
    }
  }

  dfs1(1, 0);
  dfs2(1, 1);

  const posToVal = Array(n).fill(0);
  for (let i = 1; i <= n; i++) {
    posToVal[pos[i]] = values[i];
  }

  const seg = Array(4 * n).fill(0);

  function build(node, l, r) {
    if (l === r) {
      seg[node] = posToVal[l];
      return;
    }
    const mid = Math.floor((l + r) / 2);
    build(2 * node, l, mid);
    build(2 * node + 1, mid + 1, r);
    seg[node] = seg[2 * node] + seg[2 * node + 1];
  }

  function query(node, l, r, ql, qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return seg[node];
    const mid = Math.floor((l + r) / 2);
    return (
      query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)
    );
  }

  build(1, 0, n - 1);

  function queryPath(u, v) {
    let result = 0;
    while (head[u] !== head[v]) {
      if (depth[head[u]] < depth[head[v]]) [u, v] = [v, u];
      result += query(1, 0, n - 1, pos[head[u]], pos[u]);
      u = parent[head[u]];
    }
    if (depth[u] > depth[v]) [u, v] = [v, u];
    result += query(1, 0, n - 1, pos[u], pos[v]);
    return result;
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    console.log(queryPath(u, v));
  }
});
