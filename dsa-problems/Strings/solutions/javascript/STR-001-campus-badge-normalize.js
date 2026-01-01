function normalizeBadge(s) {
  if (!s) return "";

  let result = [];
  let lastWasAlnum = false;

  for (let c of s) {
    if (/[a-zA-Z0-9]/.test(c)) {
      result.push(c.toLowerCase());
      lastWasAlnum = true;
    } else {
      // Non-alphanumeric character
      if (lastWasAlnum && result.length > 0) {
        result.push("-");
        lastWasAlnum = false;
      }
    }
  }

  // Remove trailing hyphen if present
  if (result.length > 0 && result[result.length - 1] === "-") {
    result.pop();
  }

  return result.join("");
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
    console.log(sol.normalizeBadge(s));
});
