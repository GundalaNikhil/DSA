#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> mergeWithPriority(vector<int>& A, vector<int>& B) {
        int n = A.size();
        int m = B.size();
        vector<int> result;
        result.reserve(n + m);

        int i = 0, j = 0;

        while (i < n && j < m) {
            if (A[i] <= B[j]) {
                result.push_back(A[i++]);
            } else {
                result.push_back(B[j++]);
            }
        }

        while (i < n) result.push_back(A[i++]);
        while (j < m) result.push_back(B[j++]);

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    int m;
    cin >> m;
    vector<int> B(m);
    for (int i = 0; i < m; i++) cin >> B[i];

    Solution solution;
    vector<int> result = solution.mergeWithPriority(A, B);

    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
