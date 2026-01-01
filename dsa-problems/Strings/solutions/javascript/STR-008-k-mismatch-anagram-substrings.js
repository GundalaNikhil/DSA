function countKMismatchAnagrams(s, p, k) {
  const m = p.length;
  const n = s.length;

  if (n < m) return 0;

  // Build pattern frequency
  const freqP = new Array(26).fill(0);
  for (let c of p) {
    freqP[c.charCodeAt(0) - 97]++;
  }

  // Initialize window frequency
  const freqWindow = new Array(26).fill(0);
  for (let i = 0; i < m; i++) {
    freqWindow[s.charCodeAt(i) - 97]++;
  }

  function mismatchCost(fw, fp) {
    let cost = 0;
    for (let i = 0; i < 26; i++) {
      if (fp[i] > fw[i]) {
        cost += fp[i] - fw[i];
      }
    }
    return cost;
  }

  let count = 0;

  // Check first window
  if (mismatchCost(freqWindow, freqP) <= k) {
    count++;
  }

  // Slide window
  for (let i = 1; i <= n - m; i++) {
    // Remove leftmost
    freqWindow[s.charCodeAt(i - 1) - 97]--;
    // Add rightmost
    freqWindow[s.charCodeAt(i + m - 1) - 97]++;

    if (mismatchCost(freqWindow, freqP) <= k) {
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
    const p = tokens[ptr++];
    const k = parseInt(tokens[ptr++]);
    const sol = new Solution();
    console.log(sol.countKMismatchAnagrams(s, p, k));
});
