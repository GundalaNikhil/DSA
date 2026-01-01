import java.util.*;
import java.io.*;

class Main {
class Solution {
    private int orient(long ax,long ay,long bx,long by,long cx,long cy){
        long v = (bx-ax)*(cy-ay) - (by-ay)*(cx-ax);
        return Long.compare(v,0);
    }
    private boolean onSeg(long ax,long ay,long bx,long by,long cx,long cy){
        return orient(ax,ay,bx,by,cx,cy)==0 &&
               Math.min(ax,bx)<=cx && cx<=Math.max(ax,bx) &&
               Math.min(ay,by)<=cy && cy<=Math.max(ay,by);
    }
    private boolean segInter(long ax,long ay,long bx,long by,long cx,long cy,long dx,long dy){
        int o1=orient(ax,ay,bx,by,cx,cy), o2=orient(ax,ay,bx,by,dx,dy);
        int o3=orient(cx,cy,dx,dy,ax,ay), o4=orient(cx,cy,dx,dy,bx,by);
        if (o1==0 && onSeg(ax,ay,bx,by,cx,cy)) return true;
        if (o2==0 && onSeg(ax,ay,bx,by,dx,dy)) return true;
        if (o3==0 && onSeg(cx,cy,dx,dy,ax,ay)) return true;
        if (o4==0 && onSeg(cx,cy,dx,dy,bx,by)) return true;
        return (long)o1*o2 < 0 && (long)o3*o4 < 0;
    }
    public boolean intersects(long xL, long yB, long xR, long yT, long x1, long y1, long x2, long y2) {
        boolean inside1 = (xL <= x1 && x1 <= xR && yB <= y1 && y1 <= yT);
        boolean inside2 = (xL <= x2 && x2 <= xR && yB <= y2 && y2 <= yT);
        if (inside1 || inside2) return true;
        long[][] edges = {{xL,yB,xR,yB},{xR,yB,xR,yT},{xR,yT,xL,yT},{xL,yT,xL,yB}};
        for (long[] e: edges) {
            if (segInter(x1,y1,x2,y2,e[0],e[1],e[2],e[3])) return true;
        }
        return false;
    }
}

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNext()) return;
        long xL = sc.nextLong(); long yB = sc.nextLong();
        long xR = sc.nextLong(); long yT = sc.nextLong();
        long x1 = sc.nextLong(); long y1 = sc.nextLong();
        long x2 = sc.nextLong(); long y2 = sc.nextLong();
        System.out.println(new Solution().intersects(xL, yB, xR, yT, x1, y1, x2, y2) ? "true" : "false");
    }
}
