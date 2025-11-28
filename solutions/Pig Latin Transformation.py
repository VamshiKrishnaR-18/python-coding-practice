def piglatin(word: str) -> str:
    vowels = "aeiouAEIOU"
    fv = -1  # first vowel index

    # 1. find first vowel
    for i, ch in enumerate(word):
        if ch in vowels:
            fv = i
            break

    # 2. no vowel case
    if fv == -1:
        return word + "ay"

    # 3. normal cases
    before = word[:fv]      # consonants before vowel
    after = word[fv:]       # from vowel to end

    return after + before + "ay"


if __name__ == "__main__":
    s = input().strip()
    print(piglatin(s))
