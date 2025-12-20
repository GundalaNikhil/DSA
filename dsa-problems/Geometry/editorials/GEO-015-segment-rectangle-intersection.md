---
problem_id: GEO_SEGMENT_RECT_INTERSECT__5580
display_id: GEO-015
slug: segment-rectangle-intersection
title: "Segment-Rectangle Intersection"
difficulty: Medium
difficulty_score: 50
topics:
  - Computational Geometry
  - Segment Intersection
  - Axis-Aligned Rectangle
tags:
  - geometry
  - intersection
  - rectangle
  - medium
premium: true
subscription_tier: basic
---

# GEO-015: Segment-Rectangle Intersection

## 📋 Problem Summary

Given axis-aligned rectangle `[xL, yB]` to `[xR, yT]` and a segment `P1P2`, decide if the segment intersects or lies within the rectangle. Touching the boundary counts as intersection. Output `true` or `false`.

## 🌍 Real-World Scenario

**Scenario Title:** Collision Check Against Bounding Box**

A moving object follows a straight path `P1P2`. Before simulating full physics, you first test if the path hits the map’s bounding box. If not, you can skip expensive checks.

**Why This Problem Matters:**

- Core primitive for clipping, collision detection, and line-of-sight checks.
- Combines point-in-rectangle test with robust segment intersection against rectangle edges.

## ASCII Visual

```
Rect:
 (xL,yT) ●-------● (xR,yT)
         |       |
         |       |
 (xL,yB) ●-------● (xR,yB)

Segment crossing any edge or lying inside → true
```

## Detailed Explanation

Intersection occurs if:

1. Either endpoint is inside the rectangle, **or**
2. The segment intersects any of the 4 rectangle edges.

Use orientation and on-segment tests for robust intersection.

### Point Inside Rectangle

`xL <= x <= xR` and `yB <= y <= yT`.

### Segment-Segment Intersection

For segments `ab` and `cd`, they intersect if:
- `orient(a,b,c)` and `orient(a,b,d)` have opposite signs, and `orient(c,d,a)` and `orient(c,d,b)` have opposite signs, **or**
- Any point is collinear and lies on the other segment (on-segment check).

Orientation: `cross = (bx-ax)*(cy-ay) - (by-ay)*(cx-ax)`; use 64-bit.

### Rectangle Edges

Edges: `(xL,yB)-(xR,yB)`, `(xR,yB)-(xR,yT)`, `(xR,yT)-(xL,yT)`, `(xL,yT)-(xL,yB)`.

## Input/Output Clarifications

- Rectangle sides inclusive.
- Output lowercase `true`/`false`.
- Segment endpoints distinct.

## Naive Approach

**Algorithm:** Check inside, else test intersection with each edge.  
**Time:** `O(1)`  
**Space:** `O(1)`

## Optimal Approach

Same as naive; only constant work needed.

## Reference Implementations

### Python

```python
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
```

### Java

```java
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
```

## Common Mistakes to Avoid

1. **Bounding box only.** Overlapping bounding boxes isn’t sufficient; must test edge intersections.
2. **Excluding boundary.** Touching edges counts; include `<=` in checks.
3. **Overflow in orientation.** Use 64-bit for cross products.
4. **Zero-length segment.** Not in constraints (distinct endpoints), but guarding is fine.

## Complexity Analysis

- **Time:** `O(1)`  
- **Space:** `O(1)`

## Testing Strategy

- Segment completely inside → true.
- Segment completely outside and disjoint → false.
- Segment crossing one edge → true.
- Segment passing through a corner → true.
- Vertical/horizontal segments; large coordinates for overflow checks.

## ASCII Recap

```
Inside? yes → true
Else: test vs 4 edges with segment intersection
```
