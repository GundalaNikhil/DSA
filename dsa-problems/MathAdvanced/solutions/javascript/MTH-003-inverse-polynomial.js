const readline = require("readline");

class Solution {
  inversePolynomial(P, n, MOD) {
    const G = 3n;
    const P_MOD = BigInt(MOD);

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

    function modInverse(x) {
      return power(x, P_MOD - 2n);
    }

    function ntt(a, invert) {
      const N = a.length;
      for (let i = 1, j = 0; i < N; i++) {
        let bit = N >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) [a[i], a[j]] = [a[j], a[i]];
      }
      for (let len = 2; len <= N; len <<= 1) {
        let wlen = power(G, (P_MOD - 1n) / BigInt(len));
        if (invert) wlen = modInverse(wlen);
        for (let i = 0; i < N; i += len) {
          let w = 1n;
          for (let j = 0; j < len / 2; j++) {
            const u = a[i + j];
            const v = (a[i + j + len / 2] * w) % P_MOD;
            a[i + j] = (u + v) % P_MOD;
            a[i + j + len / 2] = (u - v + P_MOD) % P_MOD;
            w = (w * wlen) % P_MOD;
          }
        }
      }
      if (invert) {
        const nInv = modInverse(BigInt(N));
        for (let i = 0; i < N; i++) a[i] = (a[i] * nInv) % P_MOD;
      }
    }

    let b = [modInverse(BigInt(P[0]))];
    let len = 1;
    while (len < n) {
      len <<= 1;
      const limit = len << 1;
      
      const copyA = new Array(limit).fill(0n);
      const copyB = new Array(limit).fill(0n);
      
      for(let i=0; i<Math.min(P.length, len); i++) copyA[i] = BigInt(P[i]);
      for(let i=0; i<b.length; i++) copyB[i] = b[i];
      
      ntt(copyA, false);
      ntt(copyB, false);
      
      for(let i=0; i<limit; i++) {
        const term = (copyA[i] * copyB[i]) % P_MOD;
        copyB[i] = (copyB[i] * (2n - term + P_MOD)) % P_MOD;
      }
      
      ntt(copyB, true);
      b = copyB.slice(0, len);
    }
    
    return b.slice(0, n).map(x => Number(x));
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
  const n = parseInt(data[ptr++]);
  const P = [];
  for(let i=0; i<k; i++) P.push(parseInt(data[ptr++]));
  const MOD = parseInt(data[ptr++]);

  const solution = new Solution();
  const result = solution.inversePolynomial(P, n, MOD);
  console.log(result.join(" "));
});
