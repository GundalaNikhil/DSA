class TrieNode {
  constructor() {
    this.children = new Map();
    this.word = null;
    this.rarity = Infinity;
  }
}

class Solution {
  replaceWords(dictionary, sentence) {
    const root = new TrieNode();

    // Build trie
    for (const [word, rarity] of Object.entries(dictionary)) {
      this.insert(root, word, rarity);
    }

    // Process sentence
    const words = sentence.split(" ");
    const result = words.map((word) => this.findReplacement(root, word));

    return result.join(" ");
  }

  insert(root, word, rarity) {
    let curr = root;

    for (const char of word) {
      if (!curr.children.has(char)) {
        curr.children.set(char, new TrieNode());
      }
      curr = curr.children.get(char);
    }

    if (
      rarity < curr.rarity ||
      (rarity === curr.rarity &&
        (curr.word === null || word.length < curr.word.length))
    ) {
      curr.word = word;
      curr.rarity = rarity;
    }
  }

  findReplacement(root, word) {
    let curr = root;
    let best = null;
    let bestRarity = Infinity;

    for (const char of word) {
      if (!curr.children.has(char)) break;

      curr = curr.children.get(char);

      if (curr.word !== null) {
        if (
          curr.rarity < bestRarity ||
          (curr.rarity === bestRarity && curr.word.length < best.length)
        ) {
          best = curr.word;
          bestRarity = curr.rarity;
        }
      }
    }

    return best !== null ? best : word;
  }
}

// Time: O(M×K + N×L), Space: O(M×K)
