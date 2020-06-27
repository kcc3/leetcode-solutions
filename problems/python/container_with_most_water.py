def max_area(height: list) -> int:
    """Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
    lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with
    x-axis forms a container, such that the container contains the most water.

    Solve:
        We use the two pointer approach where we start from the front and back of the list, and iterate towards the
        center, stepping based on the lower height so we're always looking for the maximized area when we are stepping

    Args:
        height (list): Array of heights

    Returns:
        int: The maximum area container we can create
    """
    area = 0
    front = 0
    back = len(height) - 1
    while front != back:
        area = max(area, min(height[front], height[back]) * (back - front))
        if height[front] > height[back]:
            back -= 1
        else:
            front += 1
    return area


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
