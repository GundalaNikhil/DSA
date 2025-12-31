class Solution {
  process(ops) {
    const result = [];
    const n = 100005;
    const tree = new Int32Array(4 * n).fill(2147483647); // INT_MAX
    let currentSize = 0;
    const stackVals = [];
    
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
      if (r < start || end < l) return 2147483647;
      if (l <= start && end <= r) return tree[node];
      const mid = Math.floor((start + end) / 2);
      return Math.min(query(2 * node, start, mid, l, r),
                      query(2 * node + 1, mid + 1, end, l, r));
    };
    
    for (const op of ops) {
      const cmd = op[0];
      if (cmd === "PUSH") {
        const val = parseInt(op[1], 10);
        stackVals.push(val);
        update(1, 0, n - 1, currentSize, val);
        currentSize++;
      } else if (cmd === "POP") {
        if (currentSize === 0) {
          result.push("EMPTY");
        } else {
          result.push(stackVals.pop().toString());
          currentSize--;
        }
      } else if (cmd === "MIN") {
        const k = parseInt(op[1], 10);
        if (currentSize < k) {
          result.push("NA");
        } else {
          const minVal = query(1, 0, n - 1, currentSize - k, currentSize - 1);
          result.push(minVal.toString());
        }
      }
    }
    return result;
  }
}
