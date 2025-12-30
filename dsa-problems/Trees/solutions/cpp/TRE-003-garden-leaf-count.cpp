#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int countLeaves(int n, const vector<int>& left, const vector<int>& right) {
        if (n == 0) return 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] == -1 && right[i] == -1) {
                count++;
            }
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val >> left[i] >> right[i];
    }

    Solution solution;
    cout << solution.countLeaves(n, left, right) << "\n";
    return 0;
}
