const readline = require("readline");

class Solution {
  maximizeOrWithKPicks(a, k) {
    const n = a.length;
    
    if (k >= 30) {
      let total = 0n;
      for (const x of a) total |= BigInt(x);
      return total.toString();
    }
    
    let currentOr = 0n;
    const used = new Uint8Array(n);
    
    for (let step = 0; step < k; step++) {
      let bestOr = -1n;
      let bestIdx = -1;
      
      for (let i = 0; i < n; i++) {
        if (used[i] === 0) {
          const val = BigInt(a[i]);
          const newOr = currentOr | val;
          if (newOr > bestOr) {
            bestOr = newOr;
            bestIdx = i;
          }
        }
      }
      
      if (bestIdx !== -1) {
        currentOr = bestOr;
        used[bestIdx] = 1;
      }
    }
    
    return currentOr.toString();
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
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const a = [];
    for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
    const k = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.maximizeOrWithKPicks(a, k));
});
