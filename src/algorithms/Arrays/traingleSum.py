

def largestTriangleArea(points):
        n = len(points)
        max_area = 0

        for a in range(n):
            ax, ay = points[a][0], points[a][1]
            for b in range(a+1, n):
                bx, by = points[b][0], points[b][1]
                diff_ay_by = ay - by
                for c in range(b+1, n):
                    cx, cy = points[c][0], points[c][1]
                    #area = abs((ax*(by - cy) + bx*(cy - ay) + cx*(ay - by))/2)
                    area = abs((ax*(by - cy) + bx*(cy - ay) + cx*diff_ay_by)/2)
                    max_area = max(area, max_area)

        return max_area
      
