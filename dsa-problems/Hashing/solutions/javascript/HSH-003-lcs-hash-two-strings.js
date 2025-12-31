const readline = require("readline");

class Solution {
  longestCommonSubstring(a, b) {
    const MOD = 1000000007n;
    const BASE = 31n;

    const check = (len) => {
      if (len === 0) return true;

      const hashesA = new Set();
      let currentHash = 0n;
      let power = 1n;

      // Compute BASE^(len-1)
      for (let i = 0; i < len - 1; i++) {
        power = (power * BASE) % MOD;
      }

      // Hash A
      for (let i = 0; i < len; i++) {
        const code = BigInt(a.charCodeAt(i));
        currentHash = (currentHash * BASE + code) % MOD;
      }
      hashesA.add(currentHash);

      for (let i = len; i < a.length; i++) {
        const removeCode = BigInt(a.charCodeAt(i - len));
        const addCode = BigInt(a.charCodeAt(i));

        let remove = (removeCode * power) % MOD;
        currentHash = (currentHash - remove + MOD) % MOD;
        currentHash = (currentHash * BASE + addCode) % MOD;
        hashesA.add(currentHash);
      }

      // Check B
      currentHash = 0n;
      for (let i = 0; i < len; i++) {
        const code = BigInt(b.charCodeAt(i));
        currentHash = (currentHash * BASE + code) % MOD;
      }
      if (hashesA.has(currentHash)) return true;

      for (let i = len; i < b.length; i++) {
        const removeCode = BigInt(b.charCodeAt(i - len));
        const addCode = BigInt(b.charCodeAt(i));

        let remove = (removeCode * power) % MOD;
        currentHash = (currentHash - remove + MOD) % MOD;
        currentHash = (currentHash * BASE + addCode) % MOD;
        if (hashesA.has(currentHash)) return true;
      }

      return false;
    };

    let low = 0,
      high = Math.min(a.length, b.length);
    let ans = 0;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      if (mid === 0) {
        low = mid + 1;
        continue;
      }
      if (check(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return ans;
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
  const a = data[0];
  const b = data[1];

  const solution = new Solution();
  console.log(solution.longestCommonSubstring(a, b));
});
