const readline = require("readline");

class Solution {
  divisorGame(n) {
    const memo = new Int8Array(n + 1); // 0: unknown, 1: Win, 2: Loss

    const canWin = (curr) => {
      if (memo[curr] !== 0) return memo[curr] === 1;

      let canReachLosing = false;
      for (let i = 2; i * i <= curr; i++) {
        if (curr % i === 0) {
          const d1 = i;
          if (!canWin(d1)) {
            canReachLosing = true;
            break;
          }
          const d2 = curr / i;
          if (d2 < curr) {
            if (!canWin(d2)) {
              canReachLosing = true;
              break;
            }
          }
        }
      }

      memo[curr] = canReachLosing ? 1 : 2;
      return canReachLosing;
    };

    return canWin(n) ? "First" : "Second";
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
  const n = parseInt(data[0]);
  const solution = new Solution();
  console.log(solution.divisorGame(n));
});
