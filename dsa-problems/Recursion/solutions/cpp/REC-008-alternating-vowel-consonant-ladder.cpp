#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

class Solution {
    string S;
    int N;
    set<string> results;
    vector<bool> used;

public:
    vector<string> getAlternatingPermutations(string s) {
        S = s;
        N = s.length();
        results.clear();
        used.assign(N, false);
        string current = "";
        backtrack(current);
        return vector<string>(results.begin(), results.end());
    }

    bool is_vowel(char c) {
        return string("aeiou").find(c) != string::npos;
    }

    void backtrack(string& current) {
        if (current.length() == N) {
            results.insert(current);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!used[i]) {
                if (current.empty() || is_vowel(current.back()) != is_vowel(S[i])) {
                    used[i] = true;
                    current.push_back(S[i]);
                    backtrack(current);
                    current.pop_back();
                    used[i] = false;
                }
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s;
    if (!(cin >> s)) return 0;
    
    Solution sol;
    vector<string> res = sol.getAlternatingPermutations(s);
    if(res.empty()) {
        cout << "NONE" << endl;
    } else {
        for(const string& p : res) cout << p << endl;
    }
    return 0;
}
