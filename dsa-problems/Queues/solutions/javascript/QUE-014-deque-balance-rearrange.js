const readline = require("readline");

class Solution {
  buildDeque(values) {
    const result = [];
    let left = 0;
    let right = values.length - 1;
    
    while (left <= right) {
      result.push(values[left]);
      if (left !== right) {
        result.push(values[right]);
      }
      left++;
      right--;
    }
    
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
  const values = [];
  for (let i = 0; i < n; i++) {
    values.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.buildDeque(values);
  console.log(result.join(" "));
});
