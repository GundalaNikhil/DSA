const readline = require("readline");

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Solution {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  pushBack(value) {
    const newNode = new ListNode(value);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  toArray() {
    const result = [];
    let current = this.head;
    while (current) {
      result.push(current.val);
      current = current.next;
    }
    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  if (lines.length === 0) return;
  const n = parseInt(lines[0], 10);
  const sol = new Solution();
  for (let i = 1; i <= n; i++) {
    const line = lines[i];
    if (line.startsWith("push_back")) {
      const parts = line.split(" ");
      sol.pushBack(parseInt(parts[1], 10));
    } else {
      const arr = sol.toArray();
      console.log(arr.join(" "));
    }
  }
});
