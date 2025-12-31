const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = new Map();
    this.count = 0;
    this.isEnd = false;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
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

  findMinLength(word) {
    let node = this.root;
    for (let i = 0; i < word.length; i++) {
      node = node.children.get(word[i]);
      if (node.count === 1) {
        return i + 1;
      }
    }
    return word.length;
  }

  findMinimumPrefixLengths(words) {
    // Build trie with counts
    for (const word of words) {
      this.insert(word);
    }

    // Find minimum prefix length for each word
    const result = [];
    for (const word of words) {
      result.push(this.findMinLength(word));
    }

    return result;
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
  const result = solution.findMinimumPrefixLengths(words);

  console.log("[" + result.join(",") + "]");
});
