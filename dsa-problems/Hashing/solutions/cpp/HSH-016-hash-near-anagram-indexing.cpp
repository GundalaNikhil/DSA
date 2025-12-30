#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <numeric>

using namespace std;

class UnionFind {
public:
    vector<int> parent;
    int count;
    
    UnionFind(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        count = n;
    }
    
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
            count--;
        }
    }
};

class Solution {
public:
    int countNearAnagramGroups(vector<string>& words) {
        int n = words.size();
        UnionFind uf(n);
        unordered_map<string, vector<int>> groups;
        
        for (int i = 0; i < n; i++) {
            string sortedWord = words[i];
            sort(sortedWord.begin(), sortedWord.end());
            
            int len = sortedWord.length();
            for (int j = 0; j < len; j++) {
                // Optimization: Skip if same char as previous to avoid duplicate work
                if (j > 0 && sortedWord[j] == sortedWord[j-1]) continue;
                
                string reduced = sortedWord.substr(0, j) + sortedWord.substr(j + 1);
                groups[reduced].push_back(i);
            }
        }
        
        for (auto& entry : groups) {
            vector<int>& indices = entry.second;
            if (indices.empty()) continue;
            int first = indices[0];
            for (size_t k = 1; k < indices.size(); k++) {
                uf.unite(first, indices[k]);
            }
        }
        
        return uf.count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<string> words(n);
        for (int i = 0; i < n; i++) {
            cin >> words[i];
        }
        
        Solution solution;
        cout << solution.countNearAnagramGroups(words) << "\n";
    }
    
    return 0;
}
