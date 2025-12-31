const readline = require("readline");

class Solution {
  determinant_gaussian(n, MOD, matrix) {
    const P = BigInt(MOD);
    let det = 1n;
    
    // Convert matrix to BigInt
    const mat = matrix.map(row => row.map(BigInt));

    function power(base, exp) {
      let res = 1n;
      base %= P;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % P;
        base = (base * base) % P;
        exp /= 2n;
      }
      return res;
    }

    function modInverse(n) {
      return power(n, P - 2n);
    }

    for (let i = 0; i < n; i++) {
      let pivot = i;
      while (pivot < n && mat[pivot][i] === 0n) pivot++;

      if (pivot === n) return 0;

      if (pivot !== i) {
        [mat[i], mat[pivot]] = [mat[pivot], mat[i]];
        det = (P - det) % P;
      }

      det = (det * mat[i][i]) % P;
      const inv = modInverse(mat[i][i]);

      for (let j = i + 1; j < n; j++) {
        if (mat[j][i] !== 0n) {
          const factor = (mat[j][i] * inv) % P;
          for (let k = i; k < n; k++) {
            const sub = (factor * mat[i][k]) % P;
            mat[j][k] = (mat[j][k] - sub + P) % P;
          }
        }
      }
    }

    return Number(det);
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
  
  const n = parseInt(data[ptr++]);
  const MOD = parseInt(data[ptr++]);
  
  const matrix = [];
  for(let i=0; i<n; i++) {
      const row = [];
      for(let j=0; j<n; j++) row.push(parseInt(data[ptr++]));
      matrix.push(row);
  }
  
  const solution = new Solution();
  console.log(solution.determinant_gaussian(n, MOD, matrix));
});
