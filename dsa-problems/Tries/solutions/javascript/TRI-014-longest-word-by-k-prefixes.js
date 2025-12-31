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

  insert(word) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
    }
    node.isEnd = true;
  }

  countPrefixes(word) {
    let node = this.root;
    let count = 0;

    for (let i = 0; i < word.length; i++) {
      node = node.children.get(word[i]);
      if (i < word.length - 1 && node.isEnd) {
        count++;
      }
    }

    return count;
  }

  longestWordWithKPrefixes(words, k) {
    // Build trie
    for (const word of words) {
      this.insert(word);
    }

    let result = "";
    let maxLen = 0;

    // Check each word
    for (const word of words) {
      const prefixCount = this.countPrefixes(word);
      if (prefixCount >= k) {
        if (word.length > maxLen || (word.length === maxLen && word < result)) {
          result = word;
          maxLen = word.length;
        }
      }
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
  const [n, k] = lines[0].split(" ").map(Number);
  const words = [];
  for (let i = 1; i <= n; i++) {
    words.push(lines[i].trim());
  }

  const solution = new Solution();
  const result = solution.longestWordWithKPrefixes(words, k);

  console.log(result);
});
