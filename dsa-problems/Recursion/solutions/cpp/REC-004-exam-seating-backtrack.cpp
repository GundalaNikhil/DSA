#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long countArrangements(int n, int k, int d) {
        // N is small (15), so raw recursion is fine.
        // Adding memoization for completeness/scalability.
        vector<vector<long long>> memo(n + 1, vector<long long>(k + 1, -1));
        return solve(0, k, n, d, memo);
    }

private:
    long long solve(int idx, int k, int n, int d, vector<vector<long long>>& memo) {
        if (k == 0) return 1;
        if (idx >= n) return 0;
        
        if (memo[idx][k] != -1) return memo[idx][k];
        
        // Option 1: Place student
        long long res = solve(idx + d + 1, k - 1, n, d, memo);
        
        // Option 2: Skip seat
        res += solve(idx + 1, k, n, d, memo);
        
        return memo[idx][k] = res;
    }
};
