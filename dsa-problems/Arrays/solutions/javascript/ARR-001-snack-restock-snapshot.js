const readline = require("readline");

class Solution {
  prefixAverages(arr) {
    const n = arr.length;
    const result = new Array(n);
    let sum = 0;

    for (let i = 0; i < n; i++) {
      sum += arr[i];
      // Math.floor for integer division
      result[i] = Math.floor(sum / (i + 1));
    }

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
  
  // Flatten data in case multiple lines
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;
  
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(Number(tokens[ptr++]));
  }

  const solution = new Solution();
  const result = solution.prefixAverages(arr);
  console.log(result.join(" "));
});
