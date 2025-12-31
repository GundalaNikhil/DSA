#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Project {
    long long c, p, r;
};

struct CompareProfit {
    bool operator()(const Project& a, const Project& b) {
        return a.p < b.p; // Max heap
    }
};

class Solution {
public:
    long long maximizeCapital(int k, long long C, long long R, const vector<long long>& cost,
                              const vector<long long>& profit, const vector<long long>& risk) {
        int n = cost.size();
        vector<Project> projects(n);
        for (int i = 0; i < n; i++) {
            projects[i] = {cost[i], profit[i], risk[i]};
        }
        
        sort(projects.begin(), projects.end(), [](const Project& a, const Project& b) {
            return a.c < b.c;
        });
        
        priority_queue<Project, vector<Project>, CompareProfit> pq;
        int ptr = 0;
        long long currentC = C;
        long long remainingR = R;
        
        for (int i = 0; i < k; i++) {
            while (ptr < n && projects[ptr].c <= currentC) {
                pq.push(projects[ptr]);
                ptr++;
            }
            
            bool picked = false;
            while (!pq.empty()) {
                Project top = pq.top();
                if (top.r <= remainingR) {
                    pq.pop();
                    currentC += top.p;
                    remainingR -= top.r;
                    picked = true;
                    break;
                } else {
                    pq.pop();
                }
            }
            
            if (!picked) break;
        }
        
        return currentC;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, k;
    long long C, R;
    if (cin >> n >> k >> C >> R) {
        vector<long long> cost(n), profit(n), risk(n);
        for (int i = 0; i < n; i++) cin >> cost[i] >> profit[i] >> risk[i];
        
        Solution solution;
        cout << solution.maximizeCapital(k, C, R, cost, profit, risk) << "\n";
    }
    return 0;
}
