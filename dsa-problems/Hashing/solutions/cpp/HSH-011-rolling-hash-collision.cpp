#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    long long B, M;
    int L;
    unordered_map<long long, string> seen;

public:
    pair<string, string> findCollision(long long B, long long M, int L) {
        this->B = B;
        this->M = M;
        this->L = L;
        seen.clear();
        
        string current = "";
        return dfs(current);
    }
    
    pair<string, string> dfs(string& current) {
        if (current.length() == L) {
            long long h = computeHash(current);
            if (seen.count(h)) {
                return {seen[h], current};
            }
            seen[h] = current;
            return {"", ""};
        }
        
        for (char c = 'a'; c <= 'z'; c++) {
            current.push_back(c);
            pair<string, string> res = dfs(current);
            if (res.first != "") return res;
            current.pop_back();
        }
        return {"", ""};
    }
    
    long long computeHash(const string& s) {
        long long h = 0;
        for (char c : s) {
            h = (h * B + c) % M;
        }
        return h;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    long long B, M;
    int L;
    if (cin >> B >> M >> L) {
        Solution solution;
        auto result = solution.findCollision(B, M, L);
        cout << result.first << "\n" << result.second << "\n";
    }
    
    return 0;
}
