const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function isPalindrome(vals, left, right) {
  while (left < right) {
    if (vals[left] !== vals[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}

function canBePalindrome(head) {
  const vals = [];
  let curr = head;
  while (curr) {
    vals.push(curr.val);
    curr = curr.next;
  }

  let left = 0;
  let right = vals.length - 1;

  while (left < right) {
    if (vals[left] !== vals[right]) {
      return isPalindrome(vals, left + 1, right) || 
             isPalindrome(vals, left, right - 1);
    }
    left++;
    right--;
  }
  return true;
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

  console.log(canBePalindrome(dummy.next) ? "true" : "false");
});
