class TrieNode {
  constructor() {
    this.children = new Map();
    this.isEnd = false;
  }
}

class Solution {
  kthMissingString(inserted, L, k) {
    const root = new TrieNode();

    // Build trie
    for (const word of inserted) {
      this.insert(root, word);
    }

    // DFS
    const kRef = { value: k };
    return this.dfs(root, 0, L, kRef, "") || "";
  }

  insert(root, word) {
    let curr = root;
    for (const char of word) {
      if (!curr.children.has(char)) {
        curr.children.set(char, new TrieNode());
      }
      curr = curr.children.get(char);
    }
    curr.isEnd = true;
  }

  dfs(node, depth, L, kRef, current) {
    if (depth > L) return null;

    for (let i = 0; i < 26; i++) {
      const c = String.fromCharCode(97 + i); // 'a' to 'z'
      const child = node.children.get(c);

      if (depth < L && (!child || !child.isEnd)) {
        if (kRef.value === 1) {
          return current + c;
        }
        kRef.value--;
      }

      if (child && depth < L) {
        const result = this.dfs(child, depth + 1, L, kRef, current + c);
        if (result) return result;
      }
    }

    return null;
  }
}

// Time: O(26×L×k), Space: O(n×avgLen)
