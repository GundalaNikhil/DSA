function longestChunkedDecomposition(s, L) {
  const n = s.length;
  let left = 0,
    right = n - 1;
  let chunks = 0;

  while (left < right) {
    let matched = false;
    const maxLen = Math.min(L, Math.floor((right - left + 1) / 2));

    for (let len = 1; len <= maxLen; len++) {
      const leftChunk = s.slice(left, left + len);
      const rightChunk = s.slice(right - len + 1, right + 1);

      if (leftChunk === rightChunk) {
        chunks += 2;
        left += len;
        right -= len;
        matched = true;
        break;
      }
    }

    if (!matched) {
      break;
    }
  }

  // Add middle chunk if exists
  if (left <= right) {
    chunks++;
  }

  return chunks;
}
