const readline = require("readline");

class Solution {
  boundaryWithGaps(n, values, left, right) {
    const result = [];
    if (n === 0) return result;

    if (values[0] >= 0) result.push(values[0]);
    if (left[0] === -1 && right[0] === -1) return result;

    // Left Boundary
    let curr = left[0];
    while (curr !== -1) {
      if (left[curr] === -1 && right[curr] === -1) break;
      if (values[curr] >= 0) result.push(values[curr]);
      if (left[curr] !== -1) curr = left[curr];
      else curr = right[curr];
    }

    // Leaves
    const addLeaves = (u) => {
      if (u === -1) return;
      if (left[u] === -1 && right[u] === -1) {
        if (values[u] >= 0) result.push(values[u]);
        return;
      }
      addLeaves(left[u]);
      addLeaves(right[u]);
    };
    addLeaves(0);

    // Right Boundary
    const rightBound = [];
    curr = right[0];
    while (curr !== -1) {
      if (left[curr] === -1 && right[curr] === -1) break;
      if (values[curr] >= 0) rightBound.push(values[curr]);
      if (right[curr] !== -1) curr = right[curr];
      else curr = left[curr];
    }
    rightBound.reverse();
    result.push(...rightBound);

    return result;
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

  const solution = new Solution();
  const ans = solution.boundaryWithGaps(n, values, left, right);
  console.log(ans.join(" "));
});
