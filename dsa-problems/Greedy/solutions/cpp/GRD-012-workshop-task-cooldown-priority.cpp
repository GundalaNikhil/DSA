#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Task {
    char name;
    int count;
    int priority;
    int readyTime;
    
    // Priority Queue needs operator<
    // We want High Priority first, then High Count
    bool operator<(const Task& other) const {
        if (priority != other.priority) return priority < other.priority;
        return count < other.count;
    }
};

class Solution {
public:
    int minSlots(vector<Task>& inputTasks, int k) {
        priority_queue<Task> readyQueue;
        for(auto t : inputTasks) {
            t.readyTime = 0;
            readyQueue.push(t);
        }
        
        vector<Task> cooldownList;
        int time = 0;
        int tasksRemaining = 0;
        for(auto t : inputTasks) tasksRemaining += t.count;
        
        while(tasksRemaining > 0) {
            time++;
            
            // Move ready tasks
            vector<Task> nextCooldown;
            for(auto& t : cooldownList) {
                if(t.readyTime <= time) {
                    readyQueue.push(t);
                } else {
                    nextCooldown.push_back(t);
                }
            }
            cooldownList = nextCooldown;
            
            if(readyQueue.empty()) {
                continue;
            }
            
            Task current = readyQueue.top();
            readyQueue.pop();
            
            current.count--;
            tasksRemaining--;
            
            // Apply Interrupts
            for(auto& t : cooldownList) {
                if(t.priority < current.priority) {
                    t.readyTime = max(t.readyTime, time + k + 1);
                }
            }
            
            if(current.count > 0) {
                current.readyTime = time + k + 1;
                cooldownList.push_back(current);
            }
        }
        
        return time;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<Task> tasks(n);
    for (int i = 0; i < n; i++) {
        cin >> tasks[i].name >> tasks[i].count >> tasks[i].priority;
    }

    Solution solution;
    cout << solution.minSlots(tasks, k) << "\n";

    return 0;
}
