class Solution {
  process(arr, ops) {
    // Use BigInt for values to be safe, though 2e14 fits in double (safe integer limit 9e15).
    // Standard numbers are fine.
    
    const n = arr.length;
    // Heuristic block size
    let blockSize = Math.floor(Math.sqrt(n * Math.log2(n + 1))) + 1;
    if (blockSize < 100) blockSize = 100;
    
    const numBlocks = Math.ceil(n / blockSize);
    const blocks = [];
    
    // Initialize blocks
    for (let i = 0; i < numBlocks; i++) {
      const start = i * blockSize;
      const end = Math.min(n, start + blockSize);
      const sorted = arr.slice(start, end).sort((a, b) => a - b);
      blocks.push({ sorted: new Float64Array(sorted), lazy: 0 });
    }
    
    // We need a mutable array for partial updates
    // arr is already mutable
    
    const results = [];
    
    const upperBound = (arr, val) => {
      let l = 0, r = arr.length;
      while (l < r) {
        const mid = (l + r) >>> 1;
        if (arr[mid] > val) r = mid;
        else l = mid + 1;
      }
      return l;
    };

    const countLessEqual = (l, r, val) => {
      let count = 0;
      const startBlock = Math.floor(l / blockSize);
      const endBlock = Math.floor(r / blockSize);
      
      if (startBlock === endBlock) {
        const lazy = blocks[startBlock].lazy;
        for (let i = l; i <= r; i++) {
          if (arr[i] + lazy <= val) count++;
        }
      } else {
        const lazyStart = blocks[startBlock].lazy;
        const startLimit = (startBlock + 1) * blockSize;
        for (let i = l; i < startLimit; i++) {
          if (arr[i] + lazyStart <= val) count++;
        }
        
        for (let i = startBlock + 1; i < endBlock; i++) {
          const b = blocks[i];
          const target = val - b.lazy;
          count += upperBound(b.sorted, target);
        }
        
        const lazyEnd = blocks[endBlock].lazy;
        const endStart = endBlock * blockSize;
        for (let i = endStart; i <= r; i++) {
          if (arr[i] + lazyEnd <= val) count++;
        }
      }
      return count;
    };

    const update = (l, r, x) => {
      const startBlock = Math.floor(l / blockSize);
      const endBlock = Math.floor(r / blockSize);
      
      const partialUpdate = (bIdx, l, r) => {
        const b = blocks[bIdx];
        const start = bIdx * blockSize;
        const end = Math.min(n, start + blockSize);
        
        if (b.lazy !== 0) {
          for (let i = start; i < end; i++) arr[i] += b.lazy;
          b.lazy = 0;
        }
        
        for (let i = l; i <= r; i++) arr[i] += x;
        
        // Rebuild sorted
        // Creating new Float64Array is fast enough
        const chunk = arr.slice(start, end).sort((a, b) => a - b);
        b.sorted = new Float64Array(chunk);
      };

      if (startBlock === endBlock) {
        partialUpdate(startBlock, l, r);
      } else {
        partialUpdate(startBlock, l, (startBlock + 1) * blockSize - 1);
        for (let i = startBlock + 1; i < endBlock; i++) {
          blocks[i].lazy += x;
        }
        partialUpdate(endBlock, endBlock * blockSize, r);
      }
    };

    for (const op of ops) {
      if (op[0] === "ADD") {
        update(parseInt(op[1]), parseInt(op[2]), parseInt(op[3]));
      } else {
        const l = parseInt(op[1]);
        const r = parseInt(op[2]);
        const k = parseInt(op[3]);
        
        let low = -200000000000000;
        let high = 200000000000000;
        let ans = high;
        
        while (low <= high) {
          const mid = Math.floor((low + high) / 2);
          if (countLessEqual(l, r, mid) >= k) {
            ans = mid;
            high = mid - 1;
          } else {
            low = mid + 1;
          }
        }
        results.push(ans);
      }
    }
    return results;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const ops = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    ops.push([type, data[idx++], data[idx++], data[idx++]]);
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
