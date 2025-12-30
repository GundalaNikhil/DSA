const readline = require("readline");

class Solution {
  shuttleShiftBlackout(arr, k, blackout) {
    const validIndices = [];
    const values = [];
    
    for (let i = 0; i < arr.length; i++) {
      if (!blackout.has(i)) {
        validIndices.push(i);
        values.push(arr[i]);
      }
    }
    
    const count = values.length;
    if (count === 0) return arr;
    
    k = k % count;
    
    // Left rotate
    const rotatedValues = new Array(count);
    for (let i = 0; i < count; i++) {
      rotatedValues[i] = values[(i + k) % count];
    }
    
    for (let i = 0; i < count; i++) {
      arr[validIndices[i]] = rotatedValues[i];
    }
    
    return arr;
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
    
    const k = Number(tokens[ptr++]);
    const b = Number(tokens[ptr++]);
    const blackout = new Set();
    for (let i = 0; i < b; i++) blackout.add(Number(tokens[ptr++]));
    
    const solution = new Solution();
    const result = solution.shuttleShiftBlackout(arr, k, blackout);
    console.log(result.join(" "));
});
