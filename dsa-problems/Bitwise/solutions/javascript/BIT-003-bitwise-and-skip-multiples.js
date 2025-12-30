const readline = require("readline");

class Solution {
  bitwiseAndSkipMultiples(L, R, m) {
    // BigInt operations required
    const diff = R - L;
    
    if (diff <= 2000000n) {
      let ans = -1n;
      let found = false;
      for (let i = L; i <= R; i++) {
        if (i % m !== 0n) {
          if (!found) ans = i;
          else ans &= i;
          found = true;
        }
      }
      return found ? ans : -1n;
    }
    
    let lTemp = L;
    let rTemp = R;
    let shift = 0n;
    
    while (lTemp !== rTemp) {
      lTemp >>= 1n;
      rTemp >>= 1n;
      shift++;
    }
    
    let standardAnd = lTemp << shift;
    
    if (m === 2n) {
      standardAnd |= 1n;
    }
    
    return standardAnd;
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
    
    const L = BigInt(tokens[0]);
    const R = BigInt(tokens[1]);
    const m = BigInt(tokens[2]);
    
    const solution = new Solution();
    console.log(solution.bitwiseAndSkipMultiples(L, R, m).toString());
});
