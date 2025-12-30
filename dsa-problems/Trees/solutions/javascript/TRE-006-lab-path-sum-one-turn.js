const readline = require("readline");

class Solution {
  constructor() {
    this.found = false;
  }

  hasOneTurnPath(n, values, left, right, target) {
    if (n === 0) return false;
    this.found = false;
    this.dfs(0, 0n, new Set(), values, left, right, BigInt(target), true);
    return this.found;
  }

  dfs(u, currentLeftSum, prefixes, values, left, right, target, isStart) {
    if (u === -1 || this.found) return;

    const val = BigInt(values[u]);
    const nextSum = currentLeftSum + val;

    if (!isStart) {
      this.checkRightChain(right[u], nextSum, prefixes, values, right, target);
    }
    if (this.found) return;

    prefixes.add(currentLeftSum);
    this.dfs(left[u], nextSum, prefixes, values, left, right, target, false);
    prefixes.delete(currentLeftSum);

    if (this.found) return;

    this.dfs(right[u], 0n, new Set(), values, left, right, target, true);
  }

  checkRightChain(u, turnLeftSum, prefixes, values, right, target) {
    let currentRightSum = 0n;
    let curr = u;
    while (curr !== -1 && !this.found) {
      currentRightSum += BigInt(values[curr]);
      const needed = turnLeftSum + currentRightSum - target;
      if (prefixes.has(needed)) {
        this.found = true;
        return;
      }
      curr = right[curr];
    }
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
  const values = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const target = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  console.log(solution.hasOneTurnPath(n, values, left, right, target) ? "true" : "false");
});
