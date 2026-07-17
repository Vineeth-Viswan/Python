def square_root_bisection(number, tolerance=0.0001, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    if number < 1:
        lower_bound = number
        upper_bound = 1
    else:
        lower_bound = 0
        upper_bound = number

    for _ in range(max_iterations):
        root = (lower_bound + upper_bound) / 2
        square = root * root

        if square < number:
            lower_bound = root
        else:
            upper_bound = root

        # Use interval width so tolerance maps directly to root accuracy.
        if (upper_bound - lower_bound) <= tolerance:
            root = (lower_bound + upper_bound) / 2
            print(f"The square root of {number} is approximately {root}")
            return root

    print(f"Failed to converge within {max_iterations} iterations")
    return None
    