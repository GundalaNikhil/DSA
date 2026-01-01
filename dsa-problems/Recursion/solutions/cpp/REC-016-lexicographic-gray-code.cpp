#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> grayCode(int n) {
        if (n == 1) return {"0", "1"};
        
        vector<string> prev = grayCode(n - 1);
        vector<string> result;
        result.reserve(prev.size() * 2);
        
        for (const string& s : prev) {
            result.push_back("0" + s);
        }
        
        for (auto it = prev.rbegin(); it != prev.rend(); ++it) {
            result.push_back("1" + *it);
        }
        
        return result;
    }
};






int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    Solution sol;
    vector<string> res = sol.grayCode(n); for(const string& s : res) cout << s << endl; if(res.empty()) cout << "NONE" << endl;
    return 0;
}
