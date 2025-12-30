class Solution {
  smallestRange(lists) {
    const events = [];
    const k = lists.length;
    const required = new Int32Array(k);
    
    for (let i = 0; i < k; i++) {
      if (lists[i].length === 0) return [];
      required[i] = lists[i].length === 1 ? 1 : 2;
      for (const val of lists[i]) {
        events.push({ val, id: i });
      }
    }
    
    events.sort((a, b) => a.val - b.val);
    
    const counts = new Int32Array(k);
    let satisfied = 0;
    let left = 0;
    let minLen = Infinity;
    let res = [];
    
    for (let right = 0; right < events.length; right++) {
      const { val: endVal, id: listId } = events[right];
      counts[listId]++;
      
      if (counts[listId] === required[listId]) {
        satisfied++;
      }
      
      while (satisfied === k) {
        const startVal = events[left].val;
        const len = endVal - startVal;
        
        if (len < minLen) {
          minLen = len;
          res = [startVal, endVal];
        }
        
        const leftListId = events[left].id;
        if (counts[leftListId] === required[leftListId]) {
          satisfied--;
        }
        counts[leftListId]--;
        left++;
      }
    }
    
    return res;
  }
}
