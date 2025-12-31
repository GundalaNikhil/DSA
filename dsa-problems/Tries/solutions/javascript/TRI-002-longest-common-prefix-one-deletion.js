const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = new Map();
    this.wordIds = new Set();
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.longestPrefix = "";
  }

  longestCommonPrefixAfterOneDeletion(words) {
    const n = words.length;

    // Insert all variants into trie
    for (let wordId = 0; wordId < n; wordId++) {
      const word = words[wordId];

      // Insert original word
      this._insertWord(word, wordId);

      // Insert all single-deletion variants
      for (let i = 0; i < word.length; i++) {
        const variant = word.slice(0, i) + word.slice(i + 1);
        this._insertWord(variant, wordId);
      }
    }

    // DFS to find longest prefix with all word IDs
    this._dfs(this.root, "", n);

    return this.longestPrefix;
  }

  _insertWord(word, wordId) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
      node.wordIds.add(wordId);
    }
  }

  _dfs(node, prefix, totalWords) {
    // If all words are represented at this node, update longest prefix
    if (node.wordIds.size === totalWords) {
      if (prefix.length > this.longestPrefix.length) {
        this.longestPrefix = prefix;
      }
    }

    // Continue DFS
    for (const [char, child] of node.children) {
      this._dfs(child, prefix + char, totalWords);
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
  const tokens = lines.join(" ").split(/\s+/);

  const n = parseInt(tokens[0]);
  const words = tokens.slice(1, n + 1);

  const solution = new Solution();
  const result = solution.longestCommonPrefixAfterOneDeletion(words);

  console.log(result);
});
