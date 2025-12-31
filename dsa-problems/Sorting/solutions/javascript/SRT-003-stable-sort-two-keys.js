class Solution {
  stableSort(records) {
    // JavaScript's sort is stable (since ES2019)
    records.sort((a, b) => {
      if (a[0] !== b[0]) {
        return a[0] - b[0];
      }
      return b[1] - a[1]; // Descending for key2
    });
    return records;
  }
}
