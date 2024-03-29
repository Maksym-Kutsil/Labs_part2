def can_eat(piles, hours, k):
    piles.sort()
    eating_hours = 0
    for pile in piles:
        eating_hours += (pile + k - 1) // k
    return eating_hours <= hours

def min_eating_speed(piles, h):
    piles.sort()
    if h < len(piles):
        return None
    left = 1
    right = max(piles)
    while left <= right:
        mid = (left + right) // 2
        if can_eat(piles, h, mid):
            right = mid - 1
        else:
            left = mid + 1
    return left



print(min_eating_speed([4, 10, 3, 8, 6], 7))
print(min_eating_speed([4, 8, 1, 4, 5, 3], 10))
print(min_eating_speed([30, 11, 23, 4, 20], 11))
