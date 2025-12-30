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
    this.nodeCount = 1; // Start with root
  }

  insert(word) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
        this.nodeCount++;
      }
      node = node.children.get(char);
    }
    node.isEnd = true;
  }

  countTrieNodes(words) {
    for (const word of words) {
      this.insert(word);
    }
    return this.nodeCount;
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
  const words = [];
  for (let i = 1; i <= n; i++) {
    words.push(lines[i].trim());
  }

  const solution = new Solution();
  const result = solution.countTrieNodes(words);

  console.log(result);
});
