"""The following is a python solution to the problem described above. It reads the input from a file called `18_input` and prints the result of the calculation.

"""
def reduce_pair(pair):
    left, right = pair
    if isinstance(left, int) and left >= 10:
        left = [left // 2, (left + 1) // 2]
    if isinstance(right, int) and right >= 10:
        right = [right // 2, (right + 1) // 2]
    return [left, right]

def reduce_number(number):
    if not isinstance(number, list):
        return number

    if len(number) == 2 and isinstance(number[0], list) and isinstance(number[1], list):
        left, right = map(reduce_number, number)
        return reduce_pair([left, right])

    if len(number) >= 4 and isinstance(number[0], list) and isinstance(number[1], list) and isinstance(number[2], list) and isinstance(number[3], list):
        leftmost = reduce_number(number[0])
        rest = reduce_number(number[1:])
        first_regular_number = -1
        for i, n in enumerate(rest):
            if isinstance(n, int):
                first_regular_number = i
                break

        if first_regular_number == -1:
            return [0, leftmost[1]] + rest
        else:
            left_rest = rest[:first_regular_number]
            right_rest = rest[first_regular_number + 1:]
            return left_rest + [leftmost[0] + rest[first_regular_number]] + right_rest

    return reduce_pair(number)

def reduce_sum(sum):
    left, right = map(reduce_number, sum)
    return reduce_pair([left, right])

with open('18_input') as f:
    left, right = map(eval, map(str.strip, f))
    print(reduce_sum([left, right]))
""""""