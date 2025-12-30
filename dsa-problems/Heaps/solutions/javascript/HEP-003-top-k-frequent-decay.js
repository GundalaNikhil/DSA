const readline = require("readline");

class MaxHeap {
  constructor() {
    this.data = [];
  }
  isEmpty() {
    return this.data.length === 0;
  }
  better(a, b) {
    if (a.score === b.score) return a.key < b.key;
    return a.score > b.score;
  }
  push(item) {
    this.data.push(item);
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    if (this.data.length === 0) return null;
    const top = this.data[0];
    const last = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = last;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.better(this.data[idx], this.data[pIdx])) {
        [this.data[idx], this.data[pIdx]] = [this.data[pIdx], this.data[idx]];
        idx = pIdx;
      } else {
        break;
      }
    }
  }
  bubbleDown(idx) {
    const n = this.data.length;
    while (true) {
      let best = idx;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      if (left < n && this.better(this.data[left], this.data[best])) best = left;
      if (right < n && this.better(this.data[right], this.data[best])) best = right;
      if (best === idx) break;
      [this.data[idx], this.data[best]] = [this.data[best], this.data[idx]];
      idx = best;
    }
  }
}

class Solution {
  processOperations(d, k, operations) {
    const state = new Map();
    const heap = new MaxHeap();
    const results = [];
    const ln2 = Math.log(2.0);

    for (const opData of operations) {
      const op = opData[0];
      if (op === "ADD") {
        const key = opData[1];
        const t = parseInt(opData[2], 10);
        const bucket = Math.floor(t / d);

        let st = state.get(key);
        if (!st) {
          st = { count: 0.0, bucket: bucket, score: 0.0, version: 0 };
        } else if (bucket > st.bucket) {
          const diff = bucket - st.bucket;
          st.count *= Math.pow(0.5, diff);
        }

        st.count += 1.0;
        st.bucket = bucket;
        st.score = Math.log(st.count) + st.bucket * ln2;
        st.version += 1;
        state.set(key, st);
        heap.push({ key: key, score: st.score, version: st.version });
      } else {
        const out = [];
        const used = [];

        while (!heap.isEmpty() && out.length < k) {
          const e = heap.pop();
          const st = state.get(e.key);
          if (!st || st.version !== e.version) continue;
          out.push(e.key);
          used.push(e);
        }

        for (const e of used) heap.push(e);
        results.push(out.length ? out.join(" ") : "EMPTY");
      }
    }

    return results;
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
  let idx = 0;
  const q = parseInt(data[idx++]);
  const d = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "ADD") {
      const key = data[idx++];
      const t = data[idx++];
      operations.push([op, key, t]);
    } else {
      const t = data[idx++];
      operations.push([op, t]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(d, k, operations);
  console.log(result.join("\n"));
});
