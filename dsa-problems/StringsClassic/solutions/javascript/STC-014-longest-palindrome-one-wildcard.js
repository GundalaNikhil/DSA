const readline = require("readline");

class Solution {
  longestWildcardPalindrome(s) {
    const n = s.length;
    if (n === 0) return 0;

    let maxLen = 1;

    // Expand around each center (character and between characters)
    // 2*n - 1 centers
    for (let i = 0; i < 2 * n - 1; i++) {
      let l = Math.floor(i / 2);
      let r = Math.floor((i + 1) / 2);

      let tempMismatch = 0;

      while (l >= 0 && r < n) {
        if (s[l] !== s[r]) {
          tempMismatch++;
        }

        if (tempMismatch > 1) {
          break;
        }

        const length = r - l + 1;
        if (length > maxLen) {
          maxLen = length;
        }

        l--;
        r++;
      }
    }

    return maxLen;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  console.log(solution.longestWildcardPalindrome(s));
});
