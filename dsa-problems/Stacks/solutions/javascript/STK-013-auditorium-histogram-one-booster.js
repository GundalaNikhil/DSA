class Solution {
  build(node, start, end) {
    if (start === end) {
      this.tree[node] = this.h[start];
    } else {
      const mid = Math.floor((start + end) / 2);
      this.build(2 * node, start, mid);
      this.build(2 * node + 1, mid + 1, end);
      this.tree[node] = Math.min(this.tree[2 * node], this.tree[2 * node + 1]);
    }
  }

  findLastLess(node, start, end, l, r, val) {
    if (l > r || this.tree[node] >= val) {
      return -1;
    }
    if (start === end) {
      return start;
    }
    const mid = Math.floor((start + end) / 2);
    let res = -1;
    if (mid < r) {
      res = this.findLastLess(2 * node + 1, mid + 1, end, l, r, val);
    }
    if (res !== -1) return res;
    if (l <= mid) {
      return this.findLastLess(2 * node, start, mid, l, r, val);
    }
    return -1;
  }

  findFirstLess(node, start, end, l, r, val) {
    if (l > r || this.tree[node] >= val) {
      return -1;
    }
    if (start === end) {
      return start;
    }
    const mid = Math.floor((start + end) / 2);
    let res = -1;
    if (l <= mid) {
      res = this.findFirstLess(2 * node, start, mid, l, r, val);
    }
    if (res !== -1) return res;
    if (mid < r) {
      return this.findFirstLess(2 * node + 1, mid + 1, end, l, r, val);
    }
    return -1;
  }

  maxAreaWithBoost(h, b) {
    this.h = h;
    const n = h.length;
    this.tree = new Int32Array(4 * n);
    this.build(1, 0, n - 1);
    
    let maxArea = BigInt(0);
    const bBig = BigInt(b);
    
    for (let i = 0; i < n; i++) {
        // Case 1
        const boostedH = BigInt(h[i]) + bBig;
        // Search using Number value (Logic assumes h[i] fits in SMI, or works with comparison)
        // tree uses JS numbers.
        // If boostedH exceeds SMI, passed as Number might lose precision if HUGE. 
        // But logic uses tree[node] < val. 
        const searchValBoost = Number(boostedH); 
        
        const L = this.findLastLess(1, 0, n - 1, 0, i - 1, searchValBoost);
        let R = this.findFirstLess(1, 0, n - 1, i + 1, n - 1, searchValBoost);
        if (R === -1) R = n;
        
        let width = BigInt(R - L - 1);
        let area = boostedH * width;
        if (area > maxArea) maxArea = area;
        
        // Case 2
        const normalH = BigInt(h[i]);
        const searchValNormal = h[i];
        
        const L1 = this.findLastLess(1, 0, n - 1, 0, i - 1, searchValNormal);
        let R1 = this.findFirstLess(1, 0, n - 1, i + 1, n - 1, searchValNormal);
        if (R1 === -1) R1 = n;
        
        width = BigInt(R1 - L1 - 1);
        area = normalH * width;
        if (area > maxArea) maxArea = area;
        
        if (L1 !== -1 && BigInt(h[L1]) + bBig >= normalH) {
            const L2 = this.findLastLess(1, 0, n - 1, 0, L1 - 1, searchValNormal);
            width = BigInt(R1 - L2 - 1);
            area = normalH * width;
            if (area > maxArea) maxArea = area;
        }
        
        if (R1 !== n && BigInt(h[R1]) + bBig >= normalH) {
             let R2 = this.findFirstLess(1, 0, n - 1, R1 + 1, n - 1, searchValNormal);
             if (R2 === -1) R2 = n;
             width = BigInt(R2 - L1 - 1);
             area = normalH * width;
             if (area > maxArea) maxArea = area;
        }
    }
    return maxArea.toString();
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
  const h = [];
  for (let i = 0; i < n; i++) {
    h.push(parseInt(data[idx++], 10));
  }
  const b = parseInt(data[idx++], 10);
  
  const solution = new Solution();
  console.log(solution.maxAreaWithBoost(h, b));
});
