const readline = require('readline');

class PyRandom {
  constructor(seed) {
    this.N = 624;
    this.M = 397;
    this.MATRIX_A = 0x9908b0df;
    this.UPPER_MASK = 0x80000000;
    this.LOWER_MASK = 0x7fffffff;
    this.mt = new Array(this.N);
    this.mti = this.N + 1;
    this.initByArray([seed >>> 0]);
  }

  initGenrand(s) {
    this.mt[0] = s >>> 0;
    for (this.mti = 1; this.mti < this.N; this.mti++) {
      const prev = this.mt[this.mti - 1];
      this.mt[this.mti] = (Math.imul(1812433253, (prev ^ (prev >>> 30))) + this.mti) >>> 0;
    }
  }

  initByArray(initKey) {
    this.initGenrand(19650218);
    let i = 1;
    let j = 0;
    let k = Math.max(this.N, initKey.length);
    for (; k > 0; k--) {
      const prev = this.mt[i - 1];
      this.mt[i] = (this.mt[i] ^ Math.imul(prev ^ (prev >>> 30), 1664525)) + initKey[j] + j;
      this.mt[i] >>>= 0;
      i++; j++;
      if (i >= this.N) { this.mt[0] = this.mt[this.N - 1]; i = 1; }
      if (j >= initKey.length) j = 0;
    }
    for (k = this.N - 1; k > 0; k--) {
      const prev = this.mt[i - 1];
      this.mt[i] = (this.mt[i] ^ Math.imul(prev ^ (prev >>> 30), 1566083941)) - i;
      this.mt[i] >>>= 0;
      i++;
      if (i >= this.N) { this.mt[0] = this.mt[this.N - 1]; i = 1; }
    }
    this.mt[0] = 0x80000000;
  }

  genrandInt32() {
    let y;
    const mag01 = [0x0, this.MATRIX_A];
    if (this.mti >= this.N) {
      let kk;
      for (kk = 0; kk < this.N - this.M; kk++) {
        y = (this.mt[kk] & this.UPPER_MASK) | (this.mt[kk + 1] & this.LOWER_MASK);
        this.mt[kk] = this.mt[kk + this.M] ^ (y >>> 1) ^ mag01[y & 0x1];
      }
      for (; kk < this.N - 1; kk++) {
        y = (this.mt[kk] & this.UPPER_MASK) | (this.mt[kk + 1] & this.LOWER_MASK);
        this.mt[kk] = this.mt[kk + (this.M - this.N)] ^ (y >>> 1) ^ mag01[y & 0x1];
      }
      y = (this.mt[this.N - 1] & this.UPPER_MASK) | (this.mt[0] & this.LOWER_MASK);
      this.mt[this.N - 1] = this.mt[this.M - 1] ^ (y >>> 1) ^ mag01[y & 0x1];
      this.mti = 0;
    }
    y = this.mt[this.mti++];
    y ^= y >>> 11;
    y ^= (y << 7) & 0x9d2c5680;
    y ^= (y << 15) & 0xefc60000;
    y ^= y >>> 18;
    return y >>> 0;
  }

  random() {
    const a = this.genrandInt32() >>> 5;
    const b = this.genrandInt32() >>> 6;
    return (a * 67108864.0 + b) / 9007199254740992.0;
  }

  getrandbits(k) {
    if (k <= 0) return 0;
    return this.genrandInt32() >>> (32 - k);
  }

  randbelow(n) {
    if (n <= 1) return 0;
    let t = n;
    let k = 0;
    while (t > 0) { k++; t >>= 1; }
    let r;
    do { r = this.getrandbits(k); } while (r >= n);
    return r;
  }
}

