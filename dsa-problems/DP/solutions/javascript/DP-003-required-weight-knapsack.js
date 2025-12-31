const readline = require("readline");
const NEG = -(10 ** 30);

class Solution {
  maxValueWithRequiredWeight(n, W, R, w, v) {
    const dp = new Array(W + 1).fill(NEG);
    dp[0] = 0;

    for (let i = 0; i < n; i++) {
      const wi = w[i];
      const vi = v[i];
      for (let wt = W; wt >= wi; wt--) {
        if (dp[wt - wi] !== NEG) {
          dp[wt] = Math.max(dp[wt], dp[wt - wi] + vi);
        }
      }
    }

    let ans = NEG;
    for (let wt = R; wt <= W; wt++) ans = Math.max(ans, dp[wt]);
    return ans === NEG ? -1 : ans;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [nStr, WStr, RStr] = lines[idx++].split(" ");
  const n = Number(nStr), W = Number(WStr), R = Number(RStr);
  const w = new Array(n);
  const v = new Array(n);
  for (let i = 0; i < n; i++) {
    const [wi, vi] = lines[idx++].split(" ").map(Number);
    w[i] = wi; v[i] = vi;
  }
  const sol = new Solution();
  console.log(sol.maxValueWithRequiredWeight(n, W, R, w, v));
});
