const readline = require("readline");

class Solution {
  benchFlipLockedEnds(arr) {
    const n = arr.length;
    if (n < 3) return;
    
    let left = 1;
    let right = n - 2;
    
    while (left < right) {
      // Swap elements
      let temp = arr[left];
      arr[left] = arr[right];
      arr[right] = temp;
      
      left++;
      right--;
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
    for (let i = 0; i < n; i++) {
        arr.push(Number(tokens[ptr++]));
    }
    
    const solution = new Solution();
    solution.benchFlipLockedEnds(arr);
    console.log(arr.join(" "));
});
