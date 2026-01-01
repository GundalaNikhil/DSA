function canBalanceWithSkips(s, k) {
  let balance = 0;
  let skipsUsed = 0;

  for (let char of s) {
    if (char === "(") {
      balance++;
    } else {
      // char === ')'
      balance--;
      if (balance < 0) {
        // Need to skip this ')'
        skipsUsed++;
        balance = 0;
      }
    }
  }

  // Remaining balance are unmatched '('
  const totalSkipsNeeded = skipsUsed + balance;
  return totalSkipsNeeded <= k;
}


const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const k = parseInt(tokens[ptr++]);
    const sol = new Solution();
    console.log(sol.canBalanceWithSkips(s, k));
});
