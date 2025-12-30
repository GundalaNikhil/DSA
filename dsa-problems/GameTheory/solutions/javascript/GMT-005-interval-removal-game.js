const readline = require("readline");

class Solution {
  intervalRemovalGame(n, intervals) {
    let xorSum = 0n; // Use BigInt for safety with large numbers
    for (const [l, r] of intervals) {
      const len = BigInt(r) - BigInt(l);
      xorSum ^= len;
    }
    return xorSum > 0n ? "First" : "Second";
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  
  const intervals = [];
  for (let i = 0; i < n; i++) {
      const l = parseInt(flatData[idx++]);
      const r = parseInt(flatData[idx++]);
      intervals.push([l, r]);
  }

  const solution = new Solution();
  console.log(solution.intervalRemovalGame(n, intervals));
});
