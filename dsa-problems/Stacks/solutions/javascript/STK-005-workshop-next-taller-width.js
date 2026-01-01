class Solution {
  nextTallerWithin(h, w) {
    const n = h.length;
    const result = new Array(n).fill(-1);
    const stack = []; // Indices

    for (let i = n - 1; i >= 0; i--) {
      while (stack.length > 0 && h[stack[stack.length - 1]] <= h[i]) {
        stack.pop();
      }

      if (stack.length > 0) {
        const j = stack[stack.length - 1];
        if (j - i <= w) {
          result[i] = h[j];
        }
      }

      stack.push(i);
    }
    return result;
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
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const h = [];
  for (let i = 0; i < n; i++) {
    h.push(parseInt(data[idx++], 10));
  }
  const w = parseInt(data[idx++], 10);
  
  const solution = new Solution();
  const res = solution.nextTallerWithin(h, w);
  console.log(res.join("\n"));
});
