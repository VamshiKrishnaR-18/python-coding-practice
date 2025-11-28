def seplic(strs: str) -> str:
    # 1. keep only alphanumeric chars
    valid = [ch.upper() for ch in strs if ch.isalnum()]

    n = len(valid)

    # 2. length check
    if n < 2 or n > 10:
        return "INVALID"

    # 3. must contain at least one digit
    if not any(ch.isdigit() for ch in valid):
        return "INVALID"

    # 4. determine group sizes
    if n % 3 == 0:
        sizes = [3] * (n // 3)

    elif n % 3 == 1:
        num3 = (n - 4) // 3
        sizes = [3] * num3 + [2, 2]

    else:  # n % 3 == 2
        num3 = n // 3
        sizes = [3] * num3 + [2]

    # 5. slice into groups (correct slicing)
    groups = []
    i = 0
    for sz in sizes:
        group = "".join(valid[i:i + sz])
        groups.append(group)
        i += sz

    # 6. join with hyphens
    return "-".join(groups)


if __name__ == "__main__":
    s = input().strip()
    print(seplic(s))
