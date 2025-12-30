const readline = require("readline");

class Solution {
  smallestAbsentXor(a) {
    const basis = new Int32Array(32);
    
    for (let x of a) {
      for (let i = 30; i >= 0; i--) {
        if ((x >>> i) & 1) { // checking bit i
          if (basis[i] === 0) {
            basis[i] = x;
            break;
          }
          x ^= basis[i];
        }
      }
    }
    
    for (let i = 0; i <= 30; i++) {
      if (basis[i] === 0) {
        return (1n << BigInt(i)).toString();
      }
    }
    return (1n << 31n).toString();
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
    
    const solution = new Solution();
    console.log(solution.smallestAbsentXor(a));
});
