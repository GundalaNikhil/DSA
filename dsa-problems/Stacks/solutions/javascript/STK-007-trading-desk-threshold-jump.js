class Solution {
  thresholdJump(prices, t) {
    const n = prices.length;
    
    // Coordinate Compression
    const distinct = Array.from(new Set(prices)).sort((a, b) => a - b);
    const rankMap = new Map();
    distinct.forEach((val, idx) => rankMap.set(val, idx));
    const m = distinct.length;
    
    // Segment Tree
    const tree = new Int32Array(4 * m).fill(2e9);
    
    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = val;
        return;
      }
      const mid = Math.floor((start + end) / 2);
      if (idx <= mid) update(2 * node, start, mid, idx, val);
      else update(2 * node + 1, mid + 1, end, idx, val);
      tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
    };
    
    const query = (node, start, end, l, r) => {
      if (r < start || end < l) return 2e9;
      if (l <= start && end <= r) return tree[node];
      const mid = Math.floor((start + end) / 2);
      return Math.min(query(2 * node, start, mid, l, r),
                      query(2 * node + 1, mid + 1, end, l, r));
    };
    
    const result = new Int32Array(n).fill(0);
    
    // Binary Search helper
    const lowerBound = (arr, target) => {
      let l = 0, r = arr.length;
      while (l < r) {
        const mid = Math.floor((l + r) / 2);
        if (arr[mid] < target) l = mid + 1;
        else r = mid;
      }
      return l;
    };
    
    for (let i = n - 1; i >= 0; i--) {
      const target = prices[i] + t;
      const r = lowerBound(distinct, target);
      
      if (r < m) {
        const nearestIdx = query(1, 0, m - 1, r, m - 1);
        if (nearestIdx !== 2e9) {
          result[i] = nearestIdx - i;
        }
      }
      
      update(1, 0, m - 1, rankMap.get(prices[i]), i);
    }
    
    return Array.from(result);
  }
}
