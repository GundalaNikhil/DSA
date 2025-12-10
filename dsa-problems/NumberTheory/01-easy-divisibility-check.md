# Team Formation Fairness

**Difficulty:** Easy
**Topic:** Number Theory, Divisibility
**License:** Free to use for commercial purposes

## Problem Statement

A sports league has `totalPlayers` registered players. The league wants to form `teams` number of teams. Determine if it's possible to assign every player to a team such that each team has exactly the same number of players, with no players left out.

Return `true` if a fair formation is possible, `false` otherwise.

## Constraints

- `1 <= totalPlayers <= 100000`
- `1 <= teams <= 10000`

## Examples

### Example 1
```
Input: totalPlayers = 22, teams = 11
Output: true
Explanation: 22 / 11 = 2. Each team gets 2 players.
```

### Example 2
```
Input: totalPlayers = 23, teams = 5
Output: false
Explanation: 23 is not divisible by 5.
```

### Example 3
```
Input: totalPlayers = 100, teams = 4
Output: true
Explanation: 25 players per team.
```

## Function Signature

### Python
```python
def can_form_teams(totalPlayers: int, teams: int) -> bool:
    pass
```

### JavaScript
```javascript
function canFormTeams(totalPlayers, teams) {
    // Your code here
}
```

### Java
```java
public boolean canFormTeams(int totalPlayers, int teams) {
    // Your code here
}
```

## Hints
1. Modulo operator

## Tags
`number-theory` `divisibility` `easy`
