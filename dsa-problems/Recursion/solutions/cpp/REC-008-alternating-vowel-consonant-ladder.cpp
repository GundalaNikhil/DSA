#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> ladders(string start, string end, const vector<string>& dict) {
        unordered_set<string> wordSet(dict.begin(), dict.end());
        wordSet.insert(start);
        wordSet.insert(end);
        
        unordered_map<string, vector<string>> parents;
        unordered_map<string, int> dist;
        queue<string> q;
        
        q.push(start);
        dist[start] = 0;
        
        bool found = false;
        
        while (!q.empty() && !found) {
            int size = q.size();
            unordered_set<string> levelVisited;
            
            for (int i = 0; i < size; i++) {
                string curr = q.front();
                q.pop();
                
                if (curr == end) found = true;
                
                string temp = curr;
                for (int j = 0; j < temp.length(); j++) {
                    char original = temp[j];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        temp[j] = c;
                        if (wordSet.count(temp) && isAlternating(curr, temp)) {
                            if (dist.find(temp) == dist.end()) {
                                if (levelVisited.find(temp) == levelVisited.end()) {
                                    dist[temp] = dist[curr] + 1;
                                    q.push(temp);
                                    levelVisited.insert(temp);
                                }
                                parents[temp].push_back(curr);
                            } else if (dist[temp] == dist[curr] + 1) {
                                parents[temp].push_back(curr);
                            }
                        }
                    }
                    temp[j] = original;
                }
            }
        }
        
        vector<vector<string>> results;
        if (found) {
            vector<string> path;
            path.push_back(end);
            backtrack(end, start, parents, path, results);
        }
        
        // Sort for deterministic output
        sort(results.begin(), results.end());
        
        return results;
    }

private:
    void backtrack(string curr, string start, unordered_map<string, vector<string>>& parents, vector<string>& path, vector<vector<string>>& results) {
        if (curr == start) {
            vector<string> fullPath = path;
            reverse(fullPath.begin(), fullPath.end());
            results.push_back(fullPath);
            return;
        }
        
        for (const string& p : parents[curr]) {
            path.push_back(p);
            backtrack(p, start, parents, path, results);
            path.pop_back();
        }
    }

    bool isAlternating(const string& a, const string& b) {
        return isVowel(a[0]) != isVowel(b[0]);
    }

    bool isVowel(char c) {
        return string("aeiou").find(c) != string::npos;
    }
};
