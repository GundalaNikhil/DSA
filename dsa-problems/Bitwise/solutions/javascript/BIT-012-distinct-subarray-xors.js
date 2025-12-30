const readline = require("readline");

class Solution {
  distinctSubarrayXors(a) {
    const n = a.length;
    // Use TypedArray to save memory (Int32Array)
    const size = (n * (n + 1)) / 2;
    const results = new Int32Array(size);
    
    let idx = 0;
    for (let i = 0; i < n; i++) {
      let val = 0;
      for (let j = i; j < n; j++) {
        val ^= a[j];
        results[idx++] = val;
      }
    }
    
    results.sort();
    
    if (size === 0) return 0;
    let count = 1;
    for (let i = 1; i < size; i++) {
      if (results[i] !== results[i - 1]) {
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
    
    const solution = new Solution();
    console.log(String(solution.distinctSubarrayXors(a)));
});
