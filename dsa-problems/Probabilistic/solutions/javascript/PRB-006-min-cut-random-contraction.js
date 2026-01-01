const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n + 1 }, (_, i) => i);
    this.components = n;
  }
  find(i) {
    if (this.parent[i] === i) return i;
    return (this.parent[i] = this.find(this.parent[i]));
  }
  unite(i, j) {
    const rootI = this.find(i);
    const rootJ = this.find(j);
    if (rootI !== rootJ) {
      this.parent[rootI] = rootJ;
      this.components--;
    }
  }
}

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

function kargerMinCut(n, edges) {
  const dsu = new DSU(n);
  const currentEdges = [...edges];
  shuffle(currentEdges);

  for (const edge of currentEdges) {
    if (dsu.components <= 2) break;
    dsu.unite(edge[0], edge[1]);
  }

  let cutSize = 0;
  for (const edge of edges) {
    if (dsu.find(edge[0]) !== dsu.find(edge[1])) {
      cutSize++;
    }
  }
  return cutSize;
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  let trials;
  if (n <= 20) trials = 100;
  else trials = Math.floor(n * n * 0.5);

  let minCut = m + 1;
  for (let i = 0; i < trials; i++) {
    const cut = kargerMinCut(n, edges);
    if (cut < minCut) minCut = cut;
  }
  console.log(minCut);
});
