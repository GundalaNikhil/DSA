class Solution {
  minInversionsAfterSwap(arr) {
    const n = arr.length;
    let best = this.countInversions(arr);

    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        const temp = arr.slice();
        const swap = temp[i];
        temp[i] = temp[j];
        temp[j] = swap;
        const inv = this.countInversions(temp);
        if (inv < best) {
          best = inv;
        }
      }
    }

    return best;
  }

  countInversions(arr) {
    const a = arr.slice();
    const temp = new Array(a.length);

    const mergeSort = (left, right) => {
      if (left >= right) {
        return 0;
      }
      const mid = Math.floor((left + right) / 2);
      let inv = mergeSort(left, mid);
      inv += mergeSort(mid + 1, right);
      inv += merge(left, mid, right);
      return inv;
    };

    const merge = (left, mid, right) => {
      let i = left;
      let j = mid + 1;
      let k = left;
      let inv = 0;

      while (i <= mid && j <= right) {
        if (a[i] <= a[j]) {
          temp[k++] = a[i++];
        } else {
          temp[k++] = a[j++];
          inv += mid - i + 1;
        }
      }

      while (i <= mid) {
        temp[k++] = a[i++];
      }

      while (j <= right) {
        temp[k++] = a[j++];
      }

      for (let idx = left; idx <= right; idx++) {
        a[idx] = temp[idx];
      }

      return inv;
    };

    if (a.length === 0) {
      return 0;
    }
    return mergeSort(0, a.length - 1);
  }
}
