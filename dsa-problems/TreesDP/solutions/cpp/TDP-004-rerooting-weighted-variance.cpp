#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

const int MAXN = 200005;
vector<int> graph[MAXN];
long long weight[MAXN];
long long subtreeWeight[MAXN];
long long down[MAXN];
long long up[MAXN];
long long totalWeight = 0;
int n;

void dfsDown(int u, int parent) {
    subtreeWeight[u] = weight[u];
    down[u] = 0;

    for (int v : graph[u]) {
        if (v == parent) continue;

        dfsDown(v, u);

        long long childContribution = down[v] +
                                     2LL * subtreeWeight[v] +
                                     subtreeWeight[v];
        down[u] += childContribution;
        subtreeWeight[u] += subtreeWeight[v];
    }
}

void dfsUp(int u, int parent) {
    if (parent != -1) {
        long long outsideWeight = totalWeight - subtreeWeight[u];

        long long parentTotalDown = down[parent];
        long long uContribution = down[u] + 2LL * subtreeWeight[u] + subtreeWeight[u];
        long long parentDownWithoutU = parentTotalDown - uContribution;

        up[u] = up[parent] + parentDownWithoutU +
               2LL * outsideWeight + outsideWeight;
    }

    for (int v : graph[u]) {
        if (v == parent) continue;
        dfsUp(v, u);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> weight[i];
        totalWeight += weight[i];
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    dfsDown(1, -1);
    dfsUp(1, -1);

    long long minCost = LLONG_MAX;
    int bestNode = 1;

    for (int i = 1; i <= n; i++) {
        long long totalCost = down[i] + up[i];
        if (totalCost < minCost) {
            minCost = totalCost;
            bestNode = i;
        }
    }

    cout << bestNode << endl;

    return 0;
}
