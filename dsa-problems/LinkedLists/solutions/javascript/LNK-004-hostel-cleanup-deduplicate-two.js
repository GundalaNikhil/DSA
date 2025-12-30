const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function deduplicateAtMostTwo(head) {
  if (!head || !head.next) return head;

  let prev = head;
  let current = head.next;
  let count = 1;

  while (current !== null) {
    if (current.val === prev.val) {
      count++;
      if (count > 2) {
        // Remove current
        prev.next = current.next;
        current = current.next;
      } else {
        prev = current;
        current = current.next;
      }
    } else {
      count = 1;
      prev = current;
      current = current.next;
    }
  }
  return head;
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

  let head = deduplicateAtMostTwo(dummy.next);
  const out = [];
  while (head) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
});
