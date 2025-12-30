#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>

using namespace std;

const double PI = acos(-1);
const int MOD = 1000000007;

using cd = complex<double>;

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * PI / len * (invert ? -1 : 1);
        cd wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1);
            for (int j = 0; j < len / 2; j++) {
                cd u = a[i+j], v = a[i+j+len/2] * w;
                a[i+j] = u + v;
                a[i+j+len/2] = u - v;
                w *= wlen;
            }
        }
    }
    if (invert) {
        for (cd & x : a) x /= n;
    }
}

class Solution {
public:
    vector<long long> multiplyPolynomials(vector<long long>& A, vector<long long>& B) {
        int n = 1;
        while (n < A.size() + B.size()) n <<= 1;
        
        int S = 32000;
        vector<cd> a0(n), a1(n), b0(n), b1(n);
        
        for(int i=0; i<A.size(); i++) {
            a0[i] = cd(A[i] % S, 0);
            a1[i] = cd(A[i] / S, 0);
        }
        for(int i=0; i<B.size(); i++) {
            b0[i] = cd(B[i] % S, 0);
            b1[i] = cd(B[i] / S, 0);
        }
        
        fft(a0, false); fft(a1, false);
        fft(b0, false); fft(b1, false);
        
        vector<cd> c0(n), c1(n), c2(n);
        for(int i=0; i<n; i++) {
            c0[i] = a0[i] * b0[i];
            c2[i] = a1[i] * b1[i];
            c1[i] = (a0[i] + a1[i]) * (b0[i] + b1[i]) - c0[i] - c2[i];
        }
        
        fft(c0, true); fft(c1, true); fft(c2, true);
        
        vector<long long> res(A.size() + B.size() - 1);
        for(int i=0; i<res.size(); i++) {
            long long v0 = (long long)(c0[i].real() + 0.5) % MOD;
            long long v1 = (long long)(c1[i].real() + 0.5) % MOD;
            long long v2 = (long long)(c2[i].real() + 0.5) % MOD;
            
            res[i] = (v2 * S % MOD * S % MOD + v1 * S % MOD + v0) % MOD;
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    int m;
    cin >> m;
    vector<long long> B(m);
    for (int i = 0; i < m; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.multiplyPolynomials(A, B);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i < result.size() - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
