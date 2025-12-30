const readline = require("readline");

class Solution {
  longestZeroSumEvenLength(arr) {
    // Map sum -> [evenIdx, oddIdx]
    const map = new Map();
    // Use null for not seen
    map.set(0n, [null, -1]); // Sum 0 at index -1 (odd)

    let currentSum = 0n;
    let maxLen = 0;

    for (let i = 0; i < arr.length; i++) {
      currentSum += BigInt(arr[i]);
      const parity = i & 1;

      if (!map.has(currentSum)) {
        map.set(currentSum, [null, null]);
      }

      const indices = map.get(currentSum);
      const prevIdx = indices[parity];

      if (prevIdx !== null) {
        const length = i - prevIdx;
        if (length > maxLen) {
          maxLen = length;
        }
      } else {
        indices[parity] = i;
      }
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
  if (data.length === 0) return;
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(Number(tokens[ptr++]));

  const solution = new Solution();
  console.log(solution.longestZeroSumEvenLength(arr));
});
