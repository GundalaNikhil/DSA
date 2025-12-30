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

  hasEditDistance1(query) {
    return this.dfs(this.root, query, 0, 0);
  }

  dfs(node, query, index, edits) {
    if (edits > 1) {
      return false;
    }

    if (index === query.length) {
      if (node.isEnd && edits === 1) {
        return true;
      }
      if (edits === 0) {
        for (const child of node.children.values()) {
          if (child.isEnd) {
            return true;
          }
        }
      }
      return false;
    }

    const char = query[index];

    // Match without edit
    if (node.children.has(char)) {
      if (this.dfs(node.children.get(char), query, index + 1, edits)) {
        return true;
      }
    }

    if (edits < 1) {
      // Substitution
      for (const [ch, child] of node.children) {
        if (ch !== char) {
          if (this.dfs(child, query, index + 1, edits + 1)) {
            return true;
          }
        }
      }

      // Deletion from query
      if (this.dfs(node, query, index + 1, edits + 1)) {
        return true;
      }

      // Insertion into query
      for (const child of node.children.values()) {
        if (this.dfs(child, query, index, edits + 1)) {
          return true;
        }
      }
    }

    return false;
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

  const query = lines[n + 1].trim();
  const result = solution.hasEditDistance1(query);

  console.log(result ? "true" : "false");
});
