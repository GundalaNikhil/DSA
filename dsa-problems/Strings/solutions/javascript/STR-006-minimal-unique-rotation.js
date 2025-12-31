function minimalUniqueRotation(s) {
  const n = s.length;

  // Booth's algorithm
  function boothMinimalRotationIndex(s) {
    const doubled = s + s;
    const n = s.length;
    const failure = new Array(2 * n).fill(-1);
    let k = 0;

    for (let j = 1; j < 2 * n; j++) {
      let i = failure[j - k - 1];
      while (i !== -1 && doubled[j] !== doubled[k + i + 1]) {
        if (doubled[j] < doubled[k + i + 1]) {
          k = j - i - 1;
        }
        i = failure[i];
      }

      if (doubled[j] !== doubled[k + i + 1]) {
        if (doubled[j] < doubled[k + i + 1]) {
          k = j;
        }
        failure[j - k] = -1;
      } else {
        failure[j - k] = i + 1;
      }
    }

    return k;
  }

  const minIdx = boothMinimalRotationIndex(s);
  const minRotation = s.slice(minIdx) + s.slice(0, minIdx);

  // Check if same as original
  if (minRotation === s) {
    return s;
  } else {
    return minRotation;
  }
}
