#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
    struct Item {
        char c;
        int w;
    };
public:
    pair<string, long long> reduce(const string& s, const vector<int>& w) {
        vector<Item> stack; // Use vector as stack for easy string construction
        long long totalRemoved = 0;
        
        for (size_t i = 0; i < s.length(); ++i) {
            char currentChar = s[i];
            int currentWeight = w[i];
            
            if (!stack.empty() && stack.back().c == currentChar && (stack.back().w + currentWeight) % 2 == 0) {
                totalRemoved += stack.back().w + currentWeight;
                stack.pop_back();
            } else {
                stack.push_back({currentChar, currentWeight});
            }
        }
        
        string res = "";
        for (const auto& item : stack) {
            res += item.c;
        }
        
        return {res, totalRemoved};
    }
};
