def naive_search(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    comparisons = 0
    index = None

    if needle_len == 0:
        comparisons = 0
        return index, comparisons

    if haystack_len < needle_len:
        comparisons = 0
        return index, comparisons

    for i in range(haystack_len - needle_len + 1):
        j = 0
        while j < needle_len and haystack[i + j] == needle[j]:
            comparisons += 1
            j += 1

        if j == needle_len:
            index = i
            comparisons += needle_len

    if index is None:
        comparisons = haystack_len - needle_len + 1

    return index, comparisons


