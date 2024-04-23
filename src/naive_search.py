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

    found = False

    for i in range(haystack_len - needle_len + 1):
        j = 0
        while j < needle_len and haystack[i + j] == needle[j]:
            j += 1
            comparisons += 1

        if j == needle_len:
            found = True
            index = i

    if not found:
        comparisons = haystack_len

    return index, comparisons

haystack = "example1 example2 example3"
needle = "example3"
result_index, result_comparisons = naive_search(haystack, needle)

print("index:", result_index)
print("comparisons:", result_comparisons)
