#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <sstream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<string> firstNonRepeating(const string& s) {
        unordered_map<char, int> count;
        queue<char> q;
        vector<string> result;

        for (char c : s) {
            count[c]++;
            q.push(c);

            while (!q.empty() && count[q.front()] > 1) {
                q.pop();
            }

            if (q.empty()) {
                result.push_back("#");
            } else {
                string temp(1, q.front());
                result.push_back(temp);
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    string s;
    while (getline(cin, line)) {
        s += line + "\n";
    }

    // Remove trailing newline if present
    if (!s.empty() && s.back() == '\n') {
        s.pop_back();
    }

    if (!s.empty()) {
        Solution solution;
        vector<string> result = solution.firstNonRepeating(s);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
