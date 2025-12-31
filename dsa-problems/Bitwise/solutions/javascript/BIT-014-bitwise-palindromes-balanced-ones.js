const readline = require("readline");

class Solution {
  makePalindrome(half, len) {
    let res = half;
    let temp = half;
    if (len % 2 === 1) temp >>= 1n;

    let lower = 0n;
    const halfLen = BigInt(Math.floor(len / 2));
    for (let i = 0; i < halfLen; i++) {
      lower = (lower << 1n) | (temp & 1n);
      temp >>= 1n;
    }
    return (res << halfLen) | lower;
  }

  countForLen(N, len, isLimit) {
    const halfLen = Math.floor((len + 1) / 2);
    const minHalf = 1n << BigInt(halfLen - 1);
    let maxHalf = (1n << BigInt(halfLen)) - 1n;

    if (isLimit) {
      const prefix = N >> BigInt(len - halfLen);
      if (prefix < minHalf) return 0n;
      if (prefix < maxHalf) maxHalf = prefix;
    }

    let limitVal = maxHalf;
    let validBelow = 0n;

    if (limitVal > minHalf) {
      if (len % 2 === 0) {
        validBelow = limitVal - minHalf;
      } else {
        // Count evens
        validBelow = (limitVal - minHalf + 1n) / 2n;
      }
    }

    let checkBoundary = true;
    if (len % 2 === 1 && limitVal % 2n !== 0n) checkBoundary = false;

    if (checkBoundary) {
      const p = this.makePalindrome(limitVal, len);
      if (!isLimit || p <= N) {
        validBelow++;
      }
    }

    return validBelow;
  }

  solve(N) {
    if (N < 0n) return 0n;
    if (N === 0n) return 1n;

    let L = 0;
    let temp = N;
    while (temp > 0n) {
      L++;
      temp >>= 1n;
    }

    let total = 1n;

    for (let len = 1; len < L; len++) {
      // Pass a very large number for infinite limit
      total += this.countForLen(1n << 62n, len, false);
    }
    total += this.countForLen(N, L, true);
    return total;
  }

  countBitwisePalindromesBalancedOnes(L, R) {
    return this.solve(R) - this.solve(L - 1n);
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

  const L = BigInt(tokens[0]);
  const R = BigInt(tokens[1]);

  const solution = new Solution();
  console.log(solution.countBitwisePalindromesBalancedOnes(L, R).toString());
});
