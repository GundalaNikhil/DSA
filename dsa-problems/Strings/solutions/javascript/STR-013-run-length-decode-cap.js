function decodeWithCap(s, cap) {
  const result = [];
  let i = 0;
  const n = s.length;

  while (i < n) {
    // Read character
    const char = s[i];
    i++;

    // Read count
    let countStr = "";
    while (i < n && /\d/.test(s[i])) {
      countStr += s[i];
      i++;
    }

    // Decode with cap
    const count = countStr ? parseInt(countStr) : 1;
    const actualCount = Math.min(count, cap);

    result.push(char.repeat(actualCount));
  }

  return result.join("");
}
