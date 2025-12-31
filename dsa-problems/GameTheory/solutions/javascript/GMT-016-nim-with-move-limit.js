const readline = require("readline");

class Solution {
  nimLimit(n, A, L) {
    let xorSum = 0;
    for (let i = 0; i < n; i++) {
      xorSum ^= (A[i] % (L[i] + 1));
    }
    return xorSum > 0 ? "First" : "Second";
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
  
  const A = [];
  for (let i = 0; i < n; i++) {
      A.push(parseInt(flatData[idx++]));
  }
  const L = [];
  for (let i = 0; i < n; i++) {
      L.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.nimLimit(n, A, L));
});
