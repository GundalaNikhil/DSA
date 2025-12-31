const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function swapWithSkip(head, K) {
  if (!head || !head.next) return [head, 0];

  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;
  let swapCount = 0;

  while (prev.next && prev.next.next) {
    const first = prev.next;
    const second = prev.next.next;

    const nonNegative = (first.val >= 0 && second.val >= 0);
    const canSwap = (K > 0);

    if (nonNegative && canSwap) {
      prev.next = second;
      first.next = second.next;
      second.next = first;

      K--;
      swapCount++;
      prev = first;
    } else {
      prev = second;
    }
  }

  return [dummy.next, swapCount];
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
      const K = parseInt(data[idx++], 10);
      const result = swapWithSkip(dummy.next, K);
      let head = result[0];
      const swaps = result[1];
      
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
      console.log(swaps);
  }
});
