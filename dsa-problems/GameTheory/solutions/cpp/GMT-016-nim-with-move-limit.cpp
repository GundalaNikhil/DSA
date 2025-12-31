#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string nimLimit(int n, vector<int>& A, vector<int>& L) {
        long long xorSum = 0;
        for (int i = 0; i < n; i++) {
            xorSum ^= (A[i] % (L[i] + 1));
        }
        return xorSum > 0 ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }
        vector<int> L(n);
        for (int i = 0; i < n; i++) {
            cin >> L[i];
        }
        
        Solution solution;
        cout << solution.nimLimit(n, A, L) << "\n";
    }
    return 0;
}
