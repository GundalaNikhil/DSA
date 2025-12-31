const readline = require("readline");

class Solution {
  zeroSlideWithLimit(arr, m) {
    const n = arr.length;
    let writeIdx = 0;

    for (let readIdx = 0; readIdx < n; readIdx++) {
      if (arr[readIdx] !== 0) {
        if (readIdx !== writeIdx) {
          if (m <= 0) break;

          // Swap
          const temp = arr[writeIdx];
          arr[writeIdx] = arr[readIdx];
          arr[readIdx] = temp;

          m--;
        }
        writeIdx++;
      }
    }
    return arr;
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

  const m = Number(tokens[ptr++]);

  const solution = new Solution();
  const result = solution.zeroSlideWithLimit(arr, m);
  console.log(result.join(" "));
});
