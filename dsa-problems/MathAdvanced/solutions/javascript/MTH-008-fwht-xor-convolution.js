const readline = require("readline");

class Solution {
  fwht_xor_convolution(k, A, B) {
    const MOD = 1000000007n;
    const n = 1 << k;
    
    // Convert to BigInt
    const bigA = A.map(BigInt);
    const bigB = B.map(BigInt);

    function power(base, exp) {
      let res = 1n;
      base %= MOD;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2n;
      }
      return res;
    }

    function modInverse(n) {
      return power(n, MOD - 2n);
    }

    function fwht(a, invert) {
      for (let len = 1; len < n; len <<= 1) {
        for (let i = 0; i < n; i += 2 * len) {
          for (let j = 0; j < len; j++) {
            const u = a[i + j];
            const v = a[i + j + len];
            a[i + j] = (u + v) % MOD;
            a[i + j + len] = (u - v + MOD) % MOD;
          }
        }
      }
      if (invert) {
        const invN = modInverse(BigInt(n));
        for (let i = 0; i < n; i++) {
          a[i] = (a[i] * invN) % MOD;
        }
      }
    }

    fwht(bigA, false);
    fwht(bigB, false);

    const bigC = new Array(n);
    for (let i = 0; i < n; i++) {
      bigC[i] = (bigA[i] * bigB[i]) % MOD;
    }

    fwht(bigC, true);

    return bigC.map(x => Number(x));
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
  const n = 1 << k;
  
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const B = [];
  for(let i=0; i<n; i++) B.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const result = solution.fwht_xor_convolution(k, A, B);
  console.log(result.join(" "));
});
