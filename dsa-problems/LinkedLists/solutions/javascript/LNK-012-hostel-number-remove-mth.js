const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function removeMth(head, M) {
  if (M <= 0) return head;

  const dummy = new ListNode(0);
  dummy.next = head;
  let curr = dummy;

  for (let i = 0; i < M - 1; i++) {
    if (!curr) return head;
    curr = curr.next;
  }

  if (curr && curr.next) {
    curr.next = curr.next.next;
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
      const M = parseInt(data[idx++], 10);
      let head = removeMth(dummy.next, M);
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
  }
});
