#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int findFlipIndex(const vector<int>& nums, string ops, int target) {
        int n_ops = ops.length();
        for (int flip_idx = 0; flip_idx < n_ops; flip_idx++) {
            long long current_sum = nums[0];
            for (int i = 0; i < n_ops; i++) {
                char op;
                if (i == flip_idx) {
                    op = (ops[i] == '+') ? '-' : '+';
                } else {
                    op = ops[i];
                }

                if (op == '+') {
                    current_sum += nums[i + 1];
                } else {
                    current_sum -= nums[i + 1];
                }
            }
            if (current_sum == target) {
                return flip_idx;
            }
        }
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> nums(n);
    for(int i=0; i<n; i++) cin >> nums[i];
    
    string ops; cin >> ops;
    int target; cin >> target;
    
    Solution sol;
    cout << sol.findFlipIndex(nums, ops, target) << endl;
    return 0;
}
