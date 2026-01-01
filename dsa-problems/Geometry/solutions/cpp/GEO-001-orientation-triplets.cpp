#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
using namespace std;

long long cross(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
}

string orientation(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
    long long c = cross(x1, y1, x2, y2, x3, y3);
    if (c == 0) return "collinear";
    return c > 0 ? "counterclockwise" : "clockwise";
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    long long x1,y1,x2,y2,x3,y3;
    if(cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3) cout << orientation(x1,y1,x2,y2,x3,y3) << endl;
    return 0;
}
