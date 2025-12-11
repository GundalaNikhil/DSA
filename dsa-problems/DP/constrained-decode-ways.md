# Constrained Decode Ways

## Problem Metadata
- **unique_problem_id**: `dp_014`
- **display_id**: `DP-014`
- **slug**: `constrained-decode-ways`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "String", "Decoding"]`

## Problem Title
Constrained Decode Ways

## Problem Description
A digit string can be decoded into letters using the mapping:
- '1' → 'A', '2' → 'B', ..., '26' → 'Z'

Standard decoding rules apply, but with an additional constraint:
- Any digit '0' must be immediately preceded by an even digit to form a valid two-digit code
- The only valid code with '0' is "20" (even digit 2 followed by 0)

Count the number of ways to decode the given digit string under these constraints.

## Examples

### Example 1
**Input:**
```
s = "2012"
```

**Output:**
```
2
```

**Explanation:**
- Decoding 1: "20" + "12" → "T" + "L" = "TL"
- Decoding 2: "20" + "1" + "2" → "T" + "A" + "B" = "TAB"
- Invalid: "2" + "0" + ... (0 not preceded by even in the pair)
- Total: 2 ways

### Example 2
**Input:**
```
s = "2020"
```

**Output:**
```
1
```

**Explanation:**
- Only valid: "20" + "20" → "TT"
- Cannot split as "2" + "02" + "0" (leading zero invalid)
- Total: 1 way

### Example 3
**Input:**
```
s = "10"
```

**Output:**
```
0
```

**Explanation:**
- "10" is invalid because 1 is odd, and '0' must follow an even digit
- No valid decodings

### Example 4
**Input:**
```
s = "12"
```

**Output:**
```
2
```

**Explanation:**
- Decoding 1: "12" → "L"
- Decoding 2: "1" + "2" → "AB"
- Total: 2 ways

## Constraints
- `1 <= |s| <= 10^5`
- String consists of digits '0' through '9'
- May contain leading zeros or invalid patterns

## Function Signatures

### Java
```java
class Solution {
    public int numDecodings(String s) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int numDecodings(string s) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: String s (digit string to decode)
```

### Sample Input
```
2012
```

## Hints
- Use DP where dp[i] = number of ways to decode s[0..i-1]
- At each position, consider:
  - Single digit decode: s[i] must be '1'-'9'
  - Two digit decode: s[i-1:i+1] must be in range "10"-"26"
- Special constraint: If s[i] == '0', it can ONLY be decoded as part of "20"
- Check that s[i-1] == '2' when encountering '0'
- Base cases: dp[0] = 1 (empty string), dp[1] depends on s[0]
- Time complexity: O(n)

## Related Topics Quiz

### Question 1
How is this different from standard "Decode Ways" problem?
- A) It uses different letter mappings
- B) It restricts '0' to only be valid after even digits
- C) It allows more than 26 codes
- D) It requires minimum length

**Answer:** B) It restricts '0' to only be valid after even digits - Only "20" is valid for zero.

### Question 2
What is the time complexity?
- A) O(n)
- B) O(n²)
- C) O(2^n)
- D) O(n log n)

**Answer:** A) O(n) - Single pass through the string with constant-time operations.

### Question 3
Why is "10" invalid in this problem?
- A) 10 is out of range for letter mapping
- B) 1 is odd, and 0 must follow an even digit
- C) Leading zeros not allowed
- D) It would decode to 'J'

**Answer:** B) 1 is odd, and 0 must follow an even digit - The constraint requires even digit before '0'.

### Question 4
What should we return if the string starts with '0'?
- A) 1
- B) 0
- C) -1
- D) Length of string

**Answer:** B) 0 - Leading zeros make the string invalid for decoding.

### Question 5
Which two-digit combinations with '0' are valid?
- A) 10, 20, 30, ...
- B) Only 20
- C) 20, 40, 60, 80
- D) None

**Answer:** B) Only 20 - The problem restricts '0' to follow even digits, and only 20 is in range [10, 26].
