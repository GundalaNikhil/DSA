class Solution {
  minPalindromePartitions(s, L) {
    const n = s.length;
    const isPal = Array.from({ length: n }, () => Array(n).fill(false));
    for (let len = 1; len <= n; len++) {
      for (let i = 0; i <= n - len; i++) {
        const j = i + len - 1;
        if (s[i] === s[j]) {
          if (len <= 2 || isPal[i + 1][j - 1]) {
            isPal[i][j] = true;
          }
        }
      }
    }

    let results = [];
    let minCount = Infinity;

    const backtrack = (start, current) => {
      if (start === n) {
        if (current.length < minCount) {
          minCount = current.length;
          results = [[...current]];
        } else if (current.length === minCount) {
          results.push([...current]);
        }
        return;
      }

      if (current.length >= minCount) return;

      for (let end = start; end < n; end++) {
        if (end - start + 1 > L) break;
        if (isPal[start][end]) {
          current.push(s.substring(start, end + 1));
          backtrack(end + 1, current);
          current.pop();
        }
      }
    };

    backtrack(0, []);
    return results;
  }
}
