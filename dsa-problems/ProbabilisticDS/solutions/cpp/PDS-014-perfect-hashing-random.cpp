#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long totalSize(const vector<int>& sizes) {
        long long S = 0;
        for (int s : sizes) {
            S += (long long)s * s;
        }
        return S;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int t;
    if (cin >> n >> t) {
        vector<int> sizes(t);
        for (int i = 0; i < t; i++) cin >> sizes[i];
    
        Solution solution;
        long long S = solution.totalSize(sizes);
        cout << S << " " << (S <= 4 * n ? "YES" : "NO") << "\n";
    }
    return 0;
}
