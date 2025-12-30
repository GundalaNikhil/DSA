class TrieNode {
  constructor() {
    this.children = [null, null];
  }
}

class Solution {
  static MAX_BITS = 30;

  minXORPairUnderLimit(arr, L) {
    if (!arr || arr.length < 2) return -1;

    this.root = new TrieNode();
    let minXOR = Infinity;

    for (const num of arr) {
      if (this.root.children[0] || this.root.children[1]) {
        const closest = this.findClosest(num);
        const xorVal = num ^ closest;
        if (xorVal <= L) {
          minXOR = Math.min(minXOR, xorVal);
        }
      }
      this.insert(num);
    }

    return minXOR === Infinity ? -1 : minXOR;
  }

  insert(num) {
    let curr = this.root;
    for (let i = Solution.MAX_BITS; i >= 0; i--) {
      const bit = (num >> i) & 1;
      if (!curr.children[bit]) {
        curr.children[bit] = new TrieNode();
      }
      curr = curr.children[bit];
    }
  }

  findClosest(num) {
    let curr = this.root;
    let result = 0;

    for (let i = Solution.MAX_BITS; i >= 0; i--) {
      let bit = (num >> i) & 1;

      if (curr.children[bit]) {
        curr = curr.children[bit];
      } else {
        bit = 1 - bit;
        curr = curr.children[bit];
      }

      result |= bit << i;
    }

    return result;
  }
}

// Time: O(n × 30), Space: O(n × 30)
