const readline = require("readline");

class Solution {
  mergeQueues(a, b) {
    const n = a.length;
    const m = b.length;
    const result = [];
    let i = 0;
    let j = 0;
    
    while (i < n && j < m) {
      if (a[i] <= b[j]) {
        result.push(a[i++]);
      } else {
        result.push(b[j++]);
      }
    }
    
    while (i < n) result.push(a[i++]);
    while (j < m) result.push(b[j++]);
    
    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const a = [];
  for (let i = 0; i < n; i++) {
    a.push(parseInt(data[idx++], 10));
  }
  const m = parseInt(data[idx++], 10);
  const b = [];
  for (let i = 0; i < m; i++) {
    b.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.mergeQueues(a, b);
  console.log(result.join(" "));
});
