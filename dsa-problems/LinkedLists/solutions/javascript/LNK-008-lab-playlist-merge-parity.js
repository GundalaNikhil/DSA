const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function mergeByParity(l1, l2) {
  const evenDummy = new ListNode(0);
  const oddDummy = new ListNode(0);
  let evenTail = evenDummy;
  let oddTail = oddDummy;

  let curr = l1;
  while (curr) {
    if (curr.val % 2 === 0) {
      evenTail.next = curr;
      evenTail = evenTail.next;
    } else {
      oddTail.next = curr;
      oddTail = oddTail.next;
    }
    curr = curr.next;
  }

  curr = l2;
  while (curr) {
    if (curr.val % 2 === 0) {
      evenTail.next = curr;
      evenTail = evenTail.next;
    } else {
      oddTail.next = curr;
      oddTail = oddTail.next;
    }
    curr = curr.next;
  }

  oddTail.next = null;
  evenTail.next = oddDummy.next;

  return evenDummy.next;
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
  
  const d1 = new ListNode(0);
  let c1 = d1;
  for (let i = 0; i < n; i++) {
    c1.next = new ListNode(parseInt(data[idx++], 10));
    c1 = c1.next;
  }
  
  const m = parseInt(data[idx++], 10);
  const d2 = new ListNode(0);
  let c2 = d2;
  for (let i = 0; i < m; i++) {
    c2.next = new ListNode(parseInt(data[idx++], 10));
    c2 = c2.next;
  }

  let head = mergeByParity(d1.next, d2.next);
  const out = [];
  while (head) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
});
