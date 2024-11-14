#Задача F
class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if sum(1 for i in (a, b, c) if type(i) not in (int, float)):
        raise TypeError
    elif not a and not b and not c:
        raise InfiniteSolutionsError
    elif not a and not b and c or b ** 2 < 4 * a * c:
        raise NoSolutionsError
    elif b ** 2 == 4 * a * c:
        return -b / (2 * a), -b / (2 * a)
    elif not a:
        return -c / b
    else:
        roots = [(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)]
        roots.sort()
        return roots[0], roots[1]