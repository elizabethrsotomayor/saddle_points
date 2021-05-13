from typing import List, Dict


def saddle_points(matrix: List) -> Dict[str, int]:
    """Return the row and column where a saddle point is present in a matrix."""
    if len(set(map(len, matrix))) > 1:
        raise ValueError('Irregular matrix')

    tmatrix = list(zip(*matrix))  # transpose for easy column ref
    points = []
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            if x == max(row) and x == min(tmatrix[j]):
                points.append({"row": i + 1, "column": j + 1})
    return points
