double distancePointSegment(long long x1, long long y1, long long x2, long long y2, long long px, long long py) {
    long long ux = x2 - x1, uy = y2 - y1;
    long long vx = px - x1, vy = py - y1;
    long long denom = ux*ux + uy*uy;
    if (denom == 0) return hypot((double)vx, (double)vy);
    double t = (ux * (double)vx + uy * (double)vy) / (double)denom;
    t = max(0.0, min(1.0, t));
    double cx = x1 + t * ux;
    double cy = y1 + t * uy;
    return hypot(px - cx, py - cy);
}
