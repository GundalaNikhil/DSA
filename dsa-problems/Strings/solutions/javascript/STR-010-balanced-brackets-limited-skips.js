function canBalanceWithSkips(s, k) {
  let balance = 0;
  let skipsUsed = 0;

  for (let char of s) {
    if (char === "(") {
      balance++;
    } else {
      // char === ')'
      balance--;
      if (balance < 0) {
        // Need to skip this ')'
        skipsUsed++;
        balance = 0;
      }
    }
  }

  // Remaining balance are unmatched '('
  const totalSkipsNeeded = skipsUsed + balance;
  return totalSkipsNeeded <= k;
}
