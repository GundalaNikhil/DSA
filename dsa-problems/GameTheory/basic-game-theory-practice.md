# Original Game Theory & Grundy Practice Set (16 Questions)

## 1) Pile Split Choice
- Slug: pile-split-choice
- Difficulty: Easy-Medium
- Problem: A pile of `n` stones; on each turn a player may split one pile into two non-empty piles of different sizes. Player who cannot move loses. Determine the winner with optimal play for given `n`.
- Constraints: `1 <= n <= 10^5`.
- Hint: Compute Grundy for n using mex of splits; note pattern for small n.
- Example:
  - Input: `n=3`
  - Output: `First`

## 2) Token Walk on Directed Graph
- Slug: token-walk-directed-graph
- Difficulty: Medium
- Problem: Token on node s of a finite directed acyclic graph. Players alternate moving token along outgoing edge; player unable to move loses. For each node, determine if it is winning or losing.
- Constraints: `1 <= n <= 2 * 10^5`, edges <= 2 * 10^5.
- Hint: Topological order; propagate win/lose.
- Example:
  - Input: edges 0->1, 1->2
  - Output: node0 winning, node1 winning, node2 losing

## 3) Subtract-a-Square with Ban List
- Slug: subtract-square-ban-list
- Difficulty: Medium
- Problem: Starting with `n`, players subtract a perfect square s.t. the square is not in a banned set `B`. Player who reaches exactly 0 wins. Determine winner.
- Constraints: `1 <= n <= 10^5`, `|B| <= 100`.
- Hint: DP/Grundy up to n; moves exclude banned squares.
- Example:
  - Input: n=7, B={1}
  - Output: `Second`

## 4) Circular Nim Variant
- Slug: circular-nim-variant
- Difficulty: Medium
- Problem: Stones in a circle of piles. A move: pick a pile with >0 stones, remove any positive number, and also must add 1 stone to each adjacent pile (if present). Player unable to move loses. Determine winner for small n via Grundy up to `n<=20` and pile sizes <= 15.
- Constraints: n<=20, pile[i]<=15.
- Example:
  - Input: piles [1,0,1]
  - Output: `First`

## 5) Interval Removal Game
- Slug: interval-removal-game
- Difficulty: Medium
- Problem: Given disjoint intervals on a line. A move: choose an interval and remove any positive length sub-interval from it; remaining pieces stay. Player unable to move loses. For each interval, Grundy = length (as positions), game Nim-sum decides winner.
- Constraints: up to 10^5 intervals, lengths <= 10^9.
- Example:
  - Input: intervals [ [0,2], [5,6] ]
  - Output: `First`

## 6) Divisor Turn Game
- Slug: divisor-turn-game
- Difficulty: Medium
- Problem: Start with integer `n`. A move: replace n with any proper divisor (greater than 1). Player who cannot move loses. Determine winner.
- Constraints: `2 <= n <= 10^6`.
- Hint: Precompute win/lose; n is losing if all divisors lead to winning positions.
- Example:
  - Input: n=2
  - Output: `Second`

## 7) Grid Chomp with Walls
- Slug: grid-chomp-walls
- Difficulty: Medium
- Problem: m x n grid; some cells are walls. A move: pick a non-wall cell (i,j) and remove it along with all cells with row>=i and col>=j (like Chomp but with walls). Player unable to move loses. Compute winner for small grids (<=15x15).
- Constraints: m,n <= 15.
- Example:
  - Input: 2x2 grid all edible
  - Output: `First`

## 8) Kayles on Graph
- Slug: kayles-on-graph
- Difficulty: Hard
- Problem: Undirected graph. Move: choose a vertex, remove it and its neighbors. Player unable to move loses. Determine winner using Sprague-Grundy (connected components).
- Constraints: n <= 100, m <= 300.
- Example:
  - Input: path of 3 nodes
  - Output: `First`

## 9) Take-or-Split Heap
- Slug: take-or-split-heap
- Difficulty: Medium
- Problem: Single heap size `n`. Move: either take 1 stone, or split heap into two heaps of equal size (only if even). Player who takes last stone wins. Determine winner.
- Constraints: `1 <= n <= 10^6`.
- Hint: Grundy pattern; compute up to limit.
- Example:
  - Input: n=2
  - Output: `First`

## 10) Removal Game on Strings
- Slug: removal-game-strings
- Difficulty: Medium
- Problem: Given string `s`. Move: remove any palindrome substring of length >=2. Remaining parts concatenate. Player unable to move loses. Determine winner for |s|<=200 via Grundy with memo.
- Constraints: |s| <= 200.
- Example:
  - Input: "aba"
  - Output: `First`

## 11) Token on DAG with Skip Move
- Slug: token-dag-skip
- Difficulty: Medium
- Problem: DAG game; from a node, a move can go along an outgoing edge or skip over one node (two edges) if path exists. Compute winning nodes.
- Constraints: n<=2e5, m<=2e5.
- Hint: Topo order; consider both lengths 1 and 2 transitions.
- Example:
  - Input: 0->1->2
  - Output: node0 winning, node1 winning, node2 losing

## 12) Rectangular Chocolate Cut
- Slug: rectangular-chocolate-cut
- Difficulty: Medium
- Problem: Rect chocolate bar w x h. Move: cut along grid line into two rectangles; remove one of the resulting pieces of area <= K. Player unable to move loses.
- Constraints: w,h <= 30, K <= 20.
- Hint: Grundy on states (w,h).
- Example:
  - Input: w=2,h=2,K=2
  - Output: `First`

## 13) Bimatrix Zero-Sum Variant
- Slug: bimatrix-zero-sum-variant
- Difficulty: Medium
- Problem: Two players choose actions A_i and B_j with payoff matrix P (can be asymmetric). Find the value of the zero-sum game using linear programming or simplex; for small n,m brute force mixed strategies.
- Constraints: n,m <= 50.
- Example:
  - Input: P = [[1,-1],[-2,2]]
  - Output: game value between -1 and 1 (solve exactly)

## 14) Greedy Coin Split Game
- Slug: greedy-coin-split-game
- Difficulty: Medium
- Problem: Coins in a line with values v[i]. On your turn, choose a prefix or suffix and remove it, gaining sum of removed coins. Opponent then moves on remaining line. Maximize your total vs optimal opponent; compute optimal first-player total.
- Constraints: `1 <= n <= 2000`.
- Hint: Interval DP (not impartial, but competitive game).
- Example:
  - Input: [1,2,3]
  - Output: 4 (take suffix 3, opponent takes 2, take 1)

## 15) Turning Turtles
- Slug: turning-turtles
- Difficulty: Medium
- Problem: Array of turtles facing L/R. Move: choose a position i, flip all turtles from i to end (reverse direction). Player with all turtles facing R loses. Determine winner.
- Constraints: n <= 2000.
- Hint: Sprague-Grundy with prefix parity representation.
- Example:
  - Input: "LR"
  - Output: `First`

## 16) Weighted Nim Heaps
- Slug: weighted-nim-heaps
- Difficulty: Medium
- Problem: Each heap i has weight w[i]; removing k stones from heap i adds w[i]*k to your score. After all heaps empty, higher score wins. Compute optimal scores for both players.
- Constraints: `1 <= n <= 50`, heap sizes <= 50.
- Hint: Each heap is independent; but total score difference matters; use DP over heaps and possible score differences.
- Example:
  - Input: heaps [2,1], weights [3,1]
  - Output: First player score 7, second 0
