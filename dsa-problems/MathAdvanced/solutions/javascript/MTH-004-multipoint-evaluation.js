const readline = require("readline");

class Solution {
  multipoint_evaluation(coeffs, points) {
    const MOD = 1000000007n;
    const results = [];
    
    const bigCoeffs = coeffs.map(BigInt);
    
    for (let i = 0; i < points.length; i++) {
        let x = BigInt(points[i]);
        let val = 0n;
        for (let j = bigCoeffs.length - 1; j >= 0; j--) {
            val = (val * x + bigCoeffs[j]) % MOD;
        }
        if (val < 0n) val += MOD;
        results.push(Number(val));
    }
    return results;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let ptr = 0;
  
  const d = parseInt(data[ptr++]);
  const n = parseInt(data[ptr++]);
  
  const coeffs = [];
  for(let i=0; i<=d; i++) coeffs.push(parseInt(data[ptr++]));
  
  const points = [];
  for(let i=0; i<n; i++) points.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const result = solution.multipoint_evaluation(coeffs, points);
  console.log(result.join(" "));
});
