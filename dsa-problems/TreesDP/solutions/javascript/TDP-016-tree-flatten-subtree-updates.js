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

  let timer = 0;
  const inTime = Array(n + 1).fill(0);
  const outTime = Array(n + 1).fill(0);

  function dfs(u, p) {
    inTime[u] = ++timer;
    for (const v of adj[u]) {
      if (v !== p) dfs(v, u);
    }
    outTime[u] = timer;
  }

  dfs(1, 0);

  const fenwick = Array(n + 2).fill(0);

  function update(i, val) {
    while (i <= n) {
      fenwick[i] += val;
      i += i & -i;
    }
  }

  function query(i) {
    let sum = 0;
    while (i > 0) {
      sum += fenwick[i];
      i -= i & -i;
    }
    return sum;
  }

  for (let i = 1; i <= n; i++) {
    update(inTime[i], values[i]);
    update(inTime[i] + 1, -values[i]);
  }

  const q = parseInt(lines[idx++]);
  for (let i = 0; i < q; i++) {
    const parts = lines[idx++].split(" ").map(Number);
    if (parts[0] === 1) {
      const [_, u, val] = parts;
      update(inTime[u], val);
      update(outTime[u] + 1, -val);
    } else {
      const [_, u] = parts;
      console.log(query(inTime[u]));
    }
  }
});
