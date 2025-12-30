const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEnd = false;
    this.count = 0;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.result = "";
    this.remaining = 0;
  }

  insert(word) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
      node.count++;
    }
    node.isEnd = true;
  }

  dfs(node, path) {
    if (node.isEnd) {
      this.remaining--;
      if (this.remaining === 0) {
        this.result = path.join("");
        return true;
      }
    }

    // Sort children for alphabetical order
    const sortedKeys = Array.from(node.children.keys()).sort();

    for (const char of sortedKeys) {
      const child = node.children.get(char);

      if (child.count >= this.remaining) {
        path.push(char);
        if (this.dfs(child, path)) {
          return true;
        }
        path.pop();
      } else {
        this.remaining -= child.count;
      }
    }

    return false;
  }

  kthSmallest(words, k) {
    for (const word of words) {
      this.insert(word);
    }

    this.remaining = k;
    this.dfs(this.root, []);

    return this.result;
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
  const [n, k] = lines[0].split(" ").map(Number);
  const words = [];
  for (let i = 1; i <= n; i++) {
    words.push(lines[i].trim());
  }

  const solution = new Solution();
  const result = solution.kthSmallest(words, k);

  console.log(result);
});
