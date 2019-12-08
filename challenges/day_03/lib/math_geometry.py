def intersect(line1, line2):

    print(line1)
    print(line2)

    x1 = line1[0][0]
    y1 = line1[0][1]
    x2 = line1[1][0]
    y2 = line1[1][1]

    x3 = line2[0][0]
    y3 = line2[0][1]
    x4 = line2[1][0]
    y4 = line2[1][1]

    xi = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / \
        ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))

    yi = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / \
        ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))

    return [int(xi), int(yi)]
