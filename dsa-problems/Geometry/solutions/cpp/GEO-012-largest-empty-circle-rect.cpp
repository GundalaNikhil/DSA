#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <random>
#include <cstdint>

#pragma STDC FP_CONTRACT OFF

using namespace std;

const double EPS = 1e-12;

struct Point {
    double x, y;
};

struct PyRandom {
    static const int N = 624;
    static const int M = 397;
    static const uint32_t MATRIX_A = 0x9908b0dfU;
    static const uint32_t UPPER_MASK = 0x80000000U;
    static const uint32_t LOWER_MASK = 0x7fffffffU;

    uint32_t mt[N];
    int mti;

    PyRandom(uint32_t seed) { init_by_array(&seed, 1); }

    void init_genrand(uint32_t s) {
        mt[0] = s;
        for (mti = 1; mti < N; mti++) {
            mt[mti] = (1812433253U * (mt[mti - 1] ^ (mt[mti - 1] >> 30)) + (uint32_t)mti);
        }
    }

    void init_by_array(const uint32_t* init_key, int key_length) {
        init_genrand(19650218U);
        int i = 1;
        int j = 0;
        int k = (N > key_length ? N : key_length);
        for (; k; k--) {
            mt[i] = (mt[i] ^ ((mt[i - 1] ^ (mt[i - 1] >> 30)) * 1664525U)) + init_key[j] + (uint32_t)j;
            i++; j++;
            if (i >= N) { mt[0] = mt[N - 1]; i = 1; }
            if (j >= key_length) j = 0;
        }
        for (k = N - 1; k; k--) {
            mt[i] = (mt[i] ^ ((mt[i - 1] ^ (mt[i - 1] >> 30)) * 1566083941U)) - (uint32_t)i;
            i++;
            if (i >= N) { mt[0] = mt[N - 1]; i = 1; }
        }
        mt[0] = 0x80000000U;
    }

    uint32_t genrand_int32() {
        uint32_t y;
        static const uint32_t mag01[2] = {0x0U, MATRIX_A};
        if (mti >= N) {
            int kk;
            for (kk = 0; kk < N - M; kk++) {
                y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK);
                mt[kk] = mt[kk + M] ^ (y >> 1) ^ mag01[y & 0x1U];
            }
            for (; kk < N - 1; kk++) {
                y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK);
                mt[kk] = mt[kk + (M - N)] ^ (y >> 1) ^ mag01[y & 0x1U];
            }
            y = (mt[N - 1] & UPPER_MASK) | (mt[0] & LOWER_MASK);
            mt[N - 1] = mt[M - 1] ^ (y >> 1) ^ mag01[y & 0x1U];
            mti = 0;
        }
        y = mt[mti++];
        y ^= (y >> 11);
        y ^= (y << 7) & 0x9d2c5680U;
        y ^= (y << 15) & 0xefc60000U;
        y ^= (y >> 18);
        return y;
    }

    double random() {
        uint32_t a = genrand_int32() >> 5;
        uint32_t b = genrand_int32() >> 6;
        return (a * 67108864.0 + b) / 9007199254740992.0;
    }

    uint32_t getrandbits(int k) {
        if (k <= 0) return 0;
        return genrand_int32() >> (32 - k);
    }

    uint32_t randbelow(uint32_t n) {
        if (n <= 1) return 0;
        uint32_t t = n;
        int k = 0;
        while (t) { k++; t >>= 1; }
        uint32_t r;
        do { r = getrandbits(k); } while (r >= n);
        return r;
    }
};

