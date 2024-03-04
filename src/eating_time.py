def can_eat(piles, hours, k):
    eating_hours = 0
    for pile in piles:
        eating_hours += (pile + k - 1) // k
    return eating_hours <= hours


def min_eating_speed(piles, h):
    left = 1
    right = max(piles)

    while left <= right:
        mid = (left + right) // 2
        if can_eat(piles, h, mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


print(min_eating_speed([3, 6, 7, 11], 8))
print(min_eating_speed([30, 11, 23, 4, 20], 5))
print(min_eating_speed([30, 11, 23, 4, 20], 6))
