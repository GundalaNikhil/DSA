const NEG = BigInt(-4e18);

function maxProfit(prices, fee) {
  const n = prices.length;
  let buyable = 0n, hold = NEG, ans = 0n;
  const unlock = Array(n + 8).fill(NEG);
  for (let i = 0; i < n; i++) {
    if (unlock[i] !== NEG) buyable = buyable > unlock[i] ? buyable : unlock[i];
    const prevHold = hold;
    hold = hold > buyable - BigInt(prices[i]) ? hold : buyable - BigInt(prices[i]);
    if (prevHold !== NEG) {
      const sellProfit = prevHold + BigInt(prices[i]) - BigInt(fee);
      if (sellProfit > ans) ans = sellProfit;
      const nextMonday = i - (i % 7) + 7;
      if (nextMonday < unlock.length && sellProfit > unlock[nextMonday]) {
        unlock[nextMonday] = sellProfit;
      }
    }
  }
  if (hold !== NEG) ans = ans > hold + BigInt(prices[n - 1]) - BigInt(fee) ? ans : hold + BigInt(prices[n - 1]) - BigInt(fee);
  if (buyable > ans) ans = buyable;
  for (let i = n; i < unlock.length; i++) if (unlock[i] > ans) ans = unlock[i];
  return Number(ans);
}
