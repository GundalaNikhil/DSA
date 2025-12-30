const readline = require("readline");

class Solution {
  maxGapAfterRemovals(seats, removeIndices) {
    const n = seats.length;
    // Using Set for cleaner lookups or Uint8Array for performance
    const removed = new Uint8Array(n);
    
    for (const idx of removeIndices) {
      removed[idx] = 1;
    }
    
    let maxGap = 0;
    let lastPos = null;
    
    for (let i = 0; i < n; i++) {
      if (removed[i] === 0) {
        const currentPos = seats[i];
        if (lastPos !== null) {
          const gap = currentPos - lastPos;
          if (gap > maxGap) {
            maxGap = gap;
          }
        }
        lastPos = currentPos;
      }
    }
    
    return maxGap;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const seats = [];
    for (let i = 0; i < n; i++) seats.push(Number(tokens[ptr++]));
    
    const r = Number(tokens[ptr++]);
    const removeIndices = [];
    for (let i = 0; i < r; i++) removeIndices.push(Number(tokens[ptr++]));
    
    const solution = new Solution();
    console.log(solution.maxGapAfterRemovals(seats, removeIndices));
});
