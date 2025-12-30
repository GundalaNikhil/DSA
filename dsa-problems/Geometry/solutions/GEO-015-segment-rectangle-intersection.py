def intersects(xL, yB, xR, yT, x1, y1, x2, y2) -> bool:
    def inside(x,y):
        return xL <= x <= xR and yB <= y <= yT
    def orient(ax,ay,bx,by,cx,cy):
        v = (bx-ax)*(cy-ay) - (by-ay)*(cx-ax)
        return (v>0) - (v<0)
    def on_seg(ax,ay,bx,by,cx,cy):
        return orient(ax,ay,bx,by,cx,cy)==0 and min(ax,bx)<=cx<=max(ax,bx) and min(ay,by)<=cy<=max(ay,by)
    def seg_inter(a,b,c,d):
        o1=orient(*a,*b,*c); o2=orient(*a,*b,*d); o3=orient(*c,*d,*a); o4=orient(*c,*d,*b)
        if o1==0 and on_seg(*a,*b,*c): return True
        if o2==0 and on_seg(*a,*b,*d): return True
        if o3==0 and on_seg(*c,*d,*a): return True
        if o4==0 and on_seg(*c,*d,*b): return True
        return o1*o2<0 and o3*o4<0
    if inside(x1,y1) or inside(x2,y2): return True
    rect_edges = [((xL,yB),(xR,yB)), ((xR,yB),(xR,yT)), ((xR,yT),(xL,yT)), ((xL,yT),(xL,yB))]
    a=(x1,y1); b=(x2,y2)
    return any(seg_inter(a,b,e1,e2) for e1,e2 in rect_edges)


def main():
    import sys
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # TODO: Parse input and call solution
    pass

if __name__ == "__main__":
    main()
