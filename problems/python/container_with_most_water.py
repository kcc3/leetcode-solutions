def max_area(height: list) -> int:
    area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            cur_area = min(height[i], height[j]) * (j - i)
            area = max(cur_area, area)
    return area


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
