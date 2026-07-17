def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers[:]

    pivot = numbers[-1]
    less_than = []
    equal_to = []
    greater_than = []

    for value in numbers:
        if value < pivot:
            less_than.append(value)
        elif value > pivot:
            greater_than.append(value)
        else:
            equal_to.append(value)

    return quick_sort(less_than) + equal_to + quick_sort(greater_than)