const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function reverseFromOffset(head, k, s) {
  if (!head || k < 1) return [head, 0, 0];

  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;

  // Move to s-1
  for (let i = 0; i < s - 1; i++) {
    if (!prev.next) return [head, 0, 0];
    prev = prev.next;
  }

  let groups = 0;
  let totalSum = 0;

  while (true) {
    // Probe
    let probe = prev;
    for (let i = 0; i < k; i++) {
      probe = probe.next;
      if (!probe) return [dummy.next, groups, totalSum];
    }

    // Reverse
    let tail = prev.next;
    let curr = tail.next;
    let groupSum = tail.val;

    for (let i = 1; i < k; i++) {
      groupSum += curr.val;
      let temp = curr.next;
      curr.next = prev.next;
      prev.next = curr;
      tail.next = temp;
      curr = temp;
    }

    groups++;
    totalSum += groupSum;
    prev = tail;
  }
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
      const k = parseInt(data[idx++], 10);
      const s = parseInt(data[idx++], 10);

      const result = reverseFromOffset(dummy.next, k, s);
      let head = result[0];
      const groups = result[1];
      const sum = result[2];
      
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
      console.log(groups);
      console.log(sum);
  }
});
