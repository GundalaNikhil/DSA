const readline = require("readline");

class Solution {
  toggleRangesMinFlips(A, B) {
    let count = 0;
    let prevDiff = 0;
    
    for (let i = 0; i < A.length; i++) {
      const currDiff = A[i] ^ B[i];
      if (currDiff === 1 && prevDiff === 0) {
        count++;
      }
      prevDiff = currDiff;
    }
    return count;
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
    const B = [];
    for (let i = 0; i < n; i++) B.push(Number(tokens[ptr++]));
    
    const solution = new Solution();
    console.log(solution.toggleRangesMinFlips(A, B));
});
