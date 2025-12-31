const readline = require("readline");

class Solution {
  offlineLca(n, edges, ops) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
      adj[v].push(u);
    }

    const LOG = 20;
    const up = Array.from({ length: n }, () => new Int32Array(LOG).fill(-1));
    const depth = new Int32Array(n);

    const dfsLCA = (u, p, d) => {
      depth[u] = d;
      up[u][0] = p;
      for (let i = 1; i < LOG; i++) {
        if (up[u][i - 1] !== -1) up[u][i] = up[up[u][i - 1]][i - 1];
        else up[u][i] = -1;
      }
      for (const v of adj[u]) {
        if (v !== p) dfsLCA(v, u, d + 1);
      }
    };

    dfsLCA(0, -1, 0);

    const getLCA = (u, v) => {
      if (depth[u] < depth[v]) { const t = u; u = v; v = t; }
      for (let i = LOG - 1; i >= 0; i--) {
        if (depth[u] - (1 << i) >= depth[v]) u = up[u][i];
      }
      if (u === v) return u;
      for (let i = LOG - 1; i >= 0; i--) {
        if (up[u][i] !== up[v][i]) {
          u = up[u][i];
          v = up[v][i];
        }
      }
      return up[u][0];
    };

    const edgeStart = new Map();
    for (const [u, v] of edges) {
      const k = u < v ? ``u,`{v}` : ``v,`{u}`;
      edgeStart.set(k, 0);
    }

    const q = ops.length;
    const intervals = [];
    const queries = new Int32Array(q).fill(-1); // Store index if query
    const queryArgs = [];

    for (let i = 0; i < q; i++) {
      const [t, u, v] = ops[i];
      const k = u < v ? ``u,`{v}` : ``v,`{u}`;

      if (t === "cut") {
        if (edgeStart.has(k)) {
          const start = edgeStart.get(k);
          edgeStart.delete(k);
          intervals.push([start, i - 1, u, v]);
        }
      } else if (t === "link") {
        edgeStart.set(k, i + 1);
      } else {
        queries[i] = queryArgs.length;
        queryArgs.push([u, v]);
      }
    }

    for (const [k, start] of edgeStart) {
      const [u, v] = k.split(",").map(Number);
      intervals.push([start, q, u, v]);
    }

    const seg = Array.from({ length: 4 * (q + 1) }, () => []);

    const addRange = (node, start, end, l, r, u, v) => {
      if (r < start || end < l) return;
      if (l <= start && end <= r) {
        seg[node].push([u, v]);
        return;
      }
      const mid = Math.floor((start + end) / 2);
      addRange(node * 2, start, mid, l, r, u, v);
      addRange(node * 2 + 1, mid + 1, end, l, r, u, v);
    };

    for (const [l, r, u, v] of intervals) {
      if (l <= r) addRange(1, 0, q, l, r, u, v);
    }

    // DSU
    const parent = new Int32Array(n);
    const size = new Int32Array(n).fill(1);
    for (let i = 0; i < n; i++) parent[i] = i;
    const history = [];

    const find = (i) => {
      while (i !== parent[i]) i = parent[i];
      return i;
    };

    const union = (i, j) => {
      let root_i = find(i);
      let root_j = find(j);
      if (root_i !== root_j) {
        if (size[root_i] < size[root_j]) { const t = root_i; root_i = root_j; root_j = t; }
        parent[root_j] = root_i;
        size[root_i] += size[root_j];
        history.push([root_j, root_i]);
        return true;
      }
      return false;
    };

    const rollback = () => {
      const [child, par] = history.pop();
      parent[child] = child;
      size[par] -= size[child];
    };

    const results = [];

    const solve = (node, start, end) => {
      let opsCount = 0;
      for (const [u, v] of seg[node]) {
        if (union(u, v)) opsCount++;
      }

      if (start === end) {
        if (queries[start] !== -1) {
          const [u, v] = queryArgs[queries[start]];
          if (find(u) === find(v)) {
            results.push(getLCA(u, v));
          } else {
            results.push(-1);
          }
        }
      } else {
        const mid = Math.floor((start + end) / 2);
        solve(node * 2, start, mid);
        solve(node * 2 + 1, mid + 1, end);
      }

      while (opsCount-- > 0) rollback();
    };

    solve(1, 0, q);
    return results;
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
  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }
  const q = parseInt(data[idx++], 10);
  const ops = [];
  for (let i = 0; i < q; i++) {
    const t = data[idx++];
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    ops.push([t, u, v]);
  }

  const solution = new Solution();
  const out = solution.offlineLca(n, edges, ops);
  console.log(out.join("\n"));
});
