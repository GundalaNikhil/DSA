const readline = require("readline");

const ROW1 = new Set("qwertyuiop".split(""));
const ROW2 = new Set("asdfghjkl".split(""));
const LEFT = new Set("qwertasdfgzxcvb".split(""));

function row(c) {
  if (ROW1.has(c)) return 1;
  if (ROW2.has(c)) return 2;
  return 3;
}

function hand(c) {
  return LEFT.has(c) ? 0 : 1;
}

function repCost(x, y) {
  if (x === y) return 0;
  if (row(x) === row(y)) return 1;
  return hand(x) === hand(y) ? 2 : 3;
}

class Solution {
  minKeyboardEditCost(a, b) {
    const n = a.length, m = b.length;
    let prev = new Array(m + 1);
    let cur = new Array(m + 1);
    for (let j = 0; j <= m; j++) prev[j] = j;

    for (let i = 1; i <= n; i++) {
      cur[0] = i;
      const ca = a[i - 1];
      for (let j = 1; j <= m; j++) {
        const cb = b[j - 1];
        const del = prev[j] + 1;
        const ins = cur[j - 1] + 1;
        const rep = prev[j - 1] + repCost(ca, cb);
        cur[j] = Math.min(del, ins, rep);
      }
      const tmp = prev; prev = cur; cur = tmp;
    }
    return prev[m];
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line));
rl.on("close", () => {
  const a = (lines[0] ?? "").trim();
  const b = (lines[1] ?? "").trim();
  const sol = new Solution();
  console.log(sol.minKeyboardEditCost(a, b));
});
