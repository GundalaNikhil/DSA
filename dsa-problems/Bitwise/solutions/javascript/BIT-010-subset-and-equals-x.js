const readline = require("readline");

class Solution {
  subsetAndEqualsX(a, X) {
    const candidates = [];
    for (const v of a) {
      if ((v & X) === X) {
        candidates.push(v);
      }
    }
    
    const n = candidates.length;
    let count = 0;
    const limit = 1 << n;
    
    for (let mask = 1; mask < limit; mask++) {
      let currentAnd = -1;
      let first = true;
      
      for (let i = 0; i < n; i++) {
        if ((mask >>> i) & 1) {
          if (first) {
            currentAnd = candidates[i];
            first = false;
          } else {
            currentAnd &= candidates[i];
          }
        }
      }
      
      if (!first && currentAnd === X) {
        count++;
      }
    }
    
    return count;
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
    
    const X = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(String(solution.subsetAndEqualsX(a, X)));
});
