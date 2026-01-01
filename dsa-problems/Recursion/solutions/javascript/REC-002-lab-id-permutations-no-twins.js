class Solution {
  generatePermutations(s) {
    const chars = s.split("").sort();
    const n = chars.length;
    const used = new Array(n).fill(false);
    const result = [];

    const backtrack = (current) => {
      if (current.length === n) {
        result.push(current.join(""));
        return;
      }

      for (let i = 0; i < n; i++) {
        if (used[i]) continue;

        // Skip duplicates
        if (i > 0 && chars[i] === chars[i - 1] && !used[i - 1]) continue;

        // Constraint: No adjacent twins
        if (current.length > 0 && current[current.length - 1] === chars[i]) continue;

        used[i] = true;
        current.push(chars[i]);
        backtrack(current);
        current.pop();
        used[i] = false;
      }
    };

    backtrack([]);
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
    const s = tokens[ptr++];
    const sol = new Solution();
    const res = sol.generatePermutations(s);
    if(res.length===0) console.log('NONE'); else res.forEach(s => console.log(s));
});
