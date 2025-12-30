class Solution {
  sortWithSwaps(arr, S) {
    const n = arr.length;
    const q0 = [],
      q1 = [],
      q2 = [];
    for (let i = 0; i < n; i++) {
      if (arr[i] === 0) q0.push(i);
      else if (arr[i] === 1) q1.push(i);
      else q2.push(i);
    }

    // Use pointers for queue simulation to avoid O(N) shift
    let p0 = 0,
      p1 = 0,
      p2 = 0;

    const bit = new Int32Array(n + 1);
    const update = (idx, val) => {
      for (; idx <= n; idx += idx & -idx) bit[idx] += val;
    };
    const query = (idx) => {
      let sum = 0;
      for (; idx > 0; idx -= idx & -idx) sum += bit[idx];
      return sum;
    };

    for (let i = 0; i < n; i++) update(i + 1, 1);

    const res = [];

    for (let i = 0; i < n; i++) {
      const idx0 = p0 < q0.length ? q0[p0] : -1;
      const idx1 = p1 < q1.length ? q1[p1] : -1;
      const idx2 = p2 < q2.length ? q2[p2] : -1;

      const cost0 = idx0 !== -1 ? query(idx0) : Infinity;
      const cost1 = idx1 !== -1 ? query(idx1) : Infinity;

      if (cost0 <= S) {
        S -= cost0;
        res.push(0);
        p0++;
        update(idx0 + 1, -1);
      } else if (cost1 <= S) {
        S -= cost1;
        res.push(1);
        p1++;
        update(idx1 + 1, -1);
      } else {
        let minIdx = Infinity;
        if (idx0 !== -1) minIdx = Math.min(minIdx, idx0);
        if (idx1 !== -1) minIdx = Math.min(minIdx, idx1);
        if (idx2 !== -1) minIdx = Math.min(minIdx, idx2);

        if (idx0 !== -1 && minIdx === idx0) {
          res.push(0);
          p0++;
          update(idx0 + 1, -1);
        } else if (idx1 !== -1 && minIdx === idx1) {
          res.push(1);
          p1++;
          update(idx1 + 1, -1);
        } else {
          res.push(2);
          p2++;
          update(idx2 + 1, -1);
        }
      }
    }
    return res;
  }
}
