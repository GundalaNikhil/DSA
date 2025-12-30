function smallestMissingSubstring(s, k) {
  // Extract all k-length substrings
  const substrings = new Set();
  for (let i = 0; i <= s.length - k; i++) {
    substrings.add(s.substring(i, i + k));
  }

  function dfs(current, remaining) {
    if (remaining === 0) {
      return substrings.has(current) ? null : current;
    }

    for (let charCode = 97; charCode <= 122; charCode++) {
      const c = String.fromCharCode(charCode);
      const result = dfs(current + c, remaining - 1);
      if (result !== null) {
        return result;
      }
    }

    return null;
  }

  return dfs("", k) || "";
}
