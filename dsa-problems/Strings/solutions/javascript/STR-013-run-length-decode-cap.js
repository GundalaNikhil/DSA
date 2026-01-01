function decodeWithCap(s, cap) {
  const result = [];
  let i = 0;
  const n = s.length;

  while (i < n) {
    // Read character
    const char = s[i];
    i++;

    // Read count
    let countStr = "";
    while (i < n && /\d/.test(s[i])) {
      countStr += s[i];
      i++;
    }

    // Decode with cap
    const count = countStr ? parseInt(countStr) : 1;
    const actualCount = Math.min(count, cap);

    result.push(char.repeat(actualCount));
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
    const cap = parseInt(tokens[ptr++]);
    const sol = new Solution();
    console.log(sol.decodeWithCap(s, cap));
});
