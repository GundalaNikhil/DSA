const readline = require("readline");

class Solution {
  countSetBitsIndexedXor(a) {
    let total = 0n;
    for (let i = 0; i < a.length; i++) {
      let val = i ^ a[i];
      // Manual popcount for JS numbers (32-bit safe for bitwise ops)
      // val = val - ((val >>> 1) & 0x55555555);
      // val = (val & 0x33333333) + ((val >>> 2) & 0x33333333);
      // val = (val + (val >>> 4)) & 0x0f0f0f0f;
      // val = val + (val >>> 8);
      // val = val + (val >>> 16);
      // total += BigInt(val & 0x3f);
      
      // Or cleaner loop since max 30 bits
      let c = 0;
      while (val > 0) {
        val &= (val - 1);
        c++;
      }
      total += BigInt(c);
    }
    return total.toString(); // BigInt generally safer for large sums
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
    console.log(solution.countSetBitsIndexedXor(a));
});
