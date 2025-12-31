const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function alternatingReverse(head, l, k) {
  if (!head || k <= 1) return head;

  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;

  // Move to l-1
  for (let i = 0; i < l - 1; i++) {
    if (!prev.next) return head;
    prev = prev.next;
  }

  let reverse = true;
  while (prev.next) {
    if (reverse) {
      let tail = prev.next;
      let curr = tail.next;
      let count = 1;
      while (curr && count < k) {
        let temp = curr.next;
        curr.next = prev.next;
        prev.next = curr;
        tail.next = temp;
        curr = temp;
        count++;
      }
      prev = tail;
    } else {
      let count = 0;
      while (prev.next && count < k) {
        prev = prev.next;
        count++;
      }
    }
    reverse = !reverse;
  }
  return dummy.next;
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
      const l = parseInt(data[idx++], 10);
      const k = parseInt(data[idx++], 10);

      let head = alternatingReverse(dummy.next, l, k);
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
  }
});
