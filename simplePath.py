

def simplePath(start, points):

    path = [start]

    for i in points:
        distx = abs(start[0] -  i[0])
        disty = abs(start[1] -  i[1])

        pathy = []
        pathx = []
        for y in range(disty):
            pathy.append((start[0],start[0]+(y+1)))
        for x in range(distx):
            pathx.append((start[0]+(y+1),start[0]+(x+1)))


        path = path + pathy + pathx
        pathy.reverse()
        pathx.reverse()
        path = path + pathx + pathy

    return path




points = [(2,2),(2,3)]
start = (0,0)
print(simplePath(start,points))
