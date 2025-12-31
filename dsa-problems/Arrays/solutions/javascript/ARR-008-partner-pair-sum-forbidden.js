const readline = require("readline");

class Solution {
  hasPairWithForbidden(arr, target, forbidden) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
      if (forbidden.has(left)) {
        left++;
        continue;
      }
      if (forbidden.has(right)) {
        right--;
        continue;
      }

      const sum = arr[left] + arr[right];

      if (sum === target) {
        return true;
      } else if (sum < target) {
        left++;
      } else {
        right--;
      }
    }

    return false;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(Number(tokens[ptr++]));

  const target = Number(tokens[ptr++]);
  const f = Number(tokens[ptr++]);
  const forbidden = new Set();
  for (let i = 0; i < f; i++) forbidden.add(Number(tokens[ptr++]));

  const solution = new Solution();
  console.log(
    solution.hasPairWithForbidden(arr, target, forbidden) ? "true" : "false"
  );
});
