const readline = require("readline");

class Solution {
  convolution(A, B, MOD) {
    const G = 3n;
    const P = BigInt(MOD);

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

    function ntt(a, invert) {
      const n = a.length;
      for (let i = 1, j = 0; i < n; i++) {
        let bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) [a[i], a[j]] = [a[j], a[i]];
      }

      for (let len = 2; len <= n; len <<= 1) {
        let wlen = power(G, (P - 1n) / BigInt(len));
        if (invert) wlen = modInverse(wlen);

        for (let i = 0; i < n; i += len) {
          let w = 1n;
          for (let j = 0; j < len / 2; j++) {
            const u = a[i + j];
            const v = (a[i + j + len / 2] * w) % P;
            a[i + j] = (u + v) % P;
            a[i + j + len / 2] = (u - v + P) % P;
            w = (w * wlen) % P;
          }
        }
      }

      if (invert) {
        const nInv = modInverse(BigInt(n));
        for (let i = 0; i < n; i++) {
          a[i] = (a[i] * nInv) % P;
        }
      }
    }

    let size = 1;
    while (size < A.length + B.length) size <<= 1;

    const fa = new Array(size).fill(0n);
    const fb = new Array(size).fill(0n);

    for (let i = 0; i < A.length; i++) fa[i] = BigInt(A[i]);
    for (let i = 0; i < B.length; i++) fb[i] = BigInt(B[i]);

    ntt(fa, false);
    ntt(fb, false);

    for (let i = 0; i < size; i++) {
      fa[i] = (fa[i] * fb[i]) % P;
    }

    ntt(fa, true);

    const result = [];
    for (let i = 0; i < A.length + B.length - 1; i++) {
      result.push(Number(fa[i]));
    }
    return result;
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
  const MOD = 998244353;
  let ptr = 0;

  const n = parseInt(data[ptr++]);
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const m = parseInt(data[ptr++]);
  const B = [];
  for(let i=0; i<m; i++) B.push(parseInt(data[ptr++]));

  const solution = new Solution();
  const result = solution.convolution(A, B, MOD);
  console.log(result.join(" "));
});
