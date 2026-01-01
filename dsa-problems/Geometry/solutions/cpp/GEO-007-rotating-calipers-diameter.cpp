#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;


using namespace std;

long long diameterSquared(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    auto cross = [&](int a, int b, int c)->long long{
        return (xs[b]-xs[a])*(ys[c]-ys[a]) - (ys[b]-ys[a])*(xs[c]-xs[a]);
    };
    auto dist2 = [&](int a, int b)->long long{
        long long dx = xs[a]-xs[b], dy = ys[a]-ys[b];
        return dx*dx + dy*dy;
    };
    long long best = 0;
    int j = 1;
    for (int i = 0; i < n; ++i) {
        int ni = (i+1)%n;
        while (cross(i, ni, (j+1)%n) > cross(i, ni, j)) j = (j+1)%n;
        best = max(best, dist2(i, j));
        best = max(best, dist2(ni, j));
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];
    cout << diameter(xs, ys) << endl;
    return 0;
}
