const readline = require("readline");

class Solution {
  minimalBitsFlipRange(x, y) {
    let diff = x ^ y;
    if (diff === 0n) return 0;
    
    // Check (diff & (diff + 1)) == 0
    if ((diff & (diff + 1n)) === 0n) {
      // Find bit length.
      return diff.toString(2).length;
    }
    
    return -1;
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
    
    const x = BigInt(tokens[0]);
    const y = BigInt(tokens[1]);
    
    const solution = new Solution();
    console.log(String(solution.minimalBitsFlipRange(x, y)));
});
