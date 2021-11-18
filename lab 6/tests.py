from classes import *

# we will test our functions using the following points and repository

repository_test = PointRepository()

point1 = MyPoint(1, 2, "red")
point2 = MyPoint(4, 1, "green")
point3 = MyPoint(2, 7, "blue")

repository_test.add_point(point1)
repository_test.add_point(point2)
repository_test.add_point(point3)


def run_tests():
    """
    Run all test
    """

    test_add_point()
    test_get_all_points()
    test_get_point_at_index()
    test_update_point_given_index()
    test_delete_point_at_index()
    reset_repository()
    print(repository_test.get_all_points())


def test_add_point():
    # current test repository has 3 points
    # so the number of points will be modified when adding a new one
    repository_test.add_point(MyPoint(3, 3, "yellow"))
    all_points = repository_test.get_all_points()
    assert len(all_points) == 4

    repository_test.add_point(MyPoint(1, 4, "orange"))
    all_points = repository_test.get_all_points()
    assert len(all_points) == 5

    repository_test.add_point(MyPoint(23, 56, "purple"))
    all_points = repository_test.get_all_points()
    assert len(all_points) == 6


def test_get_all_points():
    # repository currently has 6 points
    all_points = repository_test.get_all_points()

    point = all_points[0]
    assert point.getValueY() == 2
    assert point.getColor() == "red"

    point = all_points[1]
    assert point.getValueY() == 1
    assert point.getValueX() == 4

    point = all_points[2]
    assert point.getValueX() == 2
    assert point.getColor() == "blue"


def test_get_point_at_index():
    # testing values of the point at a given index
    test1 = repository_test.get_point_at_index(2)
    assert test1.getValueX() == 2
    test2 = repository_test.get_point_at_index(1)
    assert test2.getValueY() == 1
    test3 = repository_test.get_point_at_index(0)
    assert test3.getColor() == "red"


def test_update_point_given_index():
    # we will update the point and check if the changes happened
    repository_test.update_point_at_index(0, 1, 2, "pink")
    point = repository_test.get_point_at_index(0)
    assert point.getColor() == "pink"

    repository_test.update_point_at_index(4, 12, 43, "cyan")
    point = repository_test.get_point_at_index(4)
    assert point.getValueX() == 12

    repository_test.update_point_at_index(0, 1, 8, "indigo")
    point = repository_test.get_point_at_index(0)
    assert point.getValueY() == 8


def test_delete_point_at_index():
    # reset the repository in order to use the 3 test points
    """
    point1 = MyPoint(1, 2, "red")
    point2 = MyPoint(4, 1, "green")
    point3 = MyPoint(2, 7, "blue")
    """
    repository_test.delete_point_at_index(0)
    point = repository_test.get_point_at_index(0)
    assert point.getValueX() == 4

    repository_test.delete_point_at_index(0)
    point = repository_test.get_point_at_index(0)
    assert point.getValueY() == 7
    assert point.getColor() == "blue"


def reset_repository():
    # reseting repository for eventual upcoming tests
    point1 = MyPoint(1, 2, "red")
    point2 = MyPoint(4, 1, "green")
    point3 = MyPoint(2, 7, "blue")

    repository_test.delete_point_at_index(0)
    repository_test.delete_point_at_index(0)
    repository_test.delete_point_at_index(0)
    repository_test.delete_point_at_index(0)

    repository_test.add_point(point1)
    repository_test.add_point(point2)
    repository_test.add_point(point3)
