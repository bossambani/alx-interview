def pascal_triangle(n):
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n - 1)
        last_row  = triangle[-1]

        new_row = [1] + [sum(x) for x in zip(last_row, last_row[1:])] + [1]

        triangle.append(new_row)

        return triangle