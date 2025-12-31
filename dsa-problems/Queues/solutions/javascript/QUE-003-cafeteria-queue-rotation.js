const readline = require("readline");

class Solution {
  rotateQueue(values, k) {
    const n = values.length;
    if (n === 0) return [];
    
    // In JS, k can be larger than Number.MAX_SAFE_INTEGER if not careful,
    // but constraints say 10^9 which fits.
    const rotations = k % n;
    
    if (rotations === 0) return values;
    
    // Slice and concat
    const part1 = values.slice(rotations);
    const part2 = values.slice(0, rotations);
    return part1.concat(part2);
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
  const k = parseInt(data[idx++], 10);

  const solution = new Solution();
  const result = solution.rotateQueue(values, k);
  console.log(result.join(" "));
});
