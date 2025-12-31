const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = [null, null];
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.MAX_BITS = 30;
  }

  insert(num) {
    let node = this.root;
    for (let i = this.MAX_BITS; i >= 0; i--) {
      const bit = (num >> i) & 1;
      if (node.children[bit] === null) {
        node.children[bit] = new TrieNode();
      }
      node = node.children[bit];
    }
  }

  query(num) {
    let node = this.root;
    let result = 0;

    for (let i = this.MAX_BITS; i >= 0; i--) {
      const bit = (num >> i) & 1;

      if (node.children[bit] !== null) {
        node = node.children[bit];
      } else {
        result |= 1 << i;
        node = node.children[1 - bit];
      }
    }

    return result;
  }

  minimizeXOR(a, X) {
    const n = a.length;
    const prefix = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
      prefix[i + 1] = prefix[i] ^ a[i];
    }

    let minXor = Infinity;

    for (let j = 0; j <= n; j++) {
      if (this.root.children[0] !== null || this.root.children[1] !== null) {
        const target = prefix[j] ^ X;
        const closest = this.query(target);
        minXor = Math.min(minXor, closest ^ target);
      }
      this.insert(prefix[j]);
    }

    return minXor;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [n, X] = lines[0].split(" ").map(Number);
  const a = lines[1].split(" ").map(Number);

  const solution = new Solution();
  const result = solution.minimizeXOR(a, X);

  console.log(result);
});
