class Solution {
  minInversionsAfterSwap(arr) {
    const n = arr.length;
    const sorted = [...new Set(arr)].sort((a, b) => a - b);
    const ranks = new Map();
    sorted.forEach((v, i) => ranks.set(v, i + 1));
    const m = sorted.length;
    
    const bit = new Int32Array(m + 2);
    
    const update = (idx, val) => {
      for (; idx <= m; idx += idx & -idx) bit[idx] += val;
    };
    
    const query = (idx) => {
      let sum = 0;
      for (; idx > 0; idx -= idx & -idx) sum += bit[idx];
      return sum;
    };
    
    let initialInversions = 0n;
    for (let i = n - 1; i >= 0; i--) {
      const rk = ranks.get(arr[i]);
      initialInversions += BigInt(query(rk - 1));
      update(rk, 1);
    }
    
    let maxReduction = 0n;
    for (let i = 0; i < n - 1; i++) {
      if (arr[i] > arr[i+1]) {
        maxReduction = 1n;
        break; // At least one adjacent inversion exists
      }
    }
    
    return initialInversions - maxReduction;
  }
}
