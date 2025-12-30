const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function rotateList(head, len, k) {
  if (len <= 1 || k % len === 0) {
    let tail = head;
    while (tail.next) tail = tail.next;
    return [head, tail];
  }

  k = k % len;
  let moves = len - k;

  let newTail = head;
  for (let i = 0; i < moves - 1; i++) {
    newTail = newTail.next;
  }

  let newHead = newTail.next;
  newTail.next = null;

  let temp = newHead;
  while (temp.next) temp = temp.next;
  temp.next = head;

  return [newHead, newTail];
}

function rotateBlocks(head, b, k) {
  if (!head || b <= 0) return head;

  const dummy = new ListNode(0);
  let prevTail = dummy;
  let curr = head;

  while (curr) {
    let blockHead = curr;
    let blockTail = curr;
    let len = 1;

    for (let i = 0; i < b - 1 && blockTail.next; i++) {
      blockTail = blockTail.next;
      len++;
    }

    let nextBlockHead = blockTail.next;
    blockTail.next = null;

    const [newHead, newTail] = rotateList(blockHead, len, k);

    prevTail.next = newHead;
    prevTail = newTail;

    curr = nextBlockHead;
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
      const b = parseInt(data[idx++], 10);
      const k = parseInt(data[idx++], 10);

      let head = rotateBlocks(dummy.next, b, k);
      const out = [];
      while (head) {
        out.push(head.val);
        head = head.next;
      }
      console.log(out.join(" "));
  }
});
