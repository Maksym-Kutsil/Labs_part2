def naive_search(haystack, needle):
    n = len(haystack)
    m = len(needle)
    comparisons = (n - m + 1)
    index = None

    if m == 0:
        comparisons = 0
        return index, comparisons

    if n < m:
        comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m and haystack[i + j] == needle[j]:
            j += 1

        if j == m:
            index = i

    return index, comparisons


haystack = "example1 example2"
needle = "example2"
result_index, result_comparisons = naive_search(haystack, needle)

print("index:", result_index)
print("comparisons:", result_comparisons)
