const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
  }

  insertWord(word) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
    }
    node.isEnd = true;
  }

  search(pattern) {
    return this.dfs(this.root, pattern, 0);
  }

  dfs(node, pattern, index) {
    if (index === pattern.length) {
      return node.isEnd;
    }

    const char = pattern[index];

    if (char === "?") {
      // Match any single character
      for (const child of node.children.values()) {
        if (this.dfs(child, pattern, index + 1)) {
          return true;
        }
      }
      return false;
    } else if (char === "*") {
      // Match zero or more characters
      // Try matching 0 characters
      if (this.dfs(node, pattern, index + 1)) {
        return true;
      }
      // Try matching 1+ characters
      for (const child of node.children.values()) {
        if (this.dfs(child, pattern, index)) {
          return true;
        }
      }
      return false;
    } else {
      // Regular character
      if (!node.children.has(char)) {
        return false;
      }
      return this.dfs(node.children.get(char), pattern, index + 1);
    }
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
  const n = parseInt(lines[0]);

  const solution = new Solution();
  for (let i = 1; i <= n; i++) {
    solution.insertWord(lines[i].trim());
  }

  const pattern = lines[n + 1].trim();
  const result = solution.search(pattern);

  console.log(result ? "true" : "false");
});
