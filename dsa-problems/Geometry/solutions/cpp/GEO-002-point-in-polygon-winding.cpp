#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;


using namespace std;

string classifyPoint(const vector<long long>& xs, const vector<long long>& ys, long long qx, long long qy) {
    int n = xs.size();
    int wn = 0;
    for (int i = 0; i < n; ++i) {
        int j = (i + 1) % n;
        long long xi = xs[i], yi = ys[i], xj = xs[j], yj = ys[j];
        long long cross = (xj - xi) * (qy - yi) - (yj - yi) * (qx - xi);
        if (cross == 0 && min(xi, xj) <= qx && qx <= max(xi, xj) && min(yi, yj) <= qy && qy <= max(yi, yj))
            return "boundary";
        if (yi <= qy && yj > qy && cross > 0) wn++;
        else if (yi > qy && yj <= qy && cross < 0) wn--;
    }
    return wn != 0 ? "inside" : "outside";
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];
    long long qx, qy; cin >> qx >> qy;
    cout << pointInPolygon(n, xs, ys, qx, qy) << endl;
    return 0;
}
