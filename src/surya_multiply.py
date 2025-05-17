def surya_multiply(A_sc, B_sc):
    """Surya's method for 2x2 symmetric circulant matrices (2 multiplications).
    A_sc = [a, b] represents [[a, b], [b, a]]
    B_sc = [x, y] represents [[x, y], [y, x]]
    """
    a, b = A_sc
    x, y = B_sc
    sa = a + b
    da = a - b
    sb = x + y
    db = x - y

    p1 = sa * sb  # Multiplication 1
    p2 = da * db  # Multiplication 2

    c11 = (p1 + p2) / 2
    c12 = (p1 - p2) / 2

    if (isinstance(a, int) and isinstance(b, int) and
        isinstance(x, int) and isinstance(y, int) and
        (p1 + p2) % 2 == 0 and (p1 - p2) % 2 == 0):
        c11 = int(c11)
        c12 = int(c12)

    return [[c11, c12], [c12, c11]]
