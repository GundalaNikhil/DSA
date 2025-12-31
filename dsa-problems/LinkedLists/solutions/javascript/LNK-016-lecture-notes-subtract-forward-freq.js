const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function getLength(head) {
  let len = 0;
  while (head) {
    len++;
    head = head.next;
  }
  return len;
}

function subtractWithFreq(a, b) {
  let lenA = getLength(a);
  let lenB = getLength(b);
  let large = a, small = b;

  if (lenA < lenB) {
    large = b; small = a;
  } else if (lenA === lenB) {
    let currA = a, currB = b;
    while (currA && currA.val === currB.val) {
      currA = currA.next;
      currB = currB.next;
    }
    if (!currA) return [0, new ListNode(0), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]];
    if (currA.val < currB.val) {
      large = b; small = a;
    }
  }

  const s1 = [];
  const s2 = [];
  let curr = large;
  while (curr) { s1.push(curr.val); curr = curr.next; }
  curr = small;
  while (curr) { s2.push(curr.val); curr = curr.next; }

  let head = null;
  let borrow = 0;

  while (s1.length > 0) {
    let v1 = s1.pop();
    let v2 = s2.length > 0 ? s2.pop() : 0;

    let diff = v1 - v2 - borrow;
    if (diff < 0) {
      diff += 10;
      borrow = 1;
    } else {
      borrow = 0;
    }

    let node = new ListNode(diff);
    node.next = head;
    head = node;
  }

  while (head && head.val === 0 && head.next) {
    head = head.next;
  }

  const freq = Array(10).fill(0);
  curr = head;
  while (curr) {
    freq[curr.val]++;
    curr = curr.next;
  }

  return [1, head, freq];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const p of parts) {
    if (p !== "") data.push(p);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  
  const dummyA = new ListNode(0);
  let curA = dummyA;
  for (let i = 0; i < n; i++) {
    curA.next = new ListNode(parseInt(data[idx++], 10));
    curA = curA.next;
  }
  
  const m = parseInt(data[idx++], 10);
  const dummyB = new ListNode(0);
  let curB = dummyB;
  for (let i = 0; i < m; i++) {
    curB.next = new ListNode(parseInt(data[idx++], 10));
    curB = curB.next;
  }

  const result = subtractWithFreq(dummyA.next, dummyB.next);
  console.log(result[0]);
  
  let head = result[1];
  const out = [];
  while (head) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
  console.log(result[2].join(" "));
});
