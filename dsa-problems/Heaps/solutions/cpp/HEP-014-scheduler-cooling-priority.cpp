#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

struct Task {
    string id;
    int count;
    long long priority;
    int x;
};

class Solution {
public:
    long long maxPriority(int T, int cooldown, const vector<string>& ids,
                          const vector<int>& count, const vector<long long>& priority) {
        int m = ids.size();
        vector<Task> tasks;
        for (int i = 0; i < m; i++) {
            tasks.push_back({ids[i], count[i], priority[i], count[i]});
        }
        
        // 1. Clamp
        int limit = (T + cooldown) / (cooldown + 1);
        for (auto& t : tasks) {
            t.x = min(t.count, limit);
        }
        
        // 2. Schedule Constraint
        while (true) {
            int maxX = 0;
            for (const auto& t : tasks) maxX = max(maxX, t.x);
            
            if (maxX == 0) break;
            
            vector<Task*> atMax;
            for (auto& t : tasks) {
                if (t.x == maxX) atMax.push_back(&t);
            }
            
            long long required = (long long)(maxX - 1) * (cooldown + 1) + atMax.size();
            
            if (required <= T) break;
            
            long long allowed = T - (long long)(maxX - 1) * (cooldown + 1);
            
            sort(atMax.begin(), atMax.end(), [](Task* a, Task* b) {
                return a->priority > b->priority;
            });
            
            for (size_t i = allowed; i < atMax.size(); i++) {
                atMax[i]->x--;
            }
        }
        
        // 3. Sum Constraint
        long long sumX = 0;
        for (const auto& t : tasks) sumX += t.x;
        
        if (sumX > T) {
            long long toRemove = sumX - T;
            sort(tasks.begin(), tasks.end(), [](const Task& a, const Task& b) {
                return a.priority < b.priority;
            });
            
            for (auto& t : tasks) {
                if (toRemove <= 0) break;
                int rem = min((long long)t.x, toRemove);
                t.x -= rem;
                toRemove -= rem;
            }
        }
        
        long long totalScore = 0;
        for (const auto& t : tasks) totalScore += (long long)t.x * t.priority;
        
        return totalScore;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int m, cooldown, T;
    if (cin >> m >> cooldown >> T) {
        vector<string> ids(m);
        vector<int> count(m);
        vector<long long> priority(m);
        for (int i = 0; i < m; i++) cin >> ids[i] >> count[i] >> priority[i];
        
        Solution solution;
        cout << solution.maxPriority(T, cooldown, ids, count, priority) << "\n";
    }
    return 0;
}
