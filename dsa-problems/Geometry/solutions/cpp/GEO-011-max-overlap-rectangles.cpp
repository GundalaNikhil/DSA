#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;

// Same sweep; compress ys; segment tree supports range add and tracks max at root.

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int m; cin >> m;
    vector<long long> x1(m), y1(m), x2(m), y2(m);
    for(int i=0; i<m; i++) cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
    cout << maxOverlap(x1, y1, x2, y2) << endl;
    return 0;
}
