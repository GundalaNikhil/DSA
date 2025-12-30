function compressWithWindow(s, w) {
  if (!s) {
    return "";
  }

  const result = [];
  let i = 0;
  const n = s.length;

  while (i < n) {
    const start = i;
    const char = s[i];

    // Count consecutive occurrences
    while (i < n && s[i] === char) {
      i++;
    }

    const runLength = i - start;

    // Compress if >= threshold
    if (runLength >= w) {
      result.push(char + runLength);
    } else {
      result.push(char.repeat(runLength));
    }
  }

  return result.join("");
}
