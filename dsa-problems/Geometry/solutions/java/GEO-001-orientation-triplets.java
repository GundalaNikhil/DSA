class Solution {
    public String orientation(long x1, long y1, long x2, long y2, long x3, long y3) {
        long cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
        if (cross == 0) return "collinear";
        return cross > 0 ? "counterclockwise" : "clockwise";
    }
}
