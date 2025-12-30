#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> allOrderings(int n, const vector<pair<int,int>>& edges) {
        vector<vector<int>> adj(n);
        vector<int> indegree(n, 0);
        for (const auto& edge : edges) {
            adj[edge.first].push_back(edge.second);
            indegree[edge.second]++;
        }

        vector<vector<int>> result;
        vector<int> path;
        vector<bool> visited(n, false);
        
        backtrack(n, adj, indegree, visited, path, result);
        return result;
    }

private:
    void backtrack(int n, const vector<vector<int>>& adj, vector<int>& indegree, 
                   vector<bool>& visited, vector<int>& path, vector<vector<int>>& result) {
        if (path.size() == n) {
            result.push_back(path);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i] && indegree[i] == 0) {
                visited[i] = true;
                path.push_back(i);
                for (int neighbor : adj[i]) {
                    indegree[neighbor]--;
                }

                backtrack(n, adj, indegree, visited, path, result);

                for (int neighbor : adj[i]) {
                    indegree[neighbor]++;
                }
                path.pop_back();
                visited[i] = false;
            }
        }
    }
};
