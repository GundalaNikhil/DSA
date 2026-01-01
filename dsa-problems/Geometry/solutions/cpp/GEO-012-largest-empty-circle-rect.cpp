#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <random>

using namespace std;

const double EPS = 1e-12;
const double PI = acos(-1.0);

struct Point {
    double x, y;
};

double distSq(double x1, double y1, double x2, double y2) {
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}

double getRadius(double x, double y, int xL, int yB, int xR, int yT, const vector<Point>& pts) {
    if (x < xL || x > xR || y < yB || y > yT) return 0.0;
    
    double r = min({x - xL, (double)xR - x, y - yB, (double)yT - y});
    if (r <= EPS) return 0.0;
    
    double min_d2 = 1e18;
    for (const auto& p : pts) {
        double d2 = distSq(x, y, p.x, p.y);
        min_d2 = min(min_d2, d2);
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
    
    vector<Point> candidates;
    candidates.push_back({(double)(xL + xR) / 2.0, (double)(yB + yT) / 2.0});
    
    for (const auto& p : pts) {
        candidates.push_back({p.x, (double)(p.y + yB) / 2.0});
        candidates.push_back({p.x, (double)(p.y + yT) / 2.0});
        candidates.push_back({(double)(p.x + xL) / 2.0, p.y});
        candidates.push_back({(double)(p.x + xR) / 2.0, p.y});
    }
    
    if (n <= 100) {
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                candidates.push_back({(pts[i].x + pts[j].x) / 2.0, (pts[i].y + pts[j].y) / 2.0});
            }
        }
    }

    int GRID = 12;
    for(int i=0; i<=GRID; ++i) {
        for(int j=0; j<=GRID; ++j) {
            double gx = xL + (double)(xR - xL) * i / GRID;
            double gy = yB + (double)(yT - yB) * j / GRID;
            candidates.push_back({gx, gy});
        }
    }
    
    vector<pair<double, int>> cand_scores;
    for (int i = 0; i < candidates.size(); ++i) {
        cand_scores.push_back({getRadius(candidates[i].x, candidates[i].y, xL, yB, xR, yT, pts), i});
    }
    sort(cand_scores.rbegin(), cand_scores.rend());
    
    vector<Point> starts;
    double best_r = 0.0;
    if (!cand_scores.empty()) best_r = cand_scores[0].first;
    
    for (int i = 0; i < min((int)candidates.size(), 40); ++i) {
        starts.push_back(candidates[cand_scores[i].second]);
    }
    
    mt19937 rng(1337);
    uniform_real_distribution<double> distAngle(0.0, 2 * PI);
    
    double step_size = max(xR - xL, yT - yB) / 2.0;
    double precision = 1e-7; 
    
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
            
            double angle = distAngle(rng);
            
            for (int k = 0; k < 8; ++k) {
                double a = angle + k * (PI / 4.0);
                double dx = cos(a);
                double dy = sin(a);
                
                double nx = curr_x + dx * temp_step;
                double ny = curr_y + dy * temp_step;
                
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
                temp_step *= 0.85; 
            }
        }
        best_r = max(best_r, curr_r);
    }
    
    cout << fixed << setprecision(6) << best_r << "\n";
    
    return 0;
}
