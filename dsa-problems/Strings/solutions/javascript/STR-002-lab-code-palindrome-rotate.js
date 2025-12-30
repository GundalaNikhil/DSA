function canRotateToPalindrome(s) {
  if (!s || s.length <= 1) return true;

  // Count character frequencies
  const freq = new Map();
  for (let c of s) {
    freq.set(c, (freq.get(c) || 0) + 1);
  }

  // Count characters with odd frequency
  let oddCount = 0;
  for (let count of freq.values()) {
    if (count % 2 === 1) {
      oddCount++;
    }
  }

  return oddCount <= 1;
}
