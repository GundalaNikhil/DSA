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
    string compressWithWindow(string s, int w) {
        if (s.empty()) {
            return "";
        }

        string result;
        int i = 0;
        int n = s.size();

        while (i < n) {
            int start = i;
            char ch = s[i];

            // Count consecutive occurrences
            while (i < n && s[i] == ch) {
                i++;
            }

            int runLength = i - start;

            // Compress if >= threshold
            if (runLength >= w) {
                result += ch;
                result += to_string(runLength);
            } else {
                result.append(runLength, ch);
            }
        }

        return result;
    }
};

















int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int w; cin >> w;
    Solution sol;
    cout << sol.compressWithWindow(s, w) << endl;
    return 0;
}
