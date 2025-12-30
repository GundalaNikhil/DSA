const readline = require("readline");

const INF = 10n ** 30n;

class Deque {
  constructor() {
    this.a = [];
    this.h = 0;
  }
  pushBack(x) { this.a.push(x); }
  popBack() { this.a.pop(); }
  popFront() { this.h++; }
  front() { return this.a[this.h]; }
  back() { return this.a[this.a.length - 1]; }
  empty() { return this.h >= this.a.length; }
  cleanup() {
    if (this.h > 1024 && this.h * 2 > this.a.length) {
      this.a = this.a.slice(this.h);
      this.h = 0;
    }
  }
}

class Solution {
  minCost(k, target, d, c, p) {
    let dp = new Array(target + 1).fill(INF);
    dp[0] = 0n;

    for (let i = 0; i < k; i++) {
      const denom = d[i];
      const cap = Math.min(c[i], Math.floor(target / denom));
      const t = Math.min(Math.floor(c[i] / 2), cap);
      const penalty = BigInt(p[i]);

      const nxt = new Array(target + 1).fill(INF);

      for (let r = 0; r < denom; r++) {
        const qMax = Math.floor((target - r) / denom);
        if (qMax < 0) continue;

        const L1 = Math.min(cap, t);
        const dqNo = new Deque();
        const dqPen = new Deque();

        const key = (q) => {
          const s = r + q * denom;
          return dp[s] - BigInt(q);
        };

        for (let q = 0; q <= qMax; q++) {
          const sQ = r + q * denom;

          if (dp[sQ] < INF) {
            const kv = key(q);
            while (!dqNo.empty() && kv <= key(dqNo.back())) dqNo.popBack();
            dqNo.pushBack(q);
          }

          const minY = q - L1;
          while (!dqNo.empty() && dqNo.front() < minY) dqNo.popFront();
          dqNo.cleanup();

          let best = INF;
          if (!dqNo.empty()) {
            best = BigInt(q) + key(dqNo.front());
          }

          if (cap > t) {
            const yAdd = q - (t + 1);
            if (yAdd >= 0) {
              const sAdd = r + yAdd * denom;
              if (dp[sAdd] < INF) {
                const kv = key(yAdd);
                while (!dqPen.empty() && kv <= key(dqPen.back())) dqPen.popBack();
                dqPen.pushBack(yAdd);
              }
            }

            const minYPen = q - cap;
            while (!dqPen.empty() && dqPen.front() < minYPen) dqPen.popFront();
            dqPen.cleanup();

            if (!dqPen.empty()) {
              const cand = BigInt(q) + penalty + key(dqPen.front());
              if (cand < best) best = cand;
            }
          }

          const s = r + q * denom;
          if (best < nxt[s]) nxt[s] = best;
        }
      }

      dp = nxt;
    }

    return dp[target] >= INF ? -1 : dp[target].toString();
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [kStr, targetStr] = lines[idx++].split(" ");
  const k = Number(kStr);
  const target = Number(targetStr);
  const d = new Array(k), c = new Array(k), p = new Array(k);
  for (let i = 0; i < k; i++) {
    const [di, ci, pi] = lines[idx++].split(" ").map(Number);
    d[i] = di; c[i] = ci; p[i] = pi;
  }
  const sol = new Solution();
  console.log(sol.minCost(k, target, d, c, p));
});
