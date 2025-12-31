const readline = require("readline");

class Solution {
  exactCountSubsetSum(arr, target, k) {
    if (k === 0) return target === 0;
    let bits = new Array(k + 1).fill(0n);
    bits[0] = 1n;
    const mask = (1n << BigInt(target + 1)) - 1n;

    for (const x of arr) {
      const shift = BigInt(x);
      for (let cnt = k; cnt >= 1; cnt--) {
        bits[cnt] = (bits[cnt] | (bits[cnt - 1] << shift)) & mask;
      }
    }

    return ((bits[k] >> BigInt(target)) & 1n) === 1n;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  const [n, target, k] = lines[0].split(" ").map(Number);
  const arr = lines[1].split(" ").map(Number);
  const sol = new Solution();
  console.log(sol.exactCountSubsetSum(arr, target, k) ? "true" : "false");
});
