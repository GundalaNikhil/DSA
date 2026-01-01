function compressWithWindow(s, w) {
  if (!s) {
    return "";
  }

  const result = [];
  let i = 0;
  const n = s.length;

  while (i < n) {
    const start = i;
    const char = s[i];

    // Count consecutive occurrences
    while (i < n && s[i] === char) {
      i++;
    }

    const runLength = i - start;

    // Compress if >= threshold
    if (runLength >= w) {
      result.push(char + runLength);
    } else {
      result.push(char.repeat(runLength));
    }
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
    const w = parseInt(tokens[ptr++]);
    const sol = new Solution();
    console.log(sol.compressWithWindow(s, w));
});
