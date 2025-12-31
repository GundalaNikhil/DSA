const readline = require("readline");

class Solution {
  takeOrSplit(n, heaps) {
    let xorSum = 0n;
    for (const x of heaps) {
      xorSum ^= BigInt(x - 1);
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
  
  const heaps = [];
  for (let i = 0; i < n; i++) {
      heaps.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.takeOrSplit(n, heaps));
});
