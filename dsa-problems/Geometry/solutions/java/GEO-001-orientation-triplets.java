import java.util.*;
import java.io.*;

class Main {
static class Solution {
    public String orientation(long x1, long y1, long x2, long y2, long x3, long y3) {
        long cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
        if (cross == 0) return "collinear";
        return cross > 0 ? "counterclockwise" : "clockwise";
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        long x1 = sc.nextLong(); long y1 = sc.nextLong();
        long x2 = sc.nextLong(); long y2 = sc.nextLong();
        long x3 = sc.nextLong(); long y3 = sc.nextLong();
        System.out.println(new Solution().orientation(x1, y1, x2, y2, x3, y3));
    }
}