double getRadius(double x, double y, int xL, int yB, int xR, int yT, const vector<Point>& pts) {
    if (x < xL || x > xR || y < yB || y > yT) return 0.0;
    double r = min(min(x - xL, (double)xR - x), min(y - yB, (double)yT - y));
    if (r <= EPS) return 0.0;
    double min_d2 = 1e18;
    for (const auto& p : pts) {
        double d2 = (x - p.x) * (x - p.x) + (y - p.y) * (y - p.y);
        if (d2 < min_d2) min_d2 = d2;
        if (d2 < r * r) return sqrt(d2);
    }
    return min(r, sqrt(min_d2));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int xL, yB, xR, yT;
    if (!(cin >> xL >> yB >> xR >> yT)) return 0;
    int n;
    cin >> n;
    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

    PyRandom rng(1337U);

    vector<Point> candidates;
    candidates.push_back({(xL + xR) / 2.0, (yB + yT) / 2.0});
    for (const auto& p : pts) {
        candidates.push_back({p.x, (p.y + yB) / 2.0});
        candidates.push_back({p.x, (p.y + yT) / 2.0});
        candidates.push_back({(p.x + xL) / 2.0, p.y});
        candidates.push_back({(p.x + xR) / 2.0, p.y});
    }
    if (n <= 100) {
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                candidates.push_back({(pts[i].x + pts[j].x) / 2.0, (pts[i].y + pts[j].y) / 2.0});
            }
        }
    }

    double best_r = 0.0;
    for (const auto& c : candidates) {
        best_r = max(best_r, getRadius(c.x, c.y, xL, yB, xR, yT, pts));
    }

    vector<Point> starts;
    starts.reserve(15);
    for (int i = 0; i < 10; ++i) {
        starts.push_back({xL + rng.random() * (xR - xL), yB + rng.random() * (yT - yB)});
    }
    if (!candidates.empty()) {
        struct Cand { double r; Point p; int idx; };
        vector<Cand> cand_scores;
        cand_scores.reserve(candidates.size());
        for (int i = 0; i < (int)candidates.size(); ++i) {
            const auto& c = candidates[i];
            cand_scores.push_back({getRadius(c.x, c.y, xL, yB, xR, yT, pts), c, i});
        }
        sort(cand_scores.begin(), cand_scores.end(), [](const Cand& a, const Cand& b) {
            if (a.r != b.r) return a.r > b.r;
            if (a.p.x != b.p.x) return a.p.x > b.p.x;
            if (a.p.y != b.p.y) return a.p.y > b.p.y;
            return a.idx < b.idx;
        });
        for (int i = 0; i < (int)cand_scores.size() && i < 5; ++i) {
            starts.push_back(cand_scores[i].p);
        }
    }

    double step_size = max(xR - xL, yT - yB) / 2.0;
    double precision = 1e-4;

    const vector<Point> base_dirs = {
        {0, 1}, {0, -1}, {1, 0}, {-1, 0},
        {0.7, 0.7}, {0.7, -0.7}, {-0.7, 0.7}, {-0.7, -0.7}
    };

    for (const auto& start : starts) {
        double curr_x = start.x;
        double curr_y = start.y;
        double curr_r = getRadius(curr_x, curr_y, xL, yB, xR, yT, pts);
        double temp_step = step_size;

        while (temp_step > precision) {
            bool improved = false;
            double best_neigh_r = curr_r;
            double best_neigh_x = curr_x;
            double best_neigh_y = curr_y;

            vector<Point> dirs = base_dirs;
            for (int i = (int)dirs.size() - 1; i > 0; --i) {
                int j = (int)rng.randbelow((uint32_t)(i + 1));
                swap(dirs[i], dirs[j]);
            }
            for (const auto& d : dirs) {
                double nx = curr_x + d.x * temp_step;
                double ny = curr_y + d.y * temp_step;
                nx = max((double)xL, min((double)xR, nx));
                ny = max((double)yB, min((double)yT, ny));
                double nr = getRadius(nx, ny, xL, yB, xR, yT, pts);
                if (nr > best_neigh_r) {
                    best_neigh_r = nr;
                    best_neigh_x = nx;
                    best_neigh_y = ny;
                    improved = true;
                }
            }
            if (improved) {
                curr_x = best_neigh_x;
                curr_y = best_neigh_y;
                curr_r = best_neigh_r;
            } else {
                temp_step *= 0.6;
            }
        }
        best_r = max(best_r, curr_r);
    }

    cout << fixed << setprecision(6) << best_r << "\n";
    return 0;
}
