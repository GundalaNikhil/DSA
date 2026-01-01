#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;

long long polygonArea(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        int j = (i + 1) % n;
        sum += xs[i] * ys[j] - xs[j] * ys[i];
    }
    return llabs(sum) / 2;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<long long> xs(n), ys(n);
    for(int i=0; i<n; i++) cin >> xs[i] >> ys[i];
    cout << polygonArea(xs, ys) << endl;
    return 0;
}
