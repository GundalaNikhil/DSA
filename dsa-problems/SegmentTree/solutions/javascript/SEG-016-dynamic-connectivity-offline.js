class Solution {
  process(n, events) {
    const m = events.length;
    const tree = Array.from({ length: 4 * m }, () => []);
    const queries = new Array(m).fill(null);
    const activeEdges = new Map();

    const addEdge = (node, start, end, l, r, edge) => {
      if (l > end || r < start) return;
      if (l <= start && end <= r) {
        tree[node].push(edge);
        return;
      }
      const mid = Math.floor((start + end) / 2);
      addEdge(2 * node + 1, start, mid, l, r, edge);
      addEdge(2 * node + 2, mid + 1, end, l, r, edge);
    };

    for (let i = 0; i < m; i++) {
      const type = events[i][0];
      let u = parseInt(events[i][1], 10);
      let v = parseInt(events[i][2], 10);
      if (u > v) [u, v] = [v, u];
      const key = `${u},${v}`;

      if (type === "ADD") {
        activeEdges.set(key, i);
      } else if (type === "REMOVE") {
        if (activeEdges.has(key)) {
          const start = activeEdges.get(key);
          activeEdges.delete(key);
          addEdge(0, 0, m - 1, start, i - 1, { u, v });
        }
      } else {
        queries[i] = { u, v };
      }
    }

    for (const [key, start] of activeEdges.entries()) {
      const [u, v] = key.split(",").map(Number);
      addEdge(0, 0, m - 1, start, m - 1, { u, v });
    }

    // DSU
    const parent = new Int32Array(n + 1);
    const rank = new Int32Array(n + 1);
    for (let i = 1; i <= n; i++) {
      parent[i] = i;
      rank[i] = 1;
    }
    const history = [];

    const find = (i) => {
      if (parent[i] === i) return i;
      return find(parent[i]);
    };

    const union = (i, j) => {
      let rootI = find(i);
      let rootJ = find(j);
      if (rootI !== rootJ) {
        if (rank[rootI] < rank[rootJ]) {
          const temp = rootI;
          rootI = rootJ;
          rootJ = temp;
        }
        parent[rootJ] = rootI;
        rank[rootI] += rank[rootJ];
        history.push({ child: rootJ, parent: rootI });
      } else {
        history.push({ child: -1, parent: -1 });
      }
    };

    const rollback = () => {
      const op = history.pop();
      if (op.child !== -1) {
        parent[op.child] = op.child;
        rank[op.parent] -= rank[op.child];
      }
    };

    const connected = (i, j) => find(i) === find(j);

    const results = [];

    const dfs = (node, start, end) => {
      for (const e of tree[node]) {
        union(e.u, e.v);
      }

      if (start === end) {
        if (queries[start]) {
          results.push(connected(queries[start].u, queries[start].v) ? "true" : "false");
        }
      } else {
        const mid = Math.floor((start + end) / 2);
        dfs(2 * node + 1, start, mid);
        dfs(2 * node + 2, mid + 1, end);
      }

      for (let i = 0; i < tree[node].length; i++) {
        rollback();
      }
    };

    dfs(0, 0, m - 1);
    return results;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const events = [];
  for (let i = 0; i < m; i++) {
    const type = data[idx++];
    const u = data[idx++];
    const v = data[idx++];
    events.push([type, u, v]);
  }
  const solution = new Solution();
  const out = solution.process(n, events);
  console.log(out.join("\n"));
});
