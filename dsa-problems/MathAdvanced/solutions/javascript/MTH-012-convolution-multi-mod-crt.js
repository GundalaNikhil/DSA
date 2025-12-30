const readline = require("readline");

class Solution {
  convolution_multi_mod_crt(n, m, A, B, targetMod) {
    const TM = BigInt(targetMod);
    
    const bigA = A.map(BigInt);
    const bigB = B.map(BigInt);

    function power(base, exp, mod) {
      let res = 1n;
      base %= mod;
      while (exp > 0n) {
        if (exp % 2n === 1n) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2n;
      }
      return res;
    }

    function modInverse(n, mod) {
      return power(n, mod - 2n, mod);
    }

    function ntt(a, invert, mod, g) {
      const n = a.length;
      let j = 0;
      for (let i = 1; i < n; i++) {
        let bit = n >> 1;
        while (j & bit) {
          j ^= bit;
          bit >>= 1;
        }
        j ^= bit;
        if (i < j) [a[i], a[j]] = [a[j], a[i]];
      }

      for (let len = 2; len <= n; len <<= 1) {
        let wlen = power(g, (mod - 1n) / BigInt(len), mod);
        if (invert) wlen = modInverse(wlen, mod);
        for (let i = 0; i < n; i += len) {
          let w = 1n;
          for (let j = 0; j < len / 2; j++) {
            const u = a[i + j];
            const v = (a[i + j + len / 2] * w) % mod;
            a[i + j] = (u + v) % mod;
            a[i + j + len / 2] = (u - v + mod) % mod;
            w = (w * wlen) % mod;
          }
        }
      }

      if (invert) {
        const nInv = modInverse(BigInt(n), mod);
        for (let i = 0; i < n; i++) a[i] = (a[i] * nInv) % mod;
      }
    }

    function convolve(A, B, mod, g) {
      let size = 1;
      while (size < A.length + B.length) size <<= 1;
      const fa = new Array(size).fill(0n);
      const fb = new Array(size).fill(0n);
      for(let i=0; i<A.length; i++) fa[i] = A[i];
      for(let i=0; i<B.length; i++) fb[i] = B[i];

      ntt(fa, false, mod, g);
      ntt(fb, false, mod, g);
      for (let i = 0; i < size; i++) fa[i] = (fa[i] * fb[i]) % mod;
      ntt(fa, true, mod, g);
      return fa;
    }

    const P1 = 998244353n, G1 = 3n;
    const P2 = 1004535809n, G2 = 3n;
    const P3 = 469762049n, G3 = 3n;

    const c1 = convolve(bigA, bigB, P1, G1);
    const c2 = convolve(bigA, bigB, P2, G2);
    const c3 = convolve(bigA, bigB, P3, G3);

    const len = n + m - 1;
    const res = [];

    const P1_inv_P2 = modInverse(P1, P2);
    const P1P2_inv_P3 = modInverse((P1 * P2) % P3, P3);

    for (let i = 0; i < len; i++) {
      const a1 = c1[i];
      const a2 = c2[i];
      const a3 = c3[i];

      const x1 = a1;
      const x2 = ((a2 - x1 + P2) % P2 * P1_inv_P2) % P2;
      const x3 = ((a3 - x1 - x2 * P1 % P3 + 2n * P3) % P3 * P1P2_inv_P3) % P3;

      let ans = (x1 + x2 * P1) % TM;
      ans = (ans + (x3 * ((P1 * P2) % TM)) % TM) % TM;
      res.push(Number(ans));
    }

    return res;
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
  const m = parseInt(data[ptr++]);
  
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const B = [];
  for(let i=0; i<m; i++) B.push(parseInt(data[ptr++]));
  
  const MOD = parseInt(data[ptr++]);
  
  const solution = new Solution();
  const result = solution.convolution_multi_mod_crt(n, m, A, B, MOD);
  console.log(result.join(" "));
});
