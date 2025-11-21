# Reverse Integer (LeetCode 7)
def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0
    while x:
        rev = rev * 10 + x % 10
        x //= 10
    rev *= sign
    # 32-bit signed integer overflow check
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev

if __name__ == "__main__":
    print(reverse(123))   # 321
    print(reverse(-120))  # -21
