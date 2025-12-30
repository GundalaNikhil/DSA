class Solution {
  partialSelectionSort(arr, k) {
    const n = arr.length;
    for (let i = 0; i < k; i++) {
      let minIndex = i;
      for (let j = i + 1; j < n; j++) {
        if (arr[j] < arr[minIndex]) {
          minIndex = j;
        }
      }
      [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
    }
    return arr;
  }
}
