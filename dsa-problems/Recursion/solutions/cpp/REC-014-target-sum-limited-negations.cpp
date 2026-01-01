#include <iostream>
#include <vector>
#include <numeric>
#include <map>

using namespace std;

class Solution {
    int N;
    int K;
    int Target;
    map<pair<int, pair<int, int>>, bool> memo;
    vector<int> Nums;

public:
    bool countAssignments(const vector<int>& nums, int k, int target) {
        Nums = nums;
        N = nums.size();
        K = k;
        Target = target;
        memo.clear();
        return backtrack(0, 0, 0);
    }

    bool backtrack(int index, long long current_sum, int negations) {
        if (index == N) {
            return current_sum == Target;
        }
        
        // Memo key: index, sum, negations
        // sum can be negative. Map handles pair safely.
        if (memo.count({index, {(int)current_sum, negations}})) {
            return memo[{index, {(int)current_sum, negations}}];
        }

        // Option 1: Positive (Add)
        if (backtrack(index + 1, current_sum + Nums[index], negations)) {
            return memo[{index, {(int)current_sum, negations}}] = true;
        }

        // Option 2: Negative (Subtract) - consumes negation
        if (negations < K) {
            if (backtrack(index + 1, current_sum - Nums[index], negations + 1)) {
                return memo[{index, {(int)current_sum, negations}}] = true;
            }
        }

        return memo[{index, {(int)current_sum, negations}}] = false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; 
    if (!(cin >> n)) return 0;
    
    int k, target; 
    cin >> k >> target;
    
    vector<int> nums(n);
    for(int i=0; i<n; i++) cin >> nums[i];

    Solution sol;
    if (sol.countAssignments(nums, k, target)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}
