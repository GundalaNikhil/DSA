#include <bits/stdc++.h>
using namespace std;
const double EPS = 1e-9;
struct Line {
    double ang, a, b, c;
};

pair<double,double> intersect(const Line& L1, const Line& L2) {
    double det = L1.a * L2.b - L2.a * L1.b;
    return {(L1.c * L2.b - L2.c * L1.b) / det,
            (L1.a * L2.c - L2.a * L1.c) / det};
}

bool outside(const pair<double,double>& p, const Line& L) {
    return L.a * p.first + L.b * p.second - L.c > EPS;
}

vector<pair<double,double>> halfPlaneIntersection(const vector<long long>& A, const vector<long long>& B, const vector<long long>& C) {
    int m = A.size();
    vector<Line> L;
    L.reserve(m);
    for (int i = 0; i < m; ++i) {
        Line ln; ln.a = A[i]; ln.b = B[i]; ln.c = C[i];
        ln.ang = atan2(ln.b, ln.a);
        L.push_back(ln);
    }
    sort(L.begin(), L.end(), [](const Line& x, const Line& y){
        if (fabs(x.ang - y.ang) > EPS) return x.ang < y.ang;
        return x.c / hypot(x.a, x.b) < y.c / hypot(y.a, y.b);
    });
    vector<Line> uniq;
    for (auto &ln : L) {
        if (!uniq.empty() && fabs(ln.ang - uniq.back().ang) < EPS) {
            // keep tighter
            if (ln.c / hypot(ln.a, ln.b) < uniq.back().c / hypot(uniq.back().a, uniq.back().b))
                uniq.back() = ln;
        } else uniq.push_back(ln);
    }
    deque<Line> dq;
    for (auto &ln : uniq) {
        while (dq.size() >= 2 && outside(intersect(dq[dq.size()-2], dq.back()), ln)) dq.pop_back();
        while (dq.size() >= 2 && outside(intersect(dq[0], dq[1]), ln)) dq.pop_front();
        dq.push_back(ln);
    }
    while (dq.size() >= 3 && outside(intersect(dq[dq.size()-2], dq.back()), dq[0])) dq.pop_back();
    while (dq.size() >= 3 && outside(intersect(dq[0], dq[1]), dq.back())) dq.pop_front();
    if (dq.size() < 2) return {};
    vector<pair<double,double>> poly;
    for (int i = 0; i < (int)dq.size(); ++i) {
        poly.push_back(intersect(dq[i], dq[(i+1)%dq.size()]));
    }
    int idx = min_element(poly.begin(), poly.end(), [](auto &p1, auto &p2){
        if (fabs(p1.first - p2.first) > EPS) return p1.first < p2.first;
        return p1.second < p2.second;
    }) - poly.begin();
    rotate(poly.begin(), poly.begin()+idx, poly.end());
    return poly;
}
