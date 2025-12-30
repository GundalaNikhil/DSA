function orientation(x1, y1, x2, y2, x3, y3) {
  const cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
  if (cross === 0) return "collinear";
  return cross > 0 ? "counterclockwise" : "clockwise";
}
