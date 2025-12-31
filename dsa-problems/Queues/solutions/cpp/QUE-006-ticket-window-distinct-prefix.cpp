#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

class Solution {
public:
    vector<string> firstNonRepeating(const string& s) {
        int count[26] = {0};
        queue<char> q;
        vector<string> result;
        
        for (char c : s) {
            count[c - 'a']++;
            q.push(c);
            
            while (!q.empty() && count[q.front() - 'a'] > 1) {
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

    string s;
    if (cin >> s) {
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
