const readline = require("readline");

class Solution {
  validateBSTGap(n, values, left, right, G) {
    if (n === 0) return true;
    
    const minInit = -BigInt("9223372036854775808"); // Min 64-bit signed
    const maxInit = BigInt("9223372036854775807");  // Max 64-bit signed
    
    const validate = (u, minVal, maxVal) => {
      if (u === -1) return true;
      
      const val = BigInt(values[u]);
      if (val <= minVal || val >= maxVal) return false;
      
      const gVal = BigInt(G);
      
      if (left[u] !== -1) {
        const lVal = BigInt(values[left[u]]);
        let diff = val - lVal;
        if (diff < 0n) diff = -diff;
        if (diff < gVal) return false;
        if (!validate(left[u], minVal, val)) return false;
      }
      
      if (right[u] !== -1) {
        const rVal = BigInt(values[right[u]]);
        let diff = val - rVal;
        if (diff < 0n) diff = -diff;
        if (diff < gVal) return false;
        if (!validate(right[u], val, maxVal)) return false;
      }
      
      return true;
    };
    
    return validate(0, minInit, maxInit);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const values = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const G = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  console.log(solution.validateBSTGap(n, values, left, right, G) ? "true" : "false");
});
