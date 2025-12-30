const readline = require("readline");

class Solution {
  weightedBalancePoint(a, L, R) {
    let totalSum = 0n;
    for (const x of a) {
      totalSum += BigInt(x);
    }

    let leftSum = 0n;
    const bigL = BigInt(L);
    const bigR = BigInt(R);

    for (let i = 0; i < a.length; i++) {
      const val = BigInt(a[i]);
      const rightSum = totalSum - leftSum - val;

      if (leftSum * bigL === rightSum * bigR) {
        return i;
      }

      leftSum += val;
    }

    return -1;
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

  const L = Number(tokens[ptr++]);
  const R = Number(tokens[ptr++]);

  const solution = new Solution();
  console.log(solution.weightedBalancePoint(a, L, R));
});
