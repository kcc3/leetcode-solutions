def lengthOfLongestSubstring(s: str) -> int:
    letters = {}
    count = 0
    longest = 0
    for i in range(len(s)):
        # If we hit a character that repeats
        if s[i] in letters:
            if longest < count:
                longest = count
            count = 1
            letters.clear()
            letters[s[i]] = 1
        else:
            count += 1
            letters[s[i]] = 1
    # If the substring is at the end of the string, make sure that case is caught
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