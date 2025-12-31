#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    int weightedBalancePoint(vector<int>& a, int L, int R) {
        long long totalSum = 0;
        for (int x : a) totalSum += x;

        long long leftSum = 0;
        long long LL = L;
        long long RR = R;

        for (int i = 0; i < a.size(); i++) {
            long long rightSum = totalSum - leftSum - a[i];

            if (leftSum * LL == rightSum * RR) {
                return i;
            }

            leftSum += a[i];
        }

        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int L, R;
    cin >> L >> R;

    Solution solution;
    cout << solution.weightedBalancePoint(a, L, R) << "\n";
    return 0;
}
