with open('day13_input.txt', 'r') as f:
    points, folds = f.read().split('\n\n')
    points = {tuple(map(int, p.split(','))) for p in points.split('\n')}
    folds = [(fold[11], int(fold[13:])) for fold in folds.split('\n')]


def fold_paper(points, axis, n):
    if axis == 'x':
        return {(y - (y - n) * 2, x) if y > n else (y, x) for y, x in points}
    return {(y, x - (x - n) * 2) if x > n else (y, x) for y, x in points}


def AOC_day13_pt1(points):
    axis, n = folds[0]
    return len(fold_paper(points, axis, n))


def AOC_day13_pt2(points):
    for axis, n in folds:
        points = fold_paper(points, axis, n)
    return display_code(points)


def display_code(points):
    arr = [[' '] * 39 for _ in range(6)]
    for y, x in points:
        arr[x][y] = '#'
    return '\n'.join(''.join(row) for row in arr)


print(AOC_day13_pt1(points))
print(AOC_day13_pt2(points))