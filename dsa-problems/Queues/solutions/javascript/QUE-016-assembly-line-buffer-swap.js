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
  const q1 = [];
  for (let i = 0; i < n; i++) q1.push(parseInt(data[idx++], 10));
  const q2 = [];
  for (let i = 0; i < n; i++) q2.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const result = solution.swapQueues(q1, q2);
  result.forEach((resArr) => {
    console.log(resArr.join(" "));
  });
});
