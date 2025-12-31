const readline = require("readline");

class Solution {
  findMatrix(A, B) {
    const n = A.length, m = A[0].length;
    const p = B.length, q = B[0].length;
    
    if (p > n || q > m) return false;
    
    const MOD = 1000000007n;
    const BASE1 = 313n;
    const BASE2 = 317n;
    
    const computeMatrixHash = (M, rows, cols) => {
      const rowH = new BigInt64Array(rows);
      for (let i = 0; i < rows; i++) {
        let h = 0n;
        for (let j = 0; j < cols; j++) {
          h = (h * BASE1 + BigInt(M[i][j])) % MOD;
        }
        rowH[i] = h;
      }
      let finalH = 0n;
      for (let i = 0; i < rows; i++) {
        finalH = (finalH * BASE2 + rowH[i]) % MOD;
      }
      return finalH;
    };
    
    const targetHash = computeMatrixHash(B, p, q);
    
    // rowHashes[i][j]
    const rowHashes = Array.from({ length: n }, () => new BigInt64Array(m - q + 1));
    
    let power1 = 1n;
    for (let k = 0; k < q - 1; k++) power1 = (power1 * BASE1) % MOD;
    
    for (let i = 0; i < n; i++) {
      let h = 0n;
      for (let k = 0; k < q; k++) {
        h = (h * BASE1 + BigInt(A[i][k])) % MOD;
      }
      rowHashes[i][0] = h;
      
      for (let j = 1; j <= m - q; j++) {
        let remove = (BigInt(A[i][j - 1]) * power1) % MOD;
        h = (h - remove + MOD) % MOD;
        h = (h * BASE1 + BigInt(A[i][j + q - 1])) % MOD;
        rowHashes[i][j] = h;
      }
    }
    
    let power2 = 1n;
    for (let k = 0; k < p - 1; k++) power2 = (power2 * BASE2) % MOD;
    
    for (let j = 0; j <= m - q; j++) {
      let h = 0n;
      for (let k = 0; k < p; k++) {
        h = (h * BASE2 + rowHashes[k][j]) % MOD;
      }
      if (h === targetHash) return true;
      
      for (let i = 1; i <= n - p; i++) {
        let remove = (rowHashes[i - 1][j] * power2) % MOD;
        h = (h - remove + MOD) % MOD;
        h = (h * BASE2 + rowHashes[i + p - 1][j]) % MOD;
        
        if (h === targetHash) return true;
      }
    }
    
    return false;
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
  let ptr = 0;
  const [n, m] = data[ptr++].split(" ").map(Number);
  
  const A = [];
  for (let i = 0; i < n; i++) {
    A.push(data[ptr++].split(" ").map(Number));
  }
  
  const [p, q] = data[ptr++].split(" ").map(Number);
  
  const B = [];
  for (let i = 0; i < p; i++) {
    B.push(data[ptr++].split(" ").map(Number));
  }
  
  const solution = new Solution();
  console.log(solution.findMatrix(A, B) ? "true" : "false");
});
