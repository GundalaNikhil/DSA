function minimalDeleteKPeriodic(s, k) {
  const n = s.length;
  let deletions = 0;

  for (let pos = 0; pos < k; pos++) {
    const freq = new Map();

    // Count frequency at positions pos, pos+k, pos+2k, ...
    for (let i = pos; i < n; i += k) {
      const c = s[i];
      freq.set(c, (freq.get(c) || 0) + 1);
    }

    // Keep most frequent, delete others
    if (freq.size > 0) {
      const maxFreq = Math.max(...freq.values());
      const totalAtPos = Array.from(freq.values()).reduce((a, b) => a + b, 0);
      deletions += totalAtPos - maxFreq;
    }
  }

  return deletions;
}
