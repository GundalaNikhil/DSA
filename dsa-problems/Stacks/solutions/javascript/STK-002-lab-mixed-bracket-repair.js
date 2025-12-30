class Solution {
  canRepair(s) {
    const n = s.length;
    if (n % 2 !== 0) return false;
    
    const leftStack = [];
    const starStack = [];
    
    const isMatch = (open, close) => {
      return (open === '(' && close === ')') ||
             (open === '[' && close === ']') ||
             (open === '{' && close === '}');
    };
    
    for (let i = 0; i < n; i++) {
      const c = s[i];
      if (c === '(' || c === '[' || c === '{') {
        leftStack.push(i);
      } else if (c === '?') {
        starStack.push(i);
      } else {
        // Closer
        if (leftStack.length > 0 && isMatch(s[leftStack[leftStack.length - 1]], c)) {
          leftStack.pop();
        } else if (starStack.length > 0) {
          starStack.pop();
        } else {
          return false;
        }
      }
    }
    
    while (leftStack.length > 0) {
      if (starStack.length === 0) return false;
      if (leftStack[leftStack.length - 1] < starStack[starStack.length - 1]) {
        leftStack.pop();
        starStack.pop();
      } else {
        return false;
      }
    }
    
    return starStack.length % 2 === 0;
  }
}
