class Solution {
  grayCode(n) {
    if (n === 1) return ["0", "1"];

    const prev = this.grayCode(n - 1);
    const result = [];

    for (const s of prev) {
      result.push("0" + s);
    }

    for (let i = prev.length - 1; i >= 0; i--) {
      result.push("1" + prev[i]);
    }

    return result;
  }
}










const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const n = parseInt(tokens[ptr++]);
    const sol = new Solution();
    const res = sol.grayCode(n);
    if(res.length===0) console.log('NONE'); else res.forEach(s => console.log(s));
});
