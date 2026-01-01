#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lcaBlocked(int n, const vector<int>& values, const vector<int>& blocked,
                   const vector<int>& left, const vector<int>& right, int u, int v) {
        vector<int> parent(n, -1);
        for (int i = 0; i < n; i++) {
            if (left[i] != -1) parent[left[i]] = i;
            if (right[i] != -1) parent[right[i]] = i;
        }

        unordered_set<int> ancestors;
        int curr = u;
        int steps = 0;
        while (curr != -1 && steps < n + 5) {
            ancestors.insert(curr);
            curr = parent[curr];
            steps++;
        }

        int lca = -1;
        curr = v;
        steps = 0;
        while (curr != -1 && steps < n + 5) {
            if (ancestors.count(curr)) {
                lca = curr;
                break;
            }
            curr = parent[curr];
            steps++;
        }

        if (lca == -1) return -1;

        steps = 0;
        while (lca != -1 && blocked[lca] == 1 && steps < n + 5) {
            lca = parent[lca];
            steps++;
        }

        return lca != -1 ? values[lca] : -1;
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
    vector<int> values(n, 0), blocked(n, 0), left(n, -1), right(n, -1);

    for (int i = 0; i < n && i + 1 < (int)lines.size(); i++) {
        stringstream ss(lines[i + 1]);
        vector<long long> parts;
        long long x;
        while (ss >> x) parts.push_back(x);
        if (parts.size() < 3) continue;
        values[i] = (int)parts[0];
        if (parts.size() >= 4) {
            blocked[i] = (int)parts[1];
            left[i] = (int)parts[2];
            right[i] = (int)parts[3];
        } else {
            blocked[i] = 0;
            left[i] = (int)parts[1];
            right[i] = (int)parts[2];
        }
    }

    if ((int)lines.size() <= n + 1) return 0;
    stringstream uv(lines[n + 1]);
    int u = 0, v = 0;
    if (!(uv >> u >> v)) return 0;

    Solution solution;
    cout << solution.lcaBlocked(n, values, blocked, left, right, u, v) << "\n";
    return 0;
}
