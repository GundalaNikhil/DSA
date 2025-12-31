const readline = require("readline");

function hitProbability(a, b, T) {
  if (a === 0 && b === 0) return 1.0;
  
  const offset = T;
  const size = 2 * T + 1;
  let dp = new Float64Array(size * size);
  
  const targetX = a + offset;
  const targetY = b + offset;
  
  // Helper for 2D index
  const idx = (x, y) => x * size + y;
  
  dp[idx(offset, offset)] = 1.0;
  
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];
  
  for (let t = 1; t <= T; t++) {
    const nextDp = new Float64Array(size * size);
    
    // Carry over absorbed probability
    nextDp[idx(targetX, targetY)] = dp[idx(targetX, targetY)];
    
    const minVal = Math.max(0, offset - (t - 1));
    const maxVal = Math.min(size - 1, offset + (t - 1));
    
    for (let x = minVal; x <= maxVal; x++) {
      for (let y = minVal; y <= maxVal; y++) {
        const currIdx = idx(x, y);
        const val = dp[currIdx];
        
        if (val === 0) continue;
        if (x === targetX && y === targetY) continue;
        
        const prob = val * 0.25;
        for (let i = 0; i < 4; i++) {
          const nx = x + dx[i];
          const ny = y + dy[i];
          const nIdx = idx(nx, ny);
          nextDp[nIdx] += prob;
        }
      }
    }
    dp = nextDp;
  }
  
  return dp[idx(targetX, targetY)];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const a = parseInt(data[0], 10);
  const b = parseInt(data[1], 10);
  const T = parseInt(data[2], 10);
  console.log(hitProbability(a, b, T).toFixed(6));
});
