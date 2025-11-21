# Container With Most Water (LeetCode 11)
def max_area(height):
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        width = r - l
        area = min(height[l], height[r]) * width
        best = max(best, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best

if __name__ == "__main__":
    print(max_area([1,8,6,2,5,4,8,3,7]))  # 49
