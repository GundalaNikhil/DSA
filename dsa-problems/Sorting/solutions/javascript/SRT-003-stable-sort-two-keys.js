class Solution {
  stableSort(records) {
    // JavaScript's sort is stable (since ES2019)
    records.sort((a, b) => {
      if (a[0] !== b[0]) {
        return a[0] - b[0];
      }
      return a[1] - b[1]; // Ascending for key2
    });
    return records;
  }
}