class Solution {
  solve(xL, yB, xR, yT, xs, ys) {
        let pts = xs.map((x, i) => ({x: Number(x), y: Number(ys[i])}));

        const getRadius = (x, y) => {
            if (x < xL || x > xR || y < yB || y > yT) return 0.0;
            let r = Math.min(x - xL, xR - x, y - yB, yT - y);
            if (r <= 1e-12) return 0.0;
            let minD2 = Number.POSITIVE_INFINITY;
            for (let p of pts) {
                let dx = x - p.x;
                let dy = y - p.y;
                let d2 = dx * dx + dy * dy;
                if (d2 < minD2) minD2 = d2;
                if (d2 < r * r) return Math.sqrt(d2);
            }
            return Math.min(r, Math.sqrt(minD2));
        };

        let candidates = [];
        candidates.push({x: (xL + xR) / 2, y: (yB + yT) / 2});
        for (let p of pts) {
            candidates.push({x: p.x, y: (p.y + yB) / 2});
            candidates.push({x: p.x, y: (p.y + yT) / 2});
            candidates.push({x: (p.x + xL) / 2, y: p.y});
            candidates.push({x: (p.x + xR) / 2, y: p.y});
        }
        if (pts.length <= 100) {
            for (let i = 0; i < pts.length; i++) {
                for (let j = i + 1; j < pts.length; j++) {
                    candidates.push({x: (pts[i].x + pts[j].x) / 2, y: (pts[i].y + pts[j].y) / 2});
                }
            }
        }

        let bestR = 0.0;
        for (let c of candidates) bestR = Math.max(bestR, getRadius(c.x, c.y));

        const rng = new PyRandom(1337);

        let starts = [];
        for (let i = 0; i < 10; i++) {
            starts.push({x: xL + rng.random() * (xR - xL), y: yB + rng.random() * (yT - yB)});
        }
        if (candidates.length > 0) {
            let scored = candidates.map((c, idx) => ({c, r: getRadius(c.x, c.y), idx}));
            scored.sort((a, b) => {
                if (a.r !== b.r) return b.r - a.r;
                if (a.c.x !== b.c.x) return b.c.x - a.c.x;
                if (a.c.y !== b.c.y) return b.c.y - a.c.y;
                return a.idx - b.idx;
            });
            for (let i = 0; i < Math.min(scored.length, 5); i++) starts.push(scored[i].c);
        }

        let stepSize = Math.max(xR - xL, yT - yB) / 2.0;
        let precision = 1e-4;
        const baseDirs = [
            {x: 0, y: 1}, {x: 0, y: -1}, {x: 1, y: 0}, {x: -1, y: 0},
            {x: 0.7, y: 0.7}, {x: 0.7, y: -0.7}, {x: -0.7, y: 0.7}, {x: -0.7, y: -0.7},
        ];

        const shuffle = (arr) => {
            for (let i = arr.length - 1; i > 0; i--) {
                const j = rng.randbelow(i + 1);
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        };

        for (let start of starts) {
            let currX = start.x;
            let currY = start.y;
            let currR = getRadius(currX, currY);
            let tempStep = stepSize;

            while (tempStep > precision) {
                let improved = false;
                let bestNeighR = currR;
                let bestNeighX = currX;
                let bestNeighY = currY;

                const dirs = baseDirs.slice();
                shuffle(dirs);
                for (let d of dirs) {
                    let nx = currX + d.x * tempStep;
                    let ny = currY + d.y * tempStep;
                    nx = Math.max(xL, Math.min(xR, nx));
                    ny = Math.max(yB, Math.min(yT, ny));
                    let nr = getRadius(nx, ny);
                    if (nr > bestNeighR) {
                        bestNeighR = nr;
                        bestNeighX = nx;
                        bestNeighY = ny;
                        improved = true;
                    }
                }

                if (improved) {
                    currX = bestNeighX;
                    currY = bestNeighY;
                    currR = bestNeighR;
                } else {
                    tempStep *= 0.6;
                }
            }
            bestR = Math.max(bestR, currR);
        }
        return bestR;
    }
}
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let lines = [];
rl.on('line', (line) => {
    let tokens = line.match(/\S+/g) || [];
    lines.push(...tokens);
});
rl.on('close', () => {
    if (lines.length === 0) return;
    let idx = 0;
    const next = () => lines[idx++];
    const nextInt = () => parseInt(next());

    let xL = nextInt(), yB = nextInt(), xR = nextInt(), yT = nextInt();
    let n = nextInt();
    let xs=[], ys=[];
    for(let i=0; i<n; i++) {
        xs.push(nextInt());
        ys.push(nextInt());
    }

    const sol = new Solution();
    console.log(sol.solve(xL, yB, xR, yT, xs, ys).toFixed(6));
});
