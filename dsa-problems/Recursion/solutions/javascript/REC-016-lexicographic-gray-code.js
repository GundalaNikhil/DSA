class Solution {
  grayCode(n) {
    if (n === 1) return ["0", "1"];

    const prev = this.grayCode(n - 1);
    const result = [];

    for (const s of prev) {
      result.push("0" + s);
    }

    for (let i = prev.length - 1; i >= 0; i--) {
      result.push("1" + prev[i]);
    }

    return result;
  }
}
