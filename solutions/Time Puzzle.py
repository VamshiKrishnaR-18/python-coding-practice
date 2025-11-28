def calc_min_max(st):
    def isvalid(c: str) -> bool:
        hh = int(c[0:2])
        mm = int(c[3:5])
        ss = int(c[6:8])
        return 0 <= hh <= 23 and 0 <= mm <= 59 and 0 <= ss <= 59

    possible = []
    min_time = None
    max_time = None

    for d in "0123456789":
        candidate = st.replace("@", d)

        if isvalid(candidate):
            possible.append(d)

            if min_time is None or candidate < min_time:
                min_time = candidate

            if max_time is None or candidate > max_time:
                max_time = candidate

    print(" ".join(possible))
    print(min_time)
    print(max_time)


if __name__ == "__main__":
    s = input().strip()
    calc_min_max(s)
