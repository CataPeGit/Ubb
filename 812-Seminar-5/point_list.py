def distance(point_list, i, j):
    """
    1 - ex a
    Input: a list containing coordinates of points and two indexes
    Computes the distance between the points corresponding to the given indexes
    Returns the computed distance
    """
    if 0 <= i < len(point_list) and 0 <= j < len(point_list):
        d = ((point_list[i][0] - point_list[j][0])**2 + (point_list[i][1] - point_list[j][1])**2)**(1/2)
        return d
    else:
        raise IndexError('Indices out of the range')


def increase_x(point_list, value):
    """
    1 - ex b
    Input: list of point and a value
    Increases the x coordinated by value
    Returns the list with increased x coordinates
    """
    for point in point_list:
        point[0] += value
    return point_list


def get_first(element):
    """
    Get first element of a list.
    :param element:
    :return:
    """
    return element[0]


def k_closest(point_list, i, k):
    """
    1 - ex c
    :param point_list: list containing our points
    :param i: index of the element within the list, we calculate the dist from
    :param k: the number of distances we want to compute
    :return: a list of k closest points
    """
    if not 0 <= i < len(point_list):
        raise IndexError

    distance_list = []
    for j in range(len(point_list)):
        if j != i:
            distance_list.append([distance(point_list, i, j), j])
    distance_list.sort(key=get_first)
    # distance_list = sorted(distance_list, key=get_first)
    if len(distance_list) >= k > 0:
        value_list = []
        for dist in distance_list[:k]:
            value_list.append(point_list[dist[1]])
        return value_list
    else:
        raise ValueError


def highest_distance(point_list):
    """
    1 - ex d
    :param point_list: list of points
    :return: highest distance between any 2 points
    """

    highest_dist = None
    for i in range(len(point_list)):
        for j in range(i + 1, len(point_list)):
            curr_dist = distance(point_list, i, j)
            if highest_dist is None or highest_dist < curr_dist:
                highest_dist = curr_dist
    return highest_dist


def same_color_distance(point_list, i, j):
    """
    1 - ex a
    Input: a list containing coordinates of points and two indexes
    Computes the distance between the points corresponding to the given indexes
    Returns the computed distance
    """
    if not (0 <= i < len(point_list) and 0 <= j < len(point_list)):
        raise IndexError('Indices out of the range')
    if point_list[i][2] != point_list[j][2]:
        raise ValueError('The points have different color!')

    return distance(point_list, i, j)


def filter_color(point_list, i):
    """
    Returns points with a specified color.
    :param point_list: list of points
    :param i: index of point
    :return:
    """
    same_color = [point_list[i]]
    for j in range(len(point_list)):
        if point_list[j][2] == point_list[i][2] and j != i:
            same_color.append(point_list[j])
    return same_color


def same_color_k_closest(point_list, i, k):
    """
    Getting the k closest point with the same color as point a index i
    :param point_list: list of points
    :param i: index of the point
    :param k: number of neighbours
    :return: k closest neighbours to point at index i with the same color
    :raises IndexError: if i is out of range
    :raises ValueError: in cases defined in k_closest
    """
    if not 0 <= i < len(point_list):
        raise IndexError

    same_color = filter_color(point_list, point_list[i][2])
    return k_closest(same_color, 0, k)


def write_file(point_list, filename):
    """
    Write the list of points to a file.
    :param point_list: list of points
    :param filename: name of the file
    """
    f = open(filename, 'w')

    for point in point_list:
        f.write(f'({point[0]}, {point[1]}) - {point[2]}\n')

    f.close()


def read_file(filename):
    """
    Read the list of points from a file. The data's format should be the same as in the write function.
    :param filename: name of the file
    :return list of points
    """
    f = open(filename, 'r')

    point_list = []
    for line in f:
        line = line[1:]
        comma_split = line.split(", ")
        brace_split = comma_split[1].split(") - ")
        point_list.append([int(comma_split[0]), int(brace_split[0]), brace_split[1][:-1]])

    f.close()
    return point_list

