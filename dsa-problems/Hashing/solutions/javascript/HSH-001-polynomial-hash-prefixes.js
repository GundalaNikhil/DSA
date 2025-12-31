const readline = require("readline");

class Solution {
  computePrefixHashes(s, B, M) {
    const hashes = [];
    // Use BigInt because intermediate values (hash * B) can exceed 2^53 - 1
    // M is up to 10^9, B up to 10^9. Product is 10^18.
    // JS Number is safe up to 9*10^15. 10^18 requires BigInt.
    let currentHash = 0n;
    const bigB = BigInt(B);
    const bigM = BigInt(M);

    for (let i = 0; i < s.length; i++) {
      const charCode = BigInt(s.charCodeAt(i));
      currentHash = (currentHash * bigB + charCode) % bigM;
      hashes.push(Number(currentHash)); // Convert back to Number for output
    }

    return hashes;
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

  let ptr = 0;
  const s = data[ptr++];
  const [B, M] = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  const result = solution.computePrefixHashes(s, B, M);
  console.log(result.join(" "));
});
