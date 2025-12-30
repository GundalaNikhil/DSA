const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function findFirstIndex(head, target) {
  let current = head;
  let index = 0;
  while (current !== null) {
    if (current.val === target) {
      return index;
    }
    current = current.next;
    index++;
  }
  return -1;
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
  
  if (idx < data.length) {
      const target = parseInt(data[idx++], 10);
      console.log(findFirstIndex(dummy.next, target));
  }
});
