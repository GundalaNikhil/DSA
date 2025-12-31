const readline = require("readline");

class Solution {
  sortWithFixedOnes(arr) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
      while (left < right && (arr[left] === 0 || arr[left] === 1)) {
        left++;
      }
      while (left < right && (arr[right] === 2 || arr[right] === 1)) {
        right--;
      }

      if (left < right) {
        const temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
      }
    }
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

  const solution = new Solution();
  solution.sortWithFixedOnes(arr);
  console.log(arr.join(" "));
});
