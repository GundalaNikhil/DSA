const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  solve();
});

function solve() {
  let idx = 0;
  const n = parseInt(lines[idx++]);

  const weight = [0];
  const weights = lines[idx++].split(" ").map(Number);
  weight.push(...weights);

  const totalWeight = weight.reduce((a, b) => a + b, 0);

  const graph = Array.from({ length: n + 1 }, () => []);

  for (let i = 0; i < n - 1; i++) {
    const [u, v] = lines[idx++].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  const subtreeWeight = new Array(n + 1).fill(0);
  const down = new Array(n + 1).fill(0);
  const up = new Array(n + 1).fill(0);

  function dfsDown(u, parent) {
    subtreeWeight[u] = weight[u];
    down[u] = 0;

    for (const v of graph[u]) {
      if (v === parent) continue;

      dfsDown(v, u);

      const childContribution =
        down[v] + 2 * subtreeWeight[v] + subtreeWeight[v];
      down[u] += childContribution;
      subtreeWeight[u] += subtreeWeight[v];
    }
  }

  function dfsUp(u, parent) {
    if (parent !== -1) {
      const outsideWeight = totalWeight - subtreeWeight[u];

      const parentTotalDown = down[parent];
      const uContribution = down[u] + 2 * subtreeWeight[u] + subtreeWeight[u];
      const parentDownWithoutU = parentTotalDown - uContribution;

      up[u] =
        up[parent] + parentDownWithoutU + 2 * outsideWeight + outsideWeight;
    }

    for (const v of graph[u]) {
      if (v === parent) continue;
      dfsUp(v, u);
    }
  }

  dfsDown(1, -1);
  dfsUp(1, -1);

  let minCost = Infinity;
  let bestNode = 1;

  for (let i = 1; i <= n; i++) {
    const totalCost = down[i] + up[i];
    if (totalCost < minCost) {
      minCost = totalCost;
      bestNode = i;
    }
  }

  console.log(bestNode);
}
