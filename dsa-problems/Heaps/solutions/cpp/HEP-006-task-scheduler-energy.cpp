#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Task {
    int d, g;
};

class Solution {
public:
    int maxTasks(long long E, const vector<int>& duration, const vector<int>& gain) {
        vector<Task> positive, negative;
        for (size_t i = 0; i < duration.size(); i++) {
            if (gain[i] >= duration[i]) {
                positive.push_back({duration[i], gain[i]});
            } else {
                negative.push_back({duration[i], gain[i]});
            }
        }
        
        sort(positive.begin(), positive.end(), [](const Task& a, const Task& b) {
            return a.d < b.d;
        });
        
        int count = 0;
        for (const auto& t : positive) {
            if (E >= t.d) {
                E += (t.g - t.d);
                count++;
            } else {
                break;
            }
        }

        long long peakE = E;
        
        sort(negative.begin(), negative.end(), [](const Task& a, const Task& b) {
            return a.g > b.g;
        });
        
        priority_queue<int> pq; // Max heap for losses
        long long currentLossSum = 0;
        
        for (const auto& t : negative) {
            int loss = t.d - t.g;
            currentLossSum += loss;
            pq.push(loss);
            if (currentLossSum + t.g > peakE) {
                currentLossSum -= pq.top();
                pq.pop();
            }
        }
        
        return count + (int)pq.size();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    long long E;
    if (cin >> n >> E) {
        vector<int> duration(n), gain(n);
        for (int i = 0; i < n; i++) cin >> duration[i] >> gain[i];
        
        Solution solution;
        cout << solution.maxTasks(E, duration, gain) << "\n";
    }
    return 0;
}
