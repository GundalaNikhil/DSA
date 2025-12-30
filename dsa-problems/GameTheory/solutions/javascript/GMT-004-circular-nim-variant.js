const readline = require("readline");

class Solution {
  constructor() {
    this.memo = new Map();
    this.visiting = new Set();
  }

  circularNim(n, piles) {
    return this.solve(n, piles, 0);
  }

  solve(n, piles, depth) {
    if (depth > 50) return "Draw";
    const key = piles.join(",");
    if (this.memo.has(key)) return this.memo.get(key);
    if (this.visiting.has(key)) return "Draw";

    this.visiting.add(key);
    let canReachLoss = false;
    let canReachDraw = false;
    let hasMoves = false;

    for (let i = 0; i < n; i++) {
      if (piles[i] > 0) {
        for (let k = 1; k <= piles[i]; k++) {
          hasMoves = true;
          piles[i] -= k;
          piles[(i - 1 + n) % n]++;
          piles[(i + 1) % n]++;

          const res = this.solve(n, piles, depth + 1);

          piles[(i + 1) % n]--;
          piles[(i - 1 + n) % n]--;
          piles[i] += k;

          if (res === "Second") {
            canReachLoss = true;
            break;
          }
          if (res === "Draw") {
            canReachDraw = true;
          }
        }
        if (canReachLoss) break;
      }
    }

    this.visiting.delete(key);
    let result;
    if (canReachLoss) result = "First";
    else if (!hasMoves) result = "Second";
    else if (canReachDraw) result = "Draw";
    else result = "Second";

    this.memo.set(key, result);
    return result;
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
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  
  const piles = [];
  for (let i = 0; i < n; i++) {
      piles.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.circularNim(n, piles));
});
