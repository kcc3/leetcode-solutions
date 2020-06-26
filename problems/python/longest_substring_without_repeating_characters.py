def lengthOfLongestSubstring(s: str) -> int:
    letters = {}
    count = 0
    longest = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            # If we hit a character that repeats
            if s[j] in letters:
                if longest < count:
                    longest = count
                count = 0
                letters.clear()
                break
            else:
                count += 1
                letters[s[j]] = 1
    if longest < count:
        longest = count
    return longest


if __name__ == "__main__":
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("abccbcbbacde") == 5
    assert lengthOfLongestSubstring("abccbailkmcbbacde") == 7
    assert lengthOfLongestSubstring("dvdf") == 3
    assert lengthOfLongestSubstring(" ") == 1