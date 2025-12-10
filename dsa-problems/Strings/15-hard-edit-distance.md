# Typo Correction Cost

**Difficulty:** Hard
**Topic:** Strings, Dynamic Programming
**License:** Free to use for commercial purposes

## Problem Statement

An autocorrect system calculates the "cost" to change a typed word into a dictionary word. Operations (insert, delete, replace) cost 1 unit.

Find minimum cost to convert `typed` to `target`.

## Constraints

- `0 <= typed.length, target.length <= 500`

## Examples

### Example 1
```
Input: typed = "algorithm", target = "altruistic"
Output: 6
Explanation:
algorithm -> algrithm (del o)
algrithm -> alrithm (del g)
alrithm -> alrthm (del i)
alrthm -> alrth (del m)
alrth -> alrt (del h)
... this is hard to trace manually.
Let's use simpler example.
Input: typed = "sunday", target = "saturday"
Output: 3
Explanation:
sunday -> stunday (ins t)
stunday -> strunday (ins r)
strunday -> saturday (sub n->a)
```

### Example 2
```
Input: typed = "kitten", target = "sitting"
Output: 3
Explanation:
k->s
e->i
insert g
```

### Example 3
```
Input: typed = "same", target = "same"
Output: 0
```

## Function Signature

### Python
```python
def calculate_edit_cost(typed: str, target: str) -> int:
    pass
```

### JavaScript
```javascript
function calculateEditCost(typed, target) {
    // Your code here
}
```

### Java
```java
public int calculateEditCost(String typed, String target) {
    // Your code here
}
```

## Hints
1. Levenshtein distance DP

## Tags
`string` `edit-distance` `hard`
