class Solution {
  countVisible(h) {
    const n = h.length;
    const stack = [];
    let count = 0;

    for (let i = n - 1; i >= 0; i--) {
      while (stack.length > 0 && h[stack[stack.length - 1]] < h[i]) {
        stack.pop();
      }
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

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  if (lines.length < 2) return;
  
  // Line 0 is N, ignore
  // Line 1 is the array
  const parts = lines[1].trim().split(/\s+/).filter(x => x !== "");
  const h = parts.map(x => BigInt(x));
  
  const solution = new Solution();
  console.log(solution.countVisible(h));
});
