const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function cycleInfo(head) {
  if (!head) return [-1, 0, 0];

  let slow = head;
  let fast = head;
  let hasCycle = false;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      hasCycle = true;
      break;
    }
  }

  if (!hasCycle) return [-1, 0, 0];

  let entry = head;
  let entryIndex = 0;
  while (entry !== slow) {
    entry = entry.next;
    slow = slow.next;
    entryIndex++;
  }

  let length = 0;
  let maxVal = -Infinity;
  let curr = entry;
  do {
    length++;
    maxVal = Math.max(maxVal, curr.val);
    curr = curr.next;
  } while (curr !== entry);

  return [entryIndex, length, maxVal];
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
  const nodes = [];
  for (let i = 0; i < n; i++) {
    const node = new ListNode(parseInt(data[idx++], 10));
    cur.next = node;
    cur = cur.next;
    nodes.push(node);
  }
  
  if (idx < data.length) {
      const pos = parseInt(data[idx++], 10);
      if (pos >= 0 && n > 0) {
        cur.next = nodes[pos];
      }
      
      const res = cycleInfo(dummy.next);
      console.log(res.join(" "));
  }
});
