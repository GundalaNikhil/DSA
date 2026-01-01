function countEqualDistinctSplits(s) {
  const n = s.length;
  if (n < 2) return 0;

  // Build suffix distinct counts
  const suffixDistinct = new Array(n + 1).fill(0);
  const charSet = new Set();
  for (let i = n - 1; i >= 0; i--) {
    charSet.add(s[i]);
    suffixDistinct[i] = charSet.size;
  }

  // Scan left and compare
  const leftSet = new Set();
  let count = 0;
  for (let i = 0; i < n - 1; i++) {
    leftSet.add(s[i]);
    if (leftSet.size === suffixDistinct[i + 1]) {
      count++;
    }
  }

  return count;
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
    console.log(sol.countEqualDistinctSplits(s));
});
