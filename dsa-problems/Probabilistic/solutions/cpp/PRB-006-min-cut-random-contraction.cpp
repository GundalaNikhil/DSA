#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <numeric>

using namespace std;

struct Edge {
    int u, v;
};

struct DSU {
    vector<int> parent;
    int components;

    DSU(int n) {
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
        components = n;
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }

    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            components--;
        }
    }
};

int kargerMinCut(int n, vector<Edge>& edges, mt19937& rng) {
    DSU dsu(n);
    vector<Edge> current_edges = edges;
    shuffle(current_edges.begin(), current_edges.end(), rng);

    for (const auto& edge : current_edges) {
        if (dsu.components <= 2) break;
        dsu.unite(edge.u, edge.v);
    }

    int cut_size = 0;
    for (const auto& edge : edges) {
        if (dsu.find(edge.u) != dsu.find(edge.v)) {
            cut_size++;
        }
    }
    return cut_size;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (cin >> n >> m) {
        vector<Edge> edges;
        for (int i = 0; i < m; ++i) {
            int u, v;
            cin >> u >> v;
            edges.push_back({u, v});
        }

        int trials;
        if (n <= 20) trials = 100;
        else trials = (int)(n * n * 0.5);

        // Seed with a fixed value or device if needed, but python uses random
        // Using a fixed seed ensures determinism across runs of this binary
        mt19937 rng(42); 

        int min_cut = m + 1;

        for (int i = 0; i < trials; ++i) {
            int cut = kargerMinCut(n, edges, rng);
            if (cut < min_cut) min_cut = cut;
        }

        cout << min_cut << "\n";
    }
    return 0;
}
