class Solution {
  reduce(s, w) {
    const stack = []; // Array of objects {c, w}
    let totalRemoved = 0; // Use number, safe up to 2^53. Max weight sum ~ 200000 * 1000 = 2*10^8. Safe.
    
    for (let i = 0; i < s.length; i++) {
      const currentChar = s[i];
      const currentWeight = w[i];
      
      if (stack.length > 0) {
        const top = stack[stack.length - 1];
        if (top.c === currentChar && (top.w + currentWeight) % 2 === 0) {
          totalRemoved += top.w + currentWeight;
          stack.pop();
          continue;
        }
      }
      stack.push({c: currentChar, w: currentWeight});
    }
    
    const reducedS = stack.map(item => item.c).join("");
    return [reducedS, totalRemoved.toString()];
  }
}
