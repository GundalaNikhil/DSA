const readline = require("readline");

class Solution {
  mergeWithPriority(A, B) {
    const n = A.length;
    const m = B.length;
    const result = [];

    let i = 0,
      j = 0;

    while (i < n && j < m) {
      if (A[i] <= B[j]) {
        result.push(A[i++]);
      } else {
        result.push(B[j++]);
      }
    }

    while (i < n) result.push(A[i++]);
    while (j < m) result.push(B[j++]);

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
  const A = [];
  for (let i = 0; i < n; i++) A.push(Number(tokens[ptr++]));

  const m = Number(tokens[ptr++]);
  const B = [];
  for (let i = 0; i < m; i++) B.push(Number(tokens[ptr++]));

  const solution = new Solution();
  const result = solution.mergeWithPriority(A, B);
  console.log(result.join(" "));
});
