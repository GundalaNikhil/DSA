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

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const k = parseInt(data[idx++], 10);
const lists = [];
for (let i = 0; i < k; i++) {
  const m = parseInt(data[idx++], 10);
  const list = [];
  for (let j = 0; j < m; j++) {
    list.push(parseInt(data[idx++], 10));
  }
  lists.push(list);
}
const solution = new Solution();
const result = solution.smallestRange(lists);
if (!result || result.length === 0) {
  console.log("NONE");
} else {
  console.log(result[0] + " " + result[1]);
}
