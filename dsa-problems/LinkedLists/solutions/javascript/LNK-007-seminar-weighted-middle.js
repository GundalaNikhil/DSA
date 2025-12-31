const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function weightedMiddleValue(head) {
  if (!head) return 0;

  // Pass 1: Total weight
  let totalWeight = 0;
  let curr = head;
  while (curr) {
    totalWeight += curr.val;
    curr = curr.next;
  }

  const threshold = Math.floor((totalWeight + 1) / 2);

  // Pass 2: Find node
  let currentSum = 0;
  curr = head;
  while (curr) {
    currentSum += curr.val;
    if (currentSum >= threshold) {
      return curr.val;
    }
    curr = curr.next;
  }
  return 0;
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  
  const dummy = new ListNode(0);
  let cur = dummy;
  for (let i = 0; i < n; i++) {
    cur.next = new ListNode(parseInt(data[idx++], 10));
    cur = cur.next;
  }

  console.log(weightedMiddleValue(dummy.next));
});
