#Points inside/outside polygon(Finished)

#Core principle: If the sum of the area of every three points including
#the point waited to be judged and two from the polygon, is the whole
#are of the polygon, then this point is in the polygon, otherwise, it is
#outside.

#calculate area  #refer to Shoelace formula
def calculateArea(points):
    [x1, y1] = points[0]
    [x2, y2] = points[1]
    [x3, y3] = points[2]

    return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)

#calculate polygon area   #refer to Shoelace formula
def polygonArea(points):
    area = 0
    q = points[-1]
    for p in points:
        area += p[0] * q[1] - p[1] * q[0]
        q = p
    return area / 2

#judge point
def pointJudge(apex,points):
    result = {}
    apexPair = [[apex[id],apex[id+1]] for id in range(len(apex)-1) ]
    apexPair.append([apex[-1],apex[0]])
    for point in points:
        if sum([calculateArea([point,ap[0],ap[1]]) for ap in apexPair]) == polygonArea(apex):
            result[str(point)] = True
        else:
            result[str(point)] = False
    print(result)


apex = [[4,3],[2,6],[3,12],[2,17],[5,20],[9,21],[14,19],[20,14],[18,3],[11,7]]
points = [[7,11],[10,14],[11,4],[12,21],[16,3],[16,10],[17,4],[18,7],[18,17],[20,7]]
pointJudge(apex,points)