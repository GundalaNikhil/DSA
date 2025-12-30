const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function stablePartition(head, x) {
  const lessHead = new ListNode(0);
  const equalHead = new ListNode(0);
  const greaterHead = new ListNode(0);
  
  let less = lessHead;
  let equal = equalHead;
  let greater = greaterHead;
  
  let curr = head;
  while (curr) {
    if (curr.val < x) {
      less.next = curr;
      less = less.next;
    } else if (curr.val === x) {
      equal.next = curr;
      equal = equal.next;
    } else {
      greater.next = curr;
      greater = greater.next;
    }
    curr = curr.next;
  }
  
  greater.next = null;
  equal.next = greaterHead.next;
  less.next = equalHead.next ? equalHead.next : greaterHead.next;
  
  return lessHead.next;
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
      const x = parseInt(data[idx++], 10);
      let head = stablePartition(dummy.next, x);
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
  }
});
