const readline = require("readline");

class Solution {
  chocolateCut(R, C) {
    const area = R * C;
    return (area % 2n === 0n) ? "First" : "Second";
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
  const R = BigInt(flatData[idx++]);
  const C = BigInt(flatData[idx++]);

  const solution = new Solution();
  console.log(solution.chocolateCut(R, C));
});
