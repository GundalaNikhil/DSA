function normalizeBadge(s) {
  if (!s) return "";

  let result = [];
  let lastWasAlnum = false;

  for (let c of s) {
    if (/[a-zA-Z0-9]/.test(c)) {
      result.push(c.toLowerCase());
      lastWasAlnum = true;
    } else {
      // Non-alphanumeric character
      if (lastWasAlnum && result.length > 0) {
        result.push("-");
        lastWasAlnum = false;
      }
    }
  }

  // Remove trailing hyphen if present
  if (result.length > 0 && result[result.length - 1] === "-") {
    result.pop();
  }

  return result.join("");
}



























const fs = require('fs');
const s = fs.readFileSync(0, 'utf-8').trim();
console.log(normalizeBadge(s));
