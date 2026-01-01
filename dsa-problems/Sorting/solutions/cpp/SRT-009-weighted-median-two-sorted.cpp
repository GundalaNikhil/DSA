#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    string weightedMedian(const vector<int>& A, const vector<int>& B, long long wA, long long wB) {
        vector<int> combined;
        combined.reserve(A.size() + B.size());
        combined.insert(combined.end(), A.begin(), A.end());
        combined.insert(combined.end(), B.begin(), B.end());
        sort(combined.begin(), combined.end());

        int n = combined.size();
        if (n % 2 == 1) {
            return to_string(combined[n / 2]);
        }

        int mid1 = combined[n / 2 - 1];
        int mid2 = combined[n / 2];
        int avg = (mid1 + mid2) / 2;
        return to_string(avg);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<int> A(n);
    vector<int> B(m);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> B[i];
    }
    Solution solution;
    cout << solution.weightedMedian(A, B, 1, 1) << "\n";
    return 0;
}
