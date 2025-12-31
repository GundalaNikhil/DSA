#include <iostream>

using namespace std;

class Solution {
    long long power(long long base, long long exp, int mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }

public:
    long long factorialMissingPrime(long long n, int p) {
        long long numBlocks = n / p;
        long long remainder = n % p;
        
        long long res = power(p - 1, numBlocks, p);
        
        long long remFact = 1;
        for (int i = 1; i <= remainder; i++) {
            remFact = (remFact * i) % p;
        }
        
        return (res * remFact) % p;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int p;
    if (cin >> n >> p) {
        Solution solution;
        cout << solution.factorialMissingPrime(n, p) << "\n";
    }
    return 0;
}
