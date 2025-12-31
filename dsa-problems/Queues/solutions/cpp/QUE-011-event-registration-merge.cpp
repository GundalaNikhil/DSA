#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> mergeQueues(const vector<int>& a, const vector<int>& b) {
        int n = a.size();
        int m = b.size();
        vector<int> result;
        result.reserve(n + m);
        
        int i = 0, j = 0;
        while (i < n && j < m) {
            if (a[i] <= b[j]) {
                result.push_back(a[i++]);
            } else {
                result.push_back(b[j++]);
            }
        }
        
        while (i < n) result.push_back(a[i++]);
        while (j < m) result.push_back(b[j++]);
        
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        int m;
        cin >> m;
        vector<int> b(m);
        for (int i = 0; i < m; i++) {
            cin >> b[i];
        }
    
        Solution solution;
        vector<int> result = solution.mergeQueues(a, b);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
