const readline = require("readline");

class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class Solution {
  insert(node, val) {
    if (!node) return new TreeNode(val);
    if (val < node.val) {
      node.left = this.insert(node.left, val);
    } else {
      node.right = this.insert(node.right, val);
    }
    return node;
  }

  kthInRange(values, L, R, k) {
    let root = null;
    for (const v of values) {
      root = this.insert(root, v);
    }

    let count = 0;
    let result = -1;
    const lVal = BigInt(L);
    const rVal = BigInt(R);

    const inorder = (node) => {
      if (!node || result !== -1) return;

      const val = BigInt(node.val);

      if (val > lVal) {
        inorder(node.left);
      }

      if (result !== -1) return;

      if (val >= lVal && val <= rVal) {
        count++;
        if (count === k) {
          result = node.val;
          return;
        }
      }

      if (val < rVal) {
        inorder(node.right);
      }
    };

    inorder(root);
    return result;
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
  for (let i = 0; i < n; i++) values[i] = parseInt(data[idx++], 10);
  const L = parseInt(data[idx++], 10);
  const R = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);

  const solution = new Solution();
  console.log(solution.kthInRange(values, L, R, k).toString());
});
