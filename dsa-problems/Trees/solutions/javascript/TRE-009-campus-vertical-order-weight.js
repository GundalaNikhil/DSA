const fs = require("fs");

const lines = fs
  .readFileSync(0, "utf8")
  .split(/\r?\n/)
  .map((line) => line.trim())
  .filter((line) => line.length > 0);

if (lines.length === 0) {
  process.exit(0);
}

const n = parseInt(lines[0], 10);
const values = new Array(n).fill(0);
const weights = new Array(n).fill(1);
const left = new Array(n).fill(-1);
const right = new Array(n).fill(-1);

for (let i = 0; i < n && i + 1 < lines.length; i++) {
  const parts = lines[i + 1].split(/\s+/).map(Number);
  if (parts.length < 3) continue;
  values[i] = parts[0];
  if (parts.length >= 4) {
    weights[i] = parts[1];
    left[i] = parts[2];
    right[i] = parts[3];
  } else {
    weights[i] = 1;
    left[i] = parts[1];
    right[i] = parts[2];
  }
}

let W = 0;
if (lines.length > n + 1) {
  W = parseInt(lines[n + 1], 10);
}

if (n === 0) {
  console.log("");
  process.exit(0);
}

const hasParent = new Array(n).fill(false);
for (let i = 0; i < n; i++) {
  if (left[i] !== -1) hasParent[left[i]] = true;
  if (right[i] !== -1) hasParent[right[i]] = true;
}
let root = 0;
for (let i = 0; i < n; i++) {
  if (!hasParent[i]) {
    root = i;
    break;
  }
}

const cols = new Map();
const queue = [[root, 0, 0]];
let head = 0;
const visited = new Array(n).fill(false);
visited[root] = true;
let minCol = 0;
let maxCol = 0;

while (head < queue.length) {
  const [u, c, d] = queue[head++];
  if (!cols.has(c)) cols.set(c, []);
  cols.get(c).push({ val: values[u], weight: weights[u], depth: d });
  if (c < minCol) minCol = c;
  if (c > maxCol) maxCol = c;

  if (left[u] !== -1 && !visited[left[u]]) {
    visited[left[u]] = true;
    queue.push([left[u], c - 1, d + 1]);
  }
  if (right[u] !== -1 && !visited[right[u]]) {
    visited[right[u]] = true;
    queue.push([right[u], c + 1, d + 1]);
  }
}

const result = [];
for (let c = minCol; c <= maxCol; c++) {
  if (!cols.has(c)) continue;
  const list = cols.get(c);
  let totalWeight = 0;
  for (const node of list) totalWeight += node.weight;
  if (totalWeight >= W) {
    list.sort((a, b) => {
      if (a.depth !== b.depth) return a.depth - b.depth;
      if (a.weight !== b.weight) return b.weight - a.weight;
      return a.val - b.val;
    });
    result.push(list.map((node) => node.val));
  }
}

if (result.length === 0) {
  console.log("");
} else {
  console.log(result.map((col) => col.join(" ")).join("\n"));
}
