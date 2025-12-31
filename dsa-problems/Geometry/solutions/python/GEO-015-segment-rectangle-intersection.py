def intersects(xL, yB, xR, yT, x1, y1, x2, y2) -> bool:
    # 1. Bounding box check (fast reject)
    if min(x1, x2) > xR or max(x1, x2) < xL or min(y1, y2) > yT or max(y1, y2) < yB:
        return False
        
    # 2. Check if either endpoint is inside (fast accept)
    if xL <= x1 <= xR and yB <= y1 <= yT: return True
    if xL <= x2 <= xR and yB <= y2 <= yT: return True
    
    # 3. Check intersection with 4 diagonals using integer cross product
    # Segment P1-P2. Rectangle lines: x=xL, x=xR, y=yB, y=yT.
    # Logic: If segment straddles a line AND intersects within range.
    
    # Check intersection with vertical lines x=xL and x=xR
    # Intersection y = y1 + (y2-y1)*(x_line - x1)/(x2-x1)
    # Check if yB <= y <= yT <=> yB <= num/den <= yT
    # care with signs
    if x1 != x2:
        # Check xL
        if min(x1, x2) <= xL <= max(x1, x2):
            num = y1 * (x2 - x1) + (y2 - y1) * (xL - x1)
            den = x2 - x1
            val_num = num
            val_den = den
            # Check yB <= val <= yT.
            # yB * den <= num <= yT * den (if den > 0)
            if den > 0:
                if yB * den <= num <= yT * den: return True
            else:
                if yT * den <= num <= yB * den: return True
                
        # Check xR
        if min(x1, x2) <= xR <= max(x1, x2):
            num = y1 * (x2 - x1) + (y2 - y1) * (xR - x1)
            den = x2 - x1
            if den > 0:
                if yB * den <= num <= yT * den: return True
            else:
                if yT * den <= num <= yB * den: return True

    if y1 != y2:
        # Check yB
        if min(y1, y2) <= yB <= max(y1, y2):
            # x = x1 + (x2-x1)*(yB-y1)/(y2-y1)
            num = x1 * (y2 - y1) + (x2 - x1) * (yB - y1)
            den = y2 - y1
            if den > 0:
                if xL * den <= num <= xR * den: return True
            else:
                if xR * den <= num <= xL * den: return True
                
        # Check yT
        if min(y1, y2) <= yT <= max(y1, y2):
            num = x1 * (y2 - y1) + (x2 - x1) * (yT - y1)
            den = y2 - y1
            if den > 0:
                if xL * den <= num <= xR * den: return True
            else:
                if xR * den <= num <= xL * den: return True
                
    return False

def main() -> None:
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 8:
        return
    xL, yB, xR, yT, x1, y1, x2, y2 = data[:8]
    val = intersects(xL, yB, xR, yT, x1, y1, x2, y2)
    print("true" if val else "false")

if __name__ == "__main__":
    main()
