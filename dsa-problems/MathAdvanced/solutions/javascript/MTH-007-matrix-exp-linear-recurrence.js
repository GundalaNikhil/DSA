const readline = require("readline");

class Solution {
  matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial) {
    const P = BigInt(MOD);
    const N = BigInt(n);
    
    if (N < BigInt(k)) return Number(initial[Number(N)]);
    
    const K = k;

    function multiply(A, B) {
      const C = Array.from({ length: K }, () => Array(K).fill(0n));
      for (let i = 0; i < K; i++) {
        for (let l = 0; l < K; l++) {
          if (A[i][l] === 0n) continue;
          for (let j = 0; j < K; j++) {
            C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % P;
          }
        }
      }
      return C;
    }

    function power(A, exp) {
      let res = Array.from({ length: K }, () => Array(K).fill(0n));
      for (let i = 0; i < K; i++) res[i][i] = 1n;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = multiply(res, A);
        A = multiply(A, A);
        exp /= 2n;
      }
      return res;
    }

    let T = Array.from({ length: K }, () => Array(K).fill(0n));
    for (let j = 0; j < K; j++) T[0][j] = BigInt(coeffs[j]);
    for (let i = 1; i < K; i++) T[i][i - 1] = 1n;

    T = power(T, N - BigInt(K) + 1n);

    let ans = 0n;
    for (let j = 0; j < K; j++) {
      ans = (ans + T[0][j] * BigInt(initial[K - 1 - j])) % P;
    }

    return Number(ans);
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
  
  const k = parseInt(data[ptr++]);
  const n = BigInt(data[ptr++]); // Keep as BigInt or string
  const MOD = parseInt(data[ptr++]);
  
  const coeffs = [];
  for(let i=0; i<k; i++) coeffs.push(parseInt(data[ptr++]));
  
  const initial = [];
  for(let i=0; i<k; i++) initial.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  console.log(solution.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial));
});
