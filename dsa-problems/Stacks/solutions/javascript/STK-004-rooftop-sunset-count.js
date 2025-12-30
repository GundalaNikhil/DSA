class Solution {
  countVisible(h) {
    let count = 0;
    let maxH = -1;
    
    for (const height of h) {
      if (height > maxH) {
        count++;
        maxH = height;
      }
    }
    return count;
  }
}
