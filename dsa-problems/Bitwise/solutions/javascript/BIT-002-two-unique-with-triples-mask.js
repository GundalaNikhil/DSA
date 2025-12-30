const readline = require("readline");

class Solution {
  twoUniqueWithTriplesMask(a, M) {
    let splitBit = -1;

    // Step 1: Find valid split bit within Mask
    for (let i = 0; i < 31; i++) {
      if (((M >> i) & 1) === 0) continue;

      let count = 0;
      for (const x of a) {
        if ((x >> i) & 1) count++;
      }

      if (count % 3 === 1) {
        splitBit = i;
        break;
      }
    }

    let num1 = 0;
    let num2 = 0;

    // Step 2: Reconstruct using standard Single Number II logic per group
    for (let i = 0; i < 31; i++) {
      let c1 = 0;
      let c2 = 0;
      for (const x of a) {
        const bitVal = (x >> i) & 1;
        const group = (x >> splitBit) & 1;
        if (group === 1) {
          c2 += bitVal;
        } else {
          c1 += bitVal;
        }
      }
      if (c1 % 3 === 1) num1 |= 1 << i;
      if (c2 % 3 === 1) num2 |= 1 << i;
    }

    const result = [num1, num2];
    result.sort((x, y) => x - y);
    return result;
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
  const M = Number(tokens[ptr++]);

  const solution = new Solution();
  const result = solution.twoUniqueWithTriplesMask(a, M);
  console.log(result.join(" "));
});
