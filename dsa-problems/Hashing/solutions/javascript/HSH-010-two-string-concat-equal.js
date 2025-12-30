const readline = require("readline");

class Solution {
  checkConcatenationEqual(a, b, c, d) {
    if (a.length + b.length !== c.length + d.length) {
      return false;
    }

    const MOD = 1000000007n;
    const BASE = 313n;

    const computeHash = (s) => {
      let h = 0n;
      for (let i = 0; i < s.length; i++) {
        const code = BigInt(s.charCodeAt(i));
        h = (h * BASE + code) % MOD;
      }
      return h;
    };

    const power = (base, exp) => {
      let res = 1n;
      let b = base;
      let e = BigInt(exp);
      while (e > 0n) {
        if (e % 2n === 1n) res = (res * b) % MOD;
        b = (b * b) % MOD;
        e /= 2n;
      }
      return res;
    };

    const hA = computeHash(a);
    const hB = computeHash(b);
    const hC = computeHash(c);
    const hD = computeHash(d);

    const combinedAB = (hA * power(BASE, b.length) + hB) % MOD;
    const combinedCD = (hC * power(BASE, d.length) + hD) % MOD;

    return combinedAB === combinedCD;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length < 4) return;
  const [a, b, c, d] = data;

  const solution = new Solution();
  console.log(solution.checkConcatenationEqual(a, b, c, d) ? "true" : "false");
});
