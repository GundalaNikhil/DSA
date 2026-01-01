class Solution {
  countChanges(s) {
    const stack = [];
    const opens = "([{";
    const closes = ")]}";
    const pairs = { ')': '(', ']': '[', '}': '{' };

    for (const c of s) {
      if (opens.includes(c)) {
        stack.push(c);
      } else if (closes.includes(c)) {
        if (stack.length > 0 && stack[stack.length - 1] === pairs[c]) {
          stack.pop();
        } else {
          stack.push(c);
        }
      } else if (c === '?') {
        stack.push('(');
      }
    }
    return stack.length;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = "";
rl.on("line", (line) => {
  data += line;
});

rl.on("close", () => {
  const s = data.trim();
  if (s.length === 0) {
      console.log(0);
      return;
  }
  const solution = new Solution();
  console.log(solution.countChanges(s));
});
