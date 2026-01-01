#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
class Solution {
public:
    string decodeWithCap(string s, int cap) {
        string result;
        int i = 0;
        int n = s.size();

        while (i < n) {
            // Read character
            char ch = s[i];
            i++;

            // Read count
            string countStr;
            while (i < n && isdigit(s[i])) {
                countStr += s[i];
                i++;
            }

            // Decode with cap
            int count = countStr.empty() ? 1 : stoi(countStr);
            int actualCount = min(count, cap);

            result.append(actualCount, ch);
        }

        return result;
    }
};

















int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int cap; cin >> cap;
    Solution sol;
    cout << sol.decodeWithCap(s, cap) << endl;
    return 0;
}
