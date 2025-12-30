const readline = require("readline");

class Complex {
  constructor(r, i) { this.r = r; this.i = i; }
  add(o) { return new Complex(this.r + o.r, this.i + o.i); }
  sub(o) { return new Complex(this.r - o.r, this.i - o.i); }
  mul(o) { return new Complex(this.r * o.r - this.i * o.i, this.r * o.i + this.i * o.r); }
}

function fft(a, invert) {
  const n = a.length;
  for (let i = 1, j = 0; i < n; i++) {
    let bit = n >> 1;
    for (; j & bit; bit >>= 1) j ^= bit;
    j ^= bit;
    if (i < j) [a[i], a[j]] = [a[j], a[i]];
  }
  for (let len = 2; len <= n; len <<= 1) {
    const ang = 2 * Math.PI / len * (invert ? -1 : 1);
    const wlen = new Complex(Math.cos(ang), Math.sin(ang));
    for (let i = 0; i < n; i += len) {
      let w = new Complex(1, 0);
      for (let j = 0; j < len / 2; j++) {
        const u = a[i + j];
        const v = a[i + j + len / 2].mul(w);
        a[i + j] = u.add(v);
        a[i + j + len / 2] = u.sub(v);
        w = w.mul(wlen);
      }
    }
  }
  if (invert) {
    for (let i = 0; i < n; i++) { a[i].r /= n; a[i].i /= n; }
  }
}

class Solution {
  multiplyPolynomials(A, B) {
    const MOD = 1000000007n;
    let n = 1;
    while (n < A.length + B.length) n <<= 1;
    
    const S = 32000;
    const a0 = new Array(n).fill(null).map(() => new Complex(0, 0));
    const a1 = new Array(n).fill(null).map(() => new Complex(0, 0));
    const b0 = new Array(n).fill(null).map(() => new Complex(0, 0));
    const b1 = new Array(n).fill(null).map(() => new Complex(0, 0));
    
    for(let i=0; i<n; i++) {
        if (i < A.length) {
            a0[i].r = A[i] % S;
            a1[i].r = Math.floor(A[i] / S);
        }
        if (i < B.length) {
            b0[i].r = B[i] % S;
            b1[i].r = Math.floor(B[i] / S);
        }
    }
    
    fft(a0, false); fft(a1, false);
    fft(b0, false); fft(b1, false);
    
    const c0 = new Array(n), c1 = new Array(n), c2 = new Array(n);
    for(let i=0; i<n; i++) {
        c0[i] = a0[i].mul(b0[i]);
        c2[i] = a1[i].mul(b1[i]);
        const sumA = a0[i].add(a1[i]);
        const sumB = b0[i].add(b1[i]);
        c1[i] = sumA.mul(sumB).sub(c0[i]).sub(c2[i]);
    }
    
    fft(c0, true); fft(c1, true); fft(c2, true);
    
    const res = [];
    const Sn = BigInt(S);
    for(let i=0; i < A.length + B.length - 1; i++) {
        const v0 = BigInt(Math.round(c0[i].r)) % MOD;
        const v1 = BigInt(Math.round(c1[i].r)) % MOD;
        const v2 = BigInt(Math.round(c2[i].r)) % MOD;
        
        let val = (v2 * Sn * Sn + v1 * Sn + v0) % MOD;
        res.push(Number(val));
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
  const A = [];
  for(let i=0; i<n; i++) A.push(parseInt(data[ptr++]));
  
  const m = parseInt(data[ptr++]);
  const B = [];
  for(let i=0; i<m; i++) B.push(parseInt(data[ptr++]));

  const solution = new Solution();
  const result = solution.multiplyPolynomials(A, B);
  console.log(result.join(" "));
});
