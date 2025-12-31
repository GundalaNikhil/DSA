const readline = require("readline");

class Solution {
  invert_vandermonde(n, MOD, x) {
    const P_MOD = BigInt(MOD);
    const X = x.map(BigInt);

    function power(base, exp) {
      let res = 1n;
      base %= P_MOD;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % P_MOD;
        base = (base * base) % P_MOD;
        exp /= 2n;
      }
      return res;
    }

    function modInverse(n) {
      return power(n, P_MOD - 2n);
    }

    const P = new Array(n + 1).fill(0n);
    P[0] = 1n;

    for (let k = 0; k < n; k++) {
      for (let i = k + 1; i >= 1; i--) {
        P[i] = (P[i - 1] - X[k] * P[i] % P_MOD + P_MOD) % P_MOD;
      }
      P[0] = (P_MOD - X[k] * P[0] % P_MOD) % P_MOD;
    }

    const inv = Array.from({ length: n }, () => new Array(n).fill(0n));

    for (let i = 0; i < n; i++) {
      let prod = 1n;
      for (let j = 0; j < n; j++) {
        if (i === j) continue;
        prod = (prod * (X[i] - X[j] + P_MOD)) % P_MOD;
      }
      const w = modInverse(prod);

      let q_k = 0n;
      for (let k = n; k >= 1; k--) {
        const val = (P[k] + X[i] * q_k) % P_MOD;
        q_k = val;
        inv[k - 1][i] = (val * w) % P_MOD;
      }
    }

    return inv.map(row => row.map(val => Number(val)));
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
  
  const x = [];
  for(let i=0; i<n; i++) x.push(parseInt(data[ptr++]));
  
  const solution = new Solution();
  const res = solution.invert_vandermonde(n, MOD, x);
  
  for (let i = 0; i < n; i++) {
    console.log(res[i].join(" "));
  }
});
