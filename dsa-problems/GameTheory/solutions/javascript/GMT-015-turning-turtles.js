const readline = require("readline");

class Solution {
  turningTurtles(n, k, s) {
    let xorSum = 0;
    const mod = k + 1;
    for (let i = 0; i < s.length; i++) {
      if (s[i] === 'H') {
        xorSum ^= ((i % mod) + 1);
      }
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
  const k = parseInt(flatData[idx++]);
  const s = flatData[idx++];

  const solution = new Solution();
  console.log(solution.turningTurtles(n, k, s));
});
