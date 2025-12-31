const readline = require("readline");

class Solution {
  oddAfterBitSalt(a, salt) {
    let result = 0;
    for (const x of a) {
      result ^= (x ^ salt);
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
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const a = [];
    for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
    
    const salt = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(String(solution.oddAfterBitSalt(a, salt)));
});
