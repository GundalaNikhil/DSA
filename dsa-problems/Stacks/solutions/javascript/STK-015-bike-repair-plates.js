class Solution {
  countUnsafe(d) {
    let count = 0;
    for (let i = 0; i < d.length - 1; i++) {
        if (d[i+1] > d[i]) {
            count++;
        }
    }
    return count;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});

rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const d = [];
  for (let i = 0; i < n; i++) {
    d.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  console.log(solution.countUnsafe(d));
});
