const readline = require("readline");

class Solution {
  maxSumGapThree(a) {
    let dp_i_3 = 0;
    let dp_i_2 = 0;
    let dp_i_1 = 0;

    for (const x of a) {
      const cur = Math.max(dp_i_1, x + dp_i_3);
      dp_i_3 = dp_i_2;
      dp_i_2 = dp_i_1;
      dp_i_1 = cur;
    }
    return dp_i_1;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  const n = Number(lines[0]);
  const a = lines[1].split(" ").map(Number);
  const sol = new Solution();
  console.log(sol.maxSumGapThree(a));
});
