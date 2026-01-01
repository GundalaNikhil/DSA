#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;

// Same sweep; compress ys; segment tree with add[] and len[] storing length where sum>=W.

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int m, W; cin >> m >> W;
    vector<long long> x1(m), y1(m), x2(m), y2(m), w(m);
    for(int i=0; i<m; i++) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i] >> w[i];
    cout << weightedArea(x1, y1, x2, y2, w, W) << endl;
    return 0;
}
