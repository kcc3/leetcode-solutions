def lengthOfLongestSubstring(s: str) -> int:
    """Given a string, find the length of the longest substring without repeating characters

    Solution:
        We use a window approach here so we can optimize and iterate just once through the list. When we find a repeat
        character, we keep the part of the substring that still remains unique, and just add the new letter and continue
        on. This way, we don't have to brute force from each position in the string.

    Args:
        s (str): the string to check

    Returns:
        int: the length of the longest substring in the string
    """
    letters = []
    longest = 0
    for st in s:
        if st in letters:
            # Keep the substring from the last time we see the repeat letter
            letters = letters[letters.index(st)+1:]
        letters.append(st)
        longest = max(longest, len(letters))
    return longest


if __name__ == "__main__":
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("abccbcbbacde") == 5
    assert lengthOfLongestSubstring("abccbailkmcbbacde") == 7
    assert lengthOfLongestSubstring("dvdf") == 3
    assert lengthOfLongestSubstring(" ") == 1
