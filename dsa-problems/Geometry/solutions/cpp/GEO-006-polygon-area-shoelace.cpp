long long polygonArea(const vector<long long>& xs, const vector<long long>& ys) {
    int n = xs.size();
    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        int j = (i + 1) % n;
        sum += xs[i] * ys[j] - xs[j] * ys[i];
    }
    return llabs(sum) / 2;
}
