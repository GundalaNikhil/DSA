class Solution {
  maxAreaWithBoost(h, b) {
    const n = h.length;
    const tree = new Int32Array(4 * n);
    
    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = h[start];
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);
        tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
      }
    };
    
    build(1, 0, n - 1);
    
    const findLastLess = (node, start, end, l, r, val) => {
      if (l > r || tree[node] >= val) return -1;
      if (start === end) return start;
      const mid = Math.floor((start + end) / 2);
      let res = -1;
      if (mid < r) res = findLastLess(2 * node + 1, mid + 1, end, l, r, val);
      if (res !== -1) return res;
      if (l <= mid) return findLastLess(2 * node, start, mid, l, r, val);
      return -1;
    };
    
    const findFirstLess = (node, start, end, l, r, val) => {
      if (l > r || tree[node] >= val) return -1;
      if (start === end) return start;
      const mid = Math.floor((start + end) / 2);
      let res = -1;
      if (l <= mid) res = findFirstLess(2 * node, start, mid, l, r, val);
      if (res !== -1) return res;
      if (mid < r) return findFirstLess(2 * node + 1, mid + 1, end, l, r, val);
      return -1;
    };
    
    let maxArea = 0n;
    const bigB = BigInt(b);
    
    for (let i = 0; i < n; i++) {
      const hVal = BigInt(h[i]);
      
      // Case 1
      const boostedH = hVal + bigB;
      const L = findLastLess(1, 0, n - 1, 0, i - 1, Number(boostedH));
      let R = findFirstLess(1, 0, n - 1, i + 1, n - 1, Number(boostedH));
      if (R === -1) R = n;
      const area1 = boostedH * BigInt(R - L - 1);
      if (area1 > maxArea) maxArea = area1;
      
      // Case 2
      const normalH = hVal;
      const L1 = findLastLess(1, 0, n - 1, 0, i - 1, Number(normalH));
      let R1 = findFirstLess(1, 0, n - 1, i + 1, n - 1, Number(normalH));
      if (R1 === -1) R1 = n;
      
      const area2 = normalH * BigInt(R1 - L1 - 1);
      if (area2 > maxArea) maxArea = area2;
      
      if (L1 !== -1 && BigInt(h[L1]) + bigB >= normalH) {
        const L2 = findLastLess(1, 0, n - 1, 0, L1 - 1, Number(normalH));
        const area3 = normalH * BigInt(R1 - L2 - 1);
        if (area3 > maxArea) maxArea = area3;
      }
      
      if (R1 !== n && BigInt(h[R1]) + bigB >= normalH) {
        let R2 = findFirstLess(1, 0, n - 1, R1 + 1, n - 1, Number(normalH));
        if (R2 === -1) R2 = n;
        const area4 = normalH * BigInt(R2 - L1 - 1);
        if (area4 > maxArea) maxArea = area4;
      }
    }
    
    return maxArea;
  }
}
