const readline = require("readline");

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class Solution {
  constructor() {
    this.root = null;
  }

  insert(node, val) {
    if (!node) return new TreeNode(val);
    if (val < node.val) {
      node.left = this.insert(node.left, val);
    } else {
      node.right = this.insert(node.right, val);
    }
    return node;
  }

  inorder(node, res) {
    if (!node) return;
    this.inorder(node.left, res);
    res.push(node.val);
    this.inorder(node.right, res);
  }

  search(node, x) {
    if (!node) return false;
    if (node.val === x) return true;
    if (x < node.val) return this.search(node.left, x);
    return this.search(node.right, x);
  }

  buildInorder(values) {
    this.root = null;
    for (const v of values) {
      this.root = this.insert(this.root, v);
    }
    const res = [];
    this.inorder(this.root, res);
    return res;
  }

  searchValue(values, x) {
    if (!this.root && values.length > 0) {
      this.buildInorder(values);
    }
    return this.search(this.root, x);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const values = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
  }
  const x = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  const inorder = solution.buildInorder(values);
  console.log(inorder.join(" "));
  console.log(solution.searchValue(values, x) ? "true" : "false");
});
