# Longest Substring Without Repeating Characters (LeetCode 3)
def length_of_longest_substring(s: str) -> int:
    seen = {}
    start = 0
    max_len = 0
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        max_len = max(max_len, i - start + 1)
    return max_len

if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
