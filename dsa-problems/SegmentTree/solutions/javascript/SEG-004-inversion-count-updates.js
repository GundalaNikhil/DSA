class Solution {
  process(arr, updates) {
    const n = arr.length;
    const blockSize = Math.floor(Math.sqrt(n * Math.log2(n + 1))) + 1;
    const safeBlockSize = blockSize < 50 ? 50 : blockSize;
    
    const blocks = [];
    for (let i = 0; i < n; i += safeBlockSize) {
      const chunk = arr.slice(i, i + safeBlockSize);
      chunk.sort((a, b) => a - b);
      blocks.push(chunk);
    }
    
    // Initial inversions
    const countInversions = (a) => {
      let count = 0n;
      const mergeSort = (arr) => {
        if (arr.length <= 1) return arr;
        const mid = Math.floor(arr.length / 2);
        const left = mergeSort(arr.slice(0, mid));
        const right = mergeSort(arr.slice(mid));
        
        let i = 0, j = 0;
        const res = [];
        while (i < left.length && j < right.length) {
          if (left[i] <= right[j]) {
            res.push(left[i++]);
          } else {
            res.push(right[j++]);
            count += BigInt(left.length - i);
          }
        }
        return res.concat(left.slice(i)).concat(right.slice(j));
      };
      mergeSort(a);
      return count;
    };
    
    let currentInversions = countInversions([...arr]);
    const results = [];
    
    // Helper for binary search
    const upperBound = (list, val) => {
      let l = 0, r = list.length;
      while (l < r) {
        const mid = (l + r) >>> 1;
        if (list[mid] > val) r = mid;
        else l = mid + 1;
      }
      return l;
    };
    
    const lowerBound = (list, val) => {
      let l = 0, r = list.length;
      while (l < r) {
        const mid = (l + r) >>> 1;
        if (list[mid] >= val) r = mid;
        else l = mid + 1;
      }
      return l;
    };

    for (const [idx, val] of updates) {
      const oldVal = arr[idx];
      if (val === oldVal) {
        results.push(currentInversions.toString());
        continue;
      }
      
      const bIdx = Math.floor(idx / safeBlockSize);
      
      // Remove oldVal
      for (let i = 0; i < bIdx; i++) {
        const b = blocks[i];
        const pos = upperBound(b, oldVal);
        currentInversions -= BigInt(b.length - pos);
      }
      
      const start = bIdx * safeBlockSize;
      for (let i = start; i < idx; i++) {
        if (arr[i] > oldVal) currentInversions--;
      }
      
      const end = Math.min((bIdx + 1) * safeBlockSize, n);
      for (let i = idx + 1; i < end; i++) {
        if (arr[i] < oldVal) currentInversions--;
      }
      
      for (let i = bIdx + 1; i < blocks.length; i++) {
        const b = blocks[i];
        const pos = lowerBound(b, oldVal);
        currentInversions -= BigInt(pos);
      }
      
      // Update
      arr[idx] = val;
      const block = blocks[bIdx];
      const removePos = lowerBound(block, oldVal);
      block.splice(removePos, 1);
      const insertPos = upperBound(block, val); // Insert to maintain stability/order
      // Actually lowerBound or upperBound works for insert position to keep sorted
      // Let's use lowerBound to keep identicals together
      const insertPos2 = lowerBound(block, val);
      block.splice(insertPos2, 0, val);
      
      // Add val
      for (let i = 0; i < bIdx; i++) {
        const b = blocks[i];
        const pos = upperBound(b, val);
        currentInversions += BigInt(b.length - pos);
      }
      
      for (let i = start; i < idx; i++) {
        if (arr[i] > val) currentInversions++;
      }
      
      for (let i = idx + 1; i < end; i++) {
        if (arr[i] < val) currentInversions++;
      }
      
      for (let i = bIdx + 1; i < blocks.length; i++) {
        const b = blocks[i];
        const pos = lowerBound(b, val);
        currentInversions += BigInt(pos);
      }
      
      results.push(currentInversions.toString());
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
  const updates = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++]; // SET
    updates.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }
  const solution = new Solution();
  const out = solution.process(arr, updates);
  console.log(out.join("\n"));
});
