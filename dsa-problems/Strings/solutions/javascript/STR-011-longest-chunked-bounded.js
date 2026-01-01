function longestChunkedDecomposition(s, L) {
  const n = s.length;
  let left = 0,
    right = n - 1;
  let chunks = 0;

  while (left < right) {
    let matched = false;
    const maxLen = Math.min(L, Math.floor((right - left + 1) / 2));

    for (let len = 1; len <= maxLen; len++) {
      const leftChunk = s.slice(left, left + len);
      const rightChunk = s.slice(right - len + 1, right + 1);

      if (leftChunk === rightChunk) {
        chunks += 2;
        left += len;
        right -= len;
        matched = true;
        break;
      }
    }

    if (!matched) {
      break;
    }
  }

  // Add middle chunk if exists
  if (left <= right) {
    chunks++;
  }

  return chunks;
}


const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const s = tokens[ptr++];
    const L = parseInt(tokens[ptr++]);
    const sol = new Solution();
    console.log(sol.longestChunkedDecomposition(s, L));
});
