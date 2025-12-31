const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = new Map();
    this.suffixCount = 0; // Number of suffixes passing through this node
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.maxLength = 0;
  }

  insertSuffix(suffix) {
    let node = this.root;
    for (const char of suffix) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
      node.suffixCount++; // Increment count for each suffix passing through
    }
  }

  dfs(node, depth) {
    // A repeated substring exists if 2+ suffixes pass through this node
    if (node.suffixCount >= 2 && depth > 0) {
      this.maxLength = Math.max(this.maxLength, depth);
    }

    for (const child of node.children.values()) {
      this.dfs(child, depth + 1);
    }
  }

  longestRepeatedSubstring(s) {
    for (let i = 0; i < s.length; i++) {
      this.insertSuffix(s.substring(i));
    }

    this.dfs(this.root, 0);
    return this.maxLength;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = "";
rl.on("line", (line) => {
  input = line.trim();
  rl.close();
}).on("close", () => {
  const solution = new Solution();
  const result = solution.longestRepeatedSubstring(input);
  console.log(result);
});
