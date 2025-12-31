const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function groupOddEvenStable(head) {
  const oddDummy = new ListNode(0);
  const evenDummy = new ListNode(0);
  let oddTail = oddDummy;
  let evenTail = evenDummy;

  let curr = head;
  while (curr) {
    if (curr.val % 2 !== 0) {
      oddTail.next = curr;
      oddTail = oddTail.next;
    } else {
      evenTail.next = curr;
      evenTail = evenTail.next;
    }
    curr = curr.next;
  }

  evenTail.next = null;
  oddTail.next = evenDummy.next;

  return oddDummy.next;
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

  let head = groupOddEvenStable(dummy.next);
  const out = [];
  while (head) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
});
