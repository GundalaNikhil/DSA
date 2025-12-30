class Solution {
  minChanges(arr) {
    const n = arr.length;
    if (n <= 1) return 0;
    
    const evenCounts = new Map();
    const oddCounts = new Map();
    
    for (let i = 0; i < n; i++) {
      if (i % 2 === 0) {
        evenCounts.set(arr[i], (evenCounts.get(arr[i]) || 0) + 1);
      } else {
        oddCounts.set(arr[i], (oddCounts.get(arr[i]) || 0) + 1);
      }
    }
    
    const getTopTwo = (counts) => {
      let firstVal = -1, firstCount = 0;
      let secondVal = -1, secondCount = 0;
      
      for (const [val, count] of counts.entries()) {
        if (count > firstCount) {
          secondCount = firstCount;
          secondVal = firstVal;
          firstCount = count;
          firstVal = val;
        } else if (count > secondCount) {
          secondCount = count;
          secondVal = val;
        }
      }
      return [{val: firstVal, count: firstCount}, {val: secondVal, count: secondCount}];
    };
    
    const [e1, e2] = getTopTwo(evenCounts);
    const [o1, o2] = getTopTwo(oddCounts);
    
    if (e1.val !== o1.val) {
      return n - (e1.count + o1.count);
    } else {
      const opt1 = n - (e1.count + o2.count);
      const opt2 = n - (e2.count + o1.count);
      return Math.min(opt1, opt2);
    }
  }
}
