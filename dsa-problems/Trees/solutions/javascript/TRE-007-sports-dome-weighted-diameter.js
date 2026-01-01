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
if (n === 0) {
  console.log("0");
  process.exit(0);
}

const left = new Array(n).fill(-1);
const right = new Array(n).fill(-1);
const lw = new Array(n).fill(1);
const rw = new Array(n).fill(1);

for (let i = 0; i < n && i + 1 < lines.length; i++) {
  const parts = lines[i + 1].split(/\s+/).map(Number);
  if (parts.length < 3) continue;
  left[i] = parts[1];
  right[i] = parts[2];
  if (parts.length >= 5) {
    lw[i] = parts[3];
    rw[i] = parts[4];
  }
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

const stack = [root];
const order = [];
const visited = new Array(n).fill(false);
visited[root] = true;

while (stack.length > 0) {
  const u = stack.pop();
  order.push(u);
  const l = left[u];
  const r = right[u];
  if (l !== -1 && !visited[l]) {
    visited[l] = true;
    stack.push(l);
  }
  if (r !== -1 && !visited[r]) {
    visited[r] = true;
    stack.push(r);
  }
}

const dist = new Array(n).fill(0);
let maxDiameter = 0;
for (let i = order.length - 1; i >= 0; i--) {
  const u = order[i];
  let lPath = 0;
  let rPath = 0;
  if (left[u] !== -1) lPath = lw[u] + dist[left[u]];
  if (right[u] !== -1) rPath = rw[u] + dist[right[u]];
  const dia = lPath + rPath;
  if (dia > maxDiameter) maxDiameter = dia;
  dist[u] = lPath > rPath ? lPath : rPath;
}

console.log(maxDiameter.toString());
