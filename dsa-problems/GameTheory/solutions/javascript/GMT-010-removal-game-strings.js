const readline = require("readline");

class Solution {
  getGrundy(k) {
    if (k === 0) return 0;
    if (k === 1) return 1;
    if (k === 2) return 0;
    const rem = k % 3;
    if (rem === 0) return 2;
    if (rem === 1) return 1;
    return 0;
  }

  stringGame(n, strings) {
    let xorSum = 0;
    for (const s of strings) {
      if (s.length === 0) continue;
      let groups = 1;
      for (let i = 1; i < s.length; i++) {
        if (s[i] !== s[i - 1]) {
          groups++;
        }
      }
      xorSum ^= this.getGrundy(groups);
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
  
  const strings = [];
  for (let i = 0; i < n; i++) {
      strings.push(flatData[idx++]);
  }

  const solution = new Solution();
  console.log(solution.stringGame(n, strings));
});
