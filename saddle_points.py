from typing import List, Dict


def saddle_points(matrix: List) -> Dict[str, int]:
    """Return the row and column where a saddle point is present in a matrix."""
    row_column = {"row": 0,
                  "column": 0}

    max_rows = [max(j) for j in matrix]
    # print(max_rows)

    columns = []

    for num in range(0, len(matrix)):
        column = [row[num] for row in matrix]
        columns.append(column)

    print(columns)

    # for num in range(0, len(matrix)): # columns
    #     for value in matrix: # rows
    #         print(value[num], value)

    return row_column


matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
print(saddle_points(matrix))  # should print {"row": 2, "column": 1} for value 5

# It's called a "saddle point" because it is greater than or equal to every element in its row and
# less than or equal to every element in its column.
