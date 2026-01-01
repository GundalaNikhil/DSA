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
const blocked = new Array(n).fill(0);
const left = new Array(n).fill(-1);
const right = new Array(n).fill(-1);

for (let i = 0; i < n && i + 1 < lines.length; i++) {
  const parts = lines[i + 1].split(/\s+/).map(Number);
  if (parts.length < 3) continue;
  values[i] = parts[0];
  if (parts.length >= 4) {
    blocked[i] = parts[1];
    left[i] = parts[2];
    right[i] = parts[3];
  } else {
    blocked[i] = 0;
    left[i] = parts[1];
    right[i] = parts[2];
  }
}

if (lines.length <= n + 1) {
  process.exit(0);
}
const uv = lines[n + 1].split(/\s+/).map(Number);
if (uv.length < 2) {
  process.exit(0);
}
const u = uv[0];
const v = uv[1];

const parent = new Array(n).fill(-1);
for (let i = 0; i < n; i++) {
  if (left[i] !== -1) parent[left[i]] = i;
  if (right[i] !== -1) parent[right[i]] = i;
}

const ancestors = new Set();
let curr = u;
let steps = 0;
while (curr !== -1 && steps < n + 5) {
  ancestors.add(curr);
  curr = parent[curr];
  steps++;
}

let lca = -1;
curr = v;
steps = 0;
while (curr !== -1 && steps < n + 5) {
  if (ancestors.has(curr)) {
    lca = curr;
    break;
  }
  curr = parent[curr];
  steps++;
}

if (lca === -1) {
  console.log("-1");
  process.exit(0);
}

steps = 0;
while (lca !== -1 && blocked[lca] === 1 && steps < n + 5) {
  lca = parent[lca];
  steps++;
}

if (lca === -1) {
  console.log("-1");
} else {
  console.log(values[lca].toString());
}
