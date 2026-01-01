class Solution {
  countVisible(h) {
    const n = h.length;
    const stack = [];
    let count = 0;

    // Scan from right to left
    for (let i = n - 1; i >= 0; i--) {
      // Remove buildings shorter than current
      while (stack.length > 0 && h[stack[stack.length - 1]] < h[i]) {
        stack.pop();
      }

      // If stack empty, current building can see sunset (nothing taller to right)
      if (stack.length === 0) {
        count++;
      }

      stack.push(i);
    }
    return count;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});

rl.on("close", () => {
  const tokens = data.trim().split(/\s+/);
  if (tokens.length === 0) return;
  
  let idx = 0;
  const n = parseInt(tokens[idx++], 10);
  const h = [];
  for (let i = 0; i < n; i++) {
    h.push(parseInt(tokens[idx++], 10));
  }
  
  const solution = new Solution();
  console.log(solution.countVisible(h));
});
