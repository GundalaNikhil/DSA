class Solution {
  process(arr, ops) {
    const n = arr.length;
    const blockSize = Math.floor(Math.sqrt(n * Math.log2(n + 1))) + 1;
    const safeBlockSize = blockSize < 50 ? 50 : blockSize;
    
    const blocks = [];
    for (let i = 0; i < n; i += safeBlockSize) {
      const chunk = arr.slice(i, i + safeBlockSize);
      chunk.sort((a, b) => a - b);
      blocks.push(chunk);
    }
    
    const results = [];
    
    const lowerBound = (list, val) => {
      let l = 0, r = list.length;
      while (l < r) {
        const mid = (l + r) >>> 1;
        if (list[mid] >= val) r = mid;
        else l = mid + 1;
      }
      return l;
    };
    
    const upperBound = (list, val) => {
      let l = 0, r = list.length;
      while (l < r) {
        const mid = (l + r) >>> 1;
        if (list[mid] > val) r = mid;
        else l = mid + 1;
      }
      return l;
    };

    for (const op of ops) {
      if (op[0] === "SET") {
        const idx = parseInt(op[1], 10);
        const val = parseInt(op[2], 10);
        const oldVal = arr[idx];
        arr[idx] = val;
        
        const bIdx = Math.floor(idx / safeBlockSize);
        const block = blocks[bIdx];
        
        const removePos = lowerBound(block, oldVal);
        block.splice(removePos, 1);
        
        const insertPos = upperBound(block, val);
        block.splice(insertPos, 0, val);
        
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const x = parseInt(op[3], 10);
        const y = parseInt(op[4], 10);
        
        let count = 0;
        const startBlock = Math.floor(l / safeBlockSize);
        const endBlock = Math.floor(r / safeBlockSize);
        
        if (startBlock === endBlock) {
          for (let i = l; i <= r; i++) {
            if (arr[i] >= x && arr[i] <= y) count++;
          }
        } else {
          for (let i = l; i < (startBlock + 1) * safeBlockSize; i++) {
            if (arr[i] >= x && arr[i] <= y) count++;
          }
          for (let i = startBlock + 1; i < endBlock; i++) {
            const b = blocks[i];
            const upper = upperBound(b, y);
            const lower = lowerBound(b, x);
            count += (upper - lower);
          }
          for (let i = endBlock * safeBlockSize; i <= r; i++) {
            if (arr[i] >= x && arr[i] <= y) count++;
          }
        }
        results.push(count);
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
    if (type === "SET") {
      ops.push([type, data[idx++], data[idx++]]);
    } else {
      ops.push([type, data[idx++], data[idx++], data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
