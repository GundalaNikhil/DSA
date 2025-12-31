const readline = require("readline");

class Solution {
  swapAdjacent2BitBlocks(x) {
    // JS bitwise operators work on 32-bit signed ints
    // Use >>> for unsigned shift
    const evenMask = 0x33333333;
    const oddMask = 0xCCCCCCCC; // This will be negative in signed 32-bit context
    
    // x & oddMask might fail if oddMask reads as negative? 
    // JS treats constants as double until bitwise op.
    // 0xCCCCCCCC is 3435973836 (unsigned) or -858993460 (signed).
    // It works correctly for bitwise AND.
    
    const evenBlocks = x & evenMask;
    const oddBlocks = x & oddMask; // Will preserve bits
    
    // Note: oddBlocks is signed. >>> 2 treats it as unsigned.
    const res = (evenBlocks << 2) | (oddBlocks >>> 2);
    
    // Ensure result is unsigned 32-bit
    return (res >>> 0).toString();
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
    
    const x = Number(tokens[0]);
    
    const solution = new Solution();
    console.log(solution.swapAdjacent2BitBlocks(x));
});
