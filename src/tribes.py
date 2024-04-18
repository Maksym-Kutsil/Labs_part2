def count_possible_pairs(n, groups):
    group_pairs = []
    used_numbers = []

    for index, group in enumerate(groups):
        if len(group) == 1:
            first = group[0]
            second = None
        else:
            first, second = group

        active_pairs = []
        is_in_prev_group = first in used_numbers or (second and second in used_numbers)

        if not is_in_prev_group:
            if first:
                active_pairs.append(first)
            if second:
                active_pairs.append(second)

        for i in range(index + 1, len(groups)):
            firs_next, second_next = groups[i]
            is_in_prev_group = firs_next in used_numbers or second_next in used_numbers
            if (firs_next in active_pairs or second_next in active_pairs) and not is_in_prev_group:
                active_pairs.extend([firs_next, second_next])

        if active_pairs:
            unique_pairs = list(set(active_pairs))
            used_numbers.extend(unique_pairs)
            group_pairs.append(unique_pairs)

    count = 0

    def is_even(number):
        return number % 2 == 0

    for i in range(len(group_pairs)):
        pair = group_pairs[i]
        for prev in pair:
            for j in range(i + 1, len(group_pairs)):
                next_pairs = group_pairs[j]
                for next_num in next_pairs:
                    if (is_even(prev) and not is_even(next_num)) or (not is_even(prev) and is_even(next_num)):
                        count += 1

    return count

input1 = [
    [1, 2],
    [2, 4],
    [3, 5]
]

input2 = [
    [1, 2],
    [2, 4],
    [1, 3],
    [3, 5],
    [8, 10]
]

input3 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(count_possible_pairs(4, input1))
print(count_possible_pairs(5, input2))
print(count_possible_pairs(3, input3))
