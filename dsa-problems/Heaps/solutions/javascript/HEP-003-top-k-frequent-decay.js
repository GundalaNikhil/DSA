const readline = require("readline");

class MaxHeap {
  constructor() {
    this.data = [];
  }
  isEmpty() {
    return this.data.length === 0;
  }
  better(a, b) {
    // a is "better" if it should be higher in heap
    // Higher count = better
    // Equal count = lexicographically smaller key = better
    if (Math.abs(a.count - b.count) > 1e-9) return a.count > b.count;
    return a.key < b.key;
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
    
    for (const opData of operations) {
      const op = opData[0];
      if (op === "ADD") {
        const key = opData[1];
        const t = parseInt(opData[2], 10);
        
        let current_count = 0.0;
        let st = state.get(key);
        
        if (st) {
          if (t >= st.last_update) {
            const steps = Math.floor((t - st.last_update) / d);
            if (steps > 0) {
              st.count *= Math.pow(0.5, steps);
            }
          }
          current_count = st.count;
        }
        
        const new_count = current_count + 1.0;
        // if reusing 'st', we need to be careful. Create clean new state object for safety/clarity
        const new_ver = (st ? st.version + 1 : 1);
        
        const newState = {
          count: new_count,
          last_update: t,
          version: new_ver
        };
        state.set(key, newState);
        
        heap.push({ count: new_count, key: key, version: new_ver });
        
      } else {
        const t = parseInt(opData[1], 10);
        const top_k = [];
        const temp_back = [];
        
        while (top_k.length < k && !heap.isEmpty()) {
          const e = heap.pop();
          const st = state.get(e.key);
          
          if (!st || st.version !== e.version) continue;
          
          let steps = 0;
          if (t >= st.last_update) {
            steps = Math.floor((t - st.last_update) / d);
          }
          
          if (steps > 0) {
            st.count *= Math.pow(0.5, steps);
            st.last_update += steps * d;
            st.version += 1;
            
            heap.push({ count: st.count, key: e.key, version: st.version });
          } else {
            top_k.push(e.key);
            temp_back.push(e);
          }
        }
        
        if (top_k.length === 0) {
          results.push("EMPTY");
        } else {
          results.push(top_k.join(" "));
        }
        
        for (const e of temp_back) {
          heap.push(e);
        }
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
