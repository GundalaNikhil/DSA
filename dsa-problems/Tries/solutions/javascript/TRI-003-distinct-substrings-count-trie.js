class TrieNode {
  constructor() {
    this.children = new Map();
  }
}

class Solution {
  countDistinctSubstrings(s) {
    if (!s || s.length === 0) return 0;

    const root = new TrieNode();
    let nodeCount = 0;
    const n = s.length;

    // Insert all suffixes
    for (let i = 0; i < n; i++) {
      let curr = root;

      for (let j = i; j < n; j++) {
        const char = s[j];

        if (!curr.children.has(char)) {
          curr.children.set(char, new TrieNode());
          nodeCount++; // New distinct substring
        }

        curr = curr.children.get(char);
      }
    }

    return nodeCount;
  }
}

// Time: O(n²), Space: O(n²)
