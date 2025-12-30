const readline = require("readline");

class Solution {
  interleaveQueue(values) {
    const n = values.length;
    const mid = Math.floor(n / 2);
    const result = [];
    
    for (let i = 0; i < mid; i++) {
      result.push(values[i]);
      result.push(values[mid + i]);
    }
    return result;
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
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.interleaveQueue(values);
  console.log(result.join(" "));
});
