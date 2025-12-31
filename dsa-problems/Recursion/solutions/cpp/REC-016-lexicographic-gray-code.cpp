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
