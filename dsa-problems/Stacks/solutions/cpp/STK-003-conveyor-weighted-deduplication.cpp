#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

struct Item {
    char c;
    int w;
};

class Solution {
public:
    pair<string, long long> reduce(string s, vector<int> w) {
        vector<Item> stack; // Use vector as stack for easy iteration
        long long totalRemoved = 0;
        
        for (size_t i = 0; i < s.length(); i++) {
            char currentChar = s[i];
            int currentWeight = w[i];
            
            if (!stack.empty() && stack.back().c == currentChar && (stack.back().w + currentWeight) % 2 == 0) {
                totalRemoved += (long long)stack.back().w + currentWeight;
                stack.pop_back();
            } else {
                stack.push_back({currentChar, currentWeight});
            }
        }
        
        string resS = "";
        for (const auto& item : stack) {
            resS += item.c;
        }
        
        return {resS, totalRemoved};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    string s = "";
    vector<int> w(n);
    
    for (int i = 0; i < n; i++) {
        char c;
        int weight;
        cin >> c >> weight;
        s += c;
        w[i] = weight;
    }
    
    Solution sol;
    pair<string, long long> res = sol.reduce(s, w);
    
    if (res.first.empty()) {
        cout << "EMPTY " << res.second << endl;
    } else {
        cout << res.first << " " << res.second << endl;
    }
    
    return 0;
}
