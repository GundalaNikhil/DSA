const readline = require("readline");

class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEndOfWord = false;
  }
}

class Solution {
  constructor() {
    this.root = new TrieNode();
    this.metadata = new Map(); // word -> {frequency, lastUsed}
  }

  insertWord(word, frequency, timestamp) {
    let node = this.root;
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode());
      }
      node = node.children.get(char);
    }
    node.isEndOfWord = true;
    this.metadata.set(word, { frequency, lastUsed: timestamp });
  }

  autocomplete(prefix, currentTime, D, k) {
    // Navigate to prefix node
    let node = this.root;
    for (const char of prefix) {
      if (!node.children.has(char)) {
        return [];
      }
      node = node.children.get(char);
    }

    // Collect all words with this prefix
    const matches = [];
    this._collectWords(node, prefix, matches);

    // Compute decay scores
    const scores = matches.map((word) => {
      const meta = this.metadata.get(word);
      const decay = Math.exp(-(currentTime - meta.lastUsed) / D);
      const score = meta.frequency * decay;
      return { word, score };
    });

    // Sort by score (desc), then lexicographically (asc)
    scores.sort((a, b) => {
      if (Math.abs(a.score - b.score) > 1e-9) {
        return b.score - a.score;
      }
      return a.word.localeCompare(b.word);
    });

    // Return top k
    return scores.slice(0, k).map((item) => item.word);
  }

  _collectWords(node, prefix, result) {
    if (node.isEndOfWord) {
      result.push(prefix);
    }
    for (const [char, child] of node.children) {
      this._collectWords(child, prefix + char, result);
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
  let idx = 0;

  const n = parseInt(tokens[idx++]);
  const solution = new Solution();

  for (let i = 0; i < n; i++) {
    const word = tokens[idx++];
    const freq = parseInt(tokens[idx++]);
    const time = parseInt(tokens[idx++]);
    solution.insertWord(word, freq, time);
  }

  const prefix = tokens[idx++];
  const currentTime = parseInt(tokens[idx++]);
  const D = parseInt(tokens[idx++]);
  const k = parseInt(tokens[idx++]);

  const result = solution.autocomplete(prefix, currentTime, D, k);
  console.log(JSON.stringify(result));
});
