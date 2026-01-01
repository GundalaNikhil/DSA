#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Solution {
    long long maxDiameter = 0;

    long long dfs(int u, const vector<int>& left, const vector<int>& right,
                  const vector<long long>& lw, const vector<long long>& rw) {
        if (u == -1) return 0;
        long long lPath = 0;
        long long rPath = 0;
        if (left[u] != -1) {
            lPath = lw[u] + dfs(left[u], left, right, lw, rw);
        }
        if (right[u] != -1) {
            rPath = rw[u] + dfs(right[u], left, right, lw, rw);
        }
        if (lPath + rPath > maxDiameter) {
            maxDiameter = lPath + rPath;
        }
        return lPath > rPath ? lPath : rPath;
    }

public:
    long long weightedDiameter(int n, const vector<int>& left, const vector<int>& right,
                               const vector<long long>& lw, const vector<long long>& rw) {
        if (n == 0) return 0;
        vector<bool> hasParent(n, false);
        for (int i = 0; i < n; i++) {
            if (left[i] != -1) hasParent[left[i]] = true;
            if (right[i] != -1) hasParent[right[i]] = true;
        }
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (!hasParent[i]) {
                root = i;
                break;
            }
        }
        maxDiameter = 0;
        dfs(root, left, right, lw, rw);
        return maxDiameter;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<string> lines;
    string line;
    while (getline(cin, line)) {
        if (!line.empty()) {
            bool allSpace = true;
            for (char ch : line) {
                if (ch > ' ') {
                    allSpace = false;
                    break;
                }
            }
            if (!allSpace) lines.push_back(line);
        }
    }
    if (lines.empty()) return 0;

    int n = stoi(lines[0]);
    vector<int> left(n, -1), right(n, -1);
    vector<long long> lw(n, 1), rw(n, 1);

    for (int i = 0; i < n && i + 1 < (int)lines.size(); i++) {
        stringstream ss(lines[i + 1]);
        vector<long long> parts;
        long long x;
        while (ss >> x) parts.push_back(x);
        if (parts.size() < 3) continue;
        left[i] = (int)parts[1];
        right[i] = (int)parts[2];
        if (parts.size() >= 5) {
            lw[i] = parts[3];
            rw[i] = parts[4];
        }
    }

    Solution solution;
    cout << solution.weightedDiameter(n, left, right, lw, rw) << "\n";
    return 0;
}
