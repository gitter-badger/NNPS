
def uniform_cube(N):
    '''
    N^3 is the number of points
    '''
    points = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                points.append([i,j,k])

    return points

def two_dimensional_square(N):
    points = []
    for i in range(N):
        for j in range(N):
            points.append([i,j,0])

    return points
