const readline = require("readline");

class Solution {
  longestPalindromicPrefix(s, c) {
    const T = s + c;
    const n = T.length;

    const MOD = 1000000007n;
    const BASE = 313n;

    let fwdHash = 0n;
    let revHash = 0n;
    let power = 1n;

    let maxLen = 0;

    for (let i = 0; i < n; i++) {
      const val = BigInt(T.charCodeAt(i));

      fwdHash = (fwdHash * BASE + val) % MOD;
      revHash = (revHash + val * power) % MOD;

      if (fwdHash === revHash) {
        maxLen = i + 1;
      }

      power = (power * BASE) % MOD;
    }

    return maxLen;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length < 2) return;
  const s = data[0];
  const c = data[1][0];

  const solution = new Solution();
  console.log(solution.longestPalindromicPrefix(s, c));
});
