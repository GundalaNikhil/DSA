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

function intersectionSum(headA, headB) {
  let lenA = getLength(headA);
  let lenB = getLength(headB);

  let ptrA = headA;
  let ptrB = headB;

  while (lenA > lenB) {
    ptrA = ptrA.next;
    lenA--;
  }
  while (lenB > lenA) {
    ptrB = ptrB.next;
    lenB--;
  }

  while (ptrA !== ptrB) {
    ptrA = ptrA.next;
    ptrB = ptrB.next;
  }

  if (!ptrA) return 0;

  let sum = 0;
  while (ptrA) {
    sum += ptrA.val;
    ptrA = ptrA.next;
  }
  return sum;
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
  const m = parseInt(data[idx++], 10);
  
  const dummyA = new ListNode(0);
  let curA = dummyA;
  const nodesA = [];
  for (let i = 0; i < n; i++) {
    const node = new ListNode(parseInt(data[idx++], 10));
    curA.next = node;
    curA = curA.next;
    nodesA.push(node);
  }
  
  const dummyB = new ListNode(0);
  let curB = dummyB;
  const nodesB = [];
  for (let i = 0; i < m; i++) {
    const node = new ListNode(parseInt(data[idx++], 10));
    curB.next = node;
    curB = curB.next;
    nodesB.push(node);
  }
  
  const ia = parseInt(data[idx++], 10);
  const ib = parseInt(data[idx++], 10);
  if (ia >= 0 && ib >= 0 && n > 0 && m > 0) {
    nodesB[ib].next = nodesA[ia];
  }

  console.log(intersectionSum(dummyA.next, dummyB.next));
});
