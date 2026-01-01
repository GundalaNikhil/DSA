import java.util.*;

class Main {
    private static int orient(long ax, long ay, long bx, long by, long cx, long cy) {
        long v = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
        if (v == 0) return 0;
        return (v > 0) ? 1 : -1;
    }

    private static boolean onSeg(long ax, long ay, long bx, long by, long cx, long cy) {
        return Math.min(ax, bx) <= cx && cx <= Math.max(ax, bx) &&
               Math.min(ay, by) <= cy && cy <= Math.max(ay, by);
    }

    public static boolean intersects(long[] s, long[] t) {
        int o1 = orient(s[0], s[1], s[2], s[3], t[0], t[1]);
        int o2 = orient(s[0], s[1], s[2], s[3], t[2], t[3]);
        int o3 = orient(t[0], t[1], t[2], t[3], s[0], s[1]);
        int o4 = orient(t[0], t[1], t[2], t[3], s[2], s[3]);

        if (((o1 > 0 && o2 < 0) || (o1 < 0 && o2 > 0)) &&
            ((o3 > 0 && o4 < 0) || (o3 < 0 && o4 > 0))) return true;

        if (o1 == 0 && onSeg(s[0], s[1], s[2], s[3], t[0], t[1])) return true;
        if (o2 == 0 && onSeg(s[0], s[1], s[2], s[3], t[2], t[3])) return true;
        if (o3 == 0 && onSeg(t[0], t[1], t[2], t[3], s[0], s[1])) return true;
        if (o4 == 0 && onSeg(t[0], t[1], t[2], t[3], s[2], s[3])) return true;

        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[][] segs = new long[n][4];
        for (int i = 0; i < n; i++) {
            segs[i][0] = sc.nextLong();
            segs[i][1] = sc.nextLong();
            segs[i][2] = sc.nextLong();
            segs[i][3] = sc.nextLong();
        }
        
        long count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (intersects(segs[i], segs[j])) count++;
            }
        }
        System.out.println(count);
        sc.close();
    }
}
