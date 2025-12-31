function countDistinctSubsequencesWithLimit(s, maxFreq, MOD) {
  const encode = (freq) => freq.join(",");
  const decode = (str) => str.split(",").map(Number);

  let dp = new Map();
  dp.set(encode(new Array(26).fill(0)), 1);

  for (let char of s) {
    const charIdx = char.charCodeAt(0) - 97;
    const newDp = new Map();

    for (let [stateStr, count] of dp) {
      const state = decode(stateStr);

      // Don't include
      const key = stateStr;
      newDp.set(key, ((newDp.get(key) || 0) + count) % MOD);

      // Include if allowed
      if (state[charIdx] < maxFreq) {
        state[charIdx]++;
        const newKey = encode(state);
        newDp.set(newKey, ((newDp.get(newKey) || 0) + count) % MOD);
        state[charIdx]--; // Restore
      }
    }

    dp = newDp;
  }

  let total = 0;
  for (let count of dp.values()) {
    total = (total + count) % MOD;
  }
  return total;
}
