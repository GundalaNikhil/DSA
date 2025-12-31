#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> lcpArray(const string& s, const vector<int>& sa) {
        int n = s.length();
        vector<int> rank(n);
        for (int i = 0; i < n; i++) {
            rank[sa[i]] = i;
        }
        
        vector<int> lcp(n - 1);
        int k = 0;
        
        for (int i = 0; i < n; i++) {
            if (rank[i] == n - 1) {
                k = 0;
                continue;
            }
            
            int j = sa[rank[i] + 1];
            while (i + k < n && j + k < n && s[i + k] == s[j + k]) {
                k++;
            }
            
            lcp[rank[i]] = k;
            if (k > 0) k--;
        }
        return lcp;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        int n;
        cin >> n;
        vector<int> sa(n);
        for (int i = 0; i < n; i++) cin >> sa[i];
        
        Solution solution;
        vector<int> lcp = solution.lcpArray(s, sa);
        for (int i = 0; i < (int)lcp.size(); i++) {
            if (i > 0) cout << " ";
            cout << lcp[i];
        }
        cout << "\n";
    }
    return 0;
}
