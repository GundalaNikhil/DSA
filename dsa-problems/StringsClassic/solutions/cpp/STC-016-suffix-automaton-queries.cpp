#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct State {
    int len, link;
    map<char, int> next;
    long long cnt = 0;
};

class Solution {
    vector<State> st;
    int sz, last;

    void extend(char c) {
        int cur = sz++;
        st.emplace_back();
        st[cur].len = st[last].len + 1;
        st[cur].cnt = 1;
        st[cur].link = 0; // Default
        
        int p = last;
        while (p != -1 && st[p].next.find(c) == st[p].next.end()) {
            st[p].next[c] = cur;
            p = st[p].link;
        }
        
        if (p == -1) {
            st[cur].link = 0;
        } else {
            int q = st[p].next[c];
            if (st[p].len + 1 == st[q].len) {
                st[cur].link = q;
            } else {
                int clone = sz++;
                st.emplace_back();
                st[clone].len = st[p].len + 1;
                st[clone].next = st[q].next;
                st[clone].link = st[q].link;
                st[clone].cnt = 0;
                
                while (p != -1 && st[p].next[c] == q) {
                    st[p].next[c] = clone;
                    p = st[p].link;
                }
                st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
    }

public:
    vector<long long> countOccurrences(const string& s, const vector<string>& queries) {
        st.clear();
        st.reserve(s.length() * 2 + 5);
        st.emplace_back(); // Root
        st[0].len = 0;
        st[0].link = -1;
        sz = 1;
        last = 0;
        
        for (char c : s) extend(c);
        
        // Propagate counts
        vector<int> nodes(sz);
        for (int i = 0; i < sz; i++) nodes[i] = i;
        sort(nodes.begin(), nodes.end(), [&](int a, int b) {
            return st[a].len > st[b].len;
        });
        
        for (int u : nodes) {
            if (u == 0) continue;
            if (st[u].link != -1) {
                st[st[u].link].cnt += st[u].cnt;
            }
        }
        
        vector<long long> ans;
        ans.reserve(queries.size());
        for (const string& q : queries) {
            int curr = 0;
            bool ok = true;
            for (char c : q) {
                if (st[curr].next.find(c) == st[curr].next.end()) {
                    ok = false;
                    break;
                }
                curr = st[curr].next[c];
            }
            if (ok) ans.push_back(st[curr].cnt);
            else ans.push_back(0);
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        int q;
        cin >> q;
        vector<string> queries(q);
        for (int i = 0; i < q; i++) {
            cin >> queries[i];
        }
        
        Solution solution;
        vector<long long> ans = solution.countOccurrences(s, queries);
        for (long long x : ans) cout << x << "\n";
    }
    return 0;
}
