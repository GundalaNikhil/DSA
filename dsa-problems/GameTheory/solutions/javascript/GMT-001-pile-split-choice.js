const readline = require("readline");

class Solution {
  pileSplitGame(n) {
    if (n === 0) return "Second";
    const g = new Int32Array(n + 1);
    
    for (let i = 3; i <= n; i++) {
      const reachable = new Set();
      for (let j = 1; 2 * j < i; j++) {
        reachable.add(g[j] ^ g[i - j]);
      }
      
      let missing = 0;
      while (reachable.has(missing)) {
        missing++;
      }
      g[i] = missing;
    }
    
    return g[n] > 0 ? "First" : "Second";
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
  const n = parseInt(data[0]);
  const solution = new Solution();
  console.log(solution.pileSplitGame(n));
});
