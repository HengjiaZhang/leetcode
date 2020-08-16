# Python program for KMP Algorithm
def KMPSearch(pattern, text):
    M = len(pattern)
    N = len(text)
    result = []

    # Preprocess the pattern: create lps[] that will hold the longest prefix suffix values for pattern
    # lps[i] = the longest proper prefix of pat[0..i], which is also a suffix of pat[0..i].
    lps = computeLPSArray(pattern)
    print(f"the longest prefix suffix array is {lps}")

    text_index = 0  # index for text[]
    pattern_index = 0  # index for pattern[]
    while text_index < N:
        # 当前字符匹配成功
        if pattern[pattern_index] == text[text_index]:
            text_index += 1
            pattern_index += 1
        # 当前字符匹配失败
        else:
            if pattern_index != 0:
                pattern_index = lps[pattern_index - 1]
            else:
                text_index += 1
        # pattern_index==len(pattern) 说明完全匹配成功
        if pattern_index == M:
            print("Found pattern at index " + str(text_index - pattern_index))
            result.append(text_index - pattern_index)
            pattern_index = lps[pattern_index - 1]
    return result if result else -1


def computeLPSArray(pattern):
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1
    # the loop calculates lps[i] for i = 1 to M-1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if length != 0:
                length = lps[length - 1]
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    return lps


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"

print(KMPSearch(pat, txt))
