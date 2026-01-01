#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Rect {
    int x1, y1, x2, y2, w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long targetW;
    if (!(cin >> n >> targetW)) return 0;

    vector<Rect> rects(n);
    vector<int> ux, uy;
    for (int i = 0; i < n; i++) {
        cin >> rects[i].x1 >> rects[i].y1 >> rects[i].x2 >> rects[i].y2 >> rects[i].w;
        ux.push_back(rects[i].x1);
        ux.push_back(rects[i].x2);
        uy.push_back(rects[i].y1);
        uy.push_back(rects[i].y2);
    }

    sort(ux.begin(), ux.end());
    ux.erase(unique(ux.begin(), ux.end()), ux.end());
    sort(uy.begin(), uy.end());
    uy.erase(unique(uy.begin(), uy.end()), uy.end());

    long long totalArea = 0;
    for (int i = 0; i + 1 < ux.size(); i++) {
        long long dx = (long long)ux[i + 1] - ux[i];
        if (dx <= 0) continue;

        vector<long long> yWeights(uy.size() - 1, 0);
        for (const auto& r : rects) {
            if (r.x1 <= ux[i] && r.x2 >= ux[i + 1]) {
                for (int j = 0; j + 1 < uy.size(); j++) {
                    if (r.y1 <= uy[j] && r.y2 >= uy[j + 1]) {
                        yWeights[j] += r.w;
                    }
                }
            }
        }

        long long dyCovered = 0;
        for (int j = 0; j + 1 < uy.size(); j++) {
            if (yWeights[j] >= targetW) {
                dyCovered += (long long)uy[j + 1] - uy[j];
            }
        }
        totalArea += dx * dyCovered;
    }

    cout << totalArea << endl;

    return 0;
}
