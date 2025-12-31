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

  const lis = Array(n + 1).fill(0);
  const active = [];

  function binarySearch(arr, val) {
    let l = 0,
      r = arr.length;
    while (l < r) {
      const mid = Math.floor((l + r) / 2);
      if (arr[mid] < val) l = mid + 1;
      else r = mid;
    }
    return l;
  }

  function dfs(u, p) {
    const pos = binarySearch(active, values[u]);
    const saved = pos < active.length ? active[pos] : null;

    if (pos < active.length) {
      active[pos] = values[u];
    } else {
      active.push(values[u]);
    }

    lis[u] = active.length;

    for (const v of adj[u]) {
      if (v !== p) dfs(v, u);
    }

    if (saved !== null) {
      active[pos] = saved;
    } else {
      active.pop();
    }
  }

  dfs(1, 0);
  console.log(lis.slice(1).join(" "));
});
