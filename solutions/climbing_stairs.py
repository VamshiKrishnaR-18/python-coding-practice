# Climbing Stairs (LeetCode 70)
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    print(climb_stairs(5))  # 8
