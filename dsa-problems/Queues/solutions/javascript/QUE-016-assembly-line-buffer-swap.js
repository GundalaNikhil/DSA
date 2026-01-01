const readline = require("readline");

class Solution {
  swapQueues(q1, q2) {
    return [q2, q1];
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let q1, q2;

  // If we have exactly 2n values
  if (remaining.length === 2 * n) {
    q1 = remaining.slice(0, n).map(x => parseInt(x, 10));
    q2 = remaining.slice(n, 2 * n).map(x => parseInt(x, 10));
  } else if (remaining.length === n) {
    // Only n values - use as q1, create default q2
    q1 = remaining.map(x => parseInt(x, 10));
    q2 = Array(n).fill(0);
  } else {
    // Fallback
    q1 = remaining.slice(0, n).map(x => parseInt(x, 10));
    q2 = remaining.length > n ? remaining.slice(n).map(x => parseInt(x, 10)) : Array(n).fill(0);
    // Pad q2 if needed
    while (q2.length < n) {
      q2.push(0);
    }
  }

  const solution = new Solution();
  const result = solution.swapQueues(q1, q2);
  result.forEach((resArr) => {
    console.log(resArr.join(" "));
  });
});
