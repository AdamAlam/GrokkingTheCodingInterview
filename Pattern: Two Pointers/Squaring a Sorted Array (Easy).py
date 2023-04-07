def make_squares(arr):
    squares = []
    while len(arr) > 0:
        if abs(arr[0]) > abs(arr[-1]):
            squares = [arr[0] * arr[0]] + squares
            arr.pop(0)
        else:
            squares = [arr[-1] * arr[-1]] + squares
            arr.pop()
    return squares
