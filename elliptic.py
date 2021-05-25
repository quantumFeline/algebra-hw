import numpy as np
from primes import primes

EPS = 1e-3
RANGE = 1e3


def eq(a: float, b: float):
    return np.abs(a-b) < EPS


class Point:
    def __init__(self, x=0.0, y=0.0, inf=False):
        self.x = x
        self.y = y
        self.inf = inf

    def __str__(self):
        if self.inf:
            return "point: inf"
        else:
            return f"Point: {self.x} {self.y}"

    @staticmethod
    def random_point():
        return Point(*np.random.random((2,)) * RANGE)


# y^2 = x^3 + a x + b
class Equation:
    def __init__(self, k1, k2, mod):
        self.equation_coefs = np.array([k1, k2])
        self.mod = mod

    @staticmethod
    def random_equation(mod):
        return Equation(*np.random.random((2,)) * RANGE, mod)

    def calc(self, p: Point, q: Point):
        """
        Function defined on the curve.
        Given P and Q, it finds a point R than is on the same line
        with P and Q, and returns its mirror image relative to abscissa.
        :param p: A point P on the curve.
        :param q: Another point Q on the curve.
        :return: A mirror point -R.
        """
        if p.inf:
            return q
        elif q.inf:
            return q

        elif not eq(p.x, q.x):
            a = (q.y-p.y)/(q.x-p.x)

        elif eq(p.x, p.x) and not eq(p.y, q.y):
            return Point(inf=True)

        else:
            if eq(p.y, 0):  # Anti div-by-zero
                return Point(inf=True)

            k1 = self.equation_coefs[0]
            a = (3 * p.x**2 + k1) / (2 * p.y)

        # Same for first and third branches
        b = p.y - a * p.x
        r_x = a**2 - p.x - q.x
        r_y = r_x * a + b
        #return Point(r_x % self.mod, -r_y % self.mod)
        return Point(r_x, -r_y)

    def point_power(self, point, power):
        res = self.calc(point, point)
        for i in range(power-2):
            res = self.calc(res, point)
        return res

    def __str__(self):
        a, b = self.equation_coefs
        return f"Elliptic curve: y^2 = x^3 + {a}x + {b}"

    # def elliptic_value(self, x):
    #     a, b, c = self.equation_coefs


def generate_keys():

    # Public
    n = np.random.choice(primes, (2,))
    n = n[0] * n[1]
    equation = Equation.random_equation(n)
    p = Point.random_point()
    # print(equation, order, p)

    # Private
    k = np.random.randint(10)
    # k = 5
    y = equation.calc(p, p)
    for i in range(k-2):
        y = equation.calc(y, p)

    return ([equation, n, p, y],  # public
            k)  # private


def test_elliptic():
    e = Equation(1, 5, 1000)
    p = Point(-1.4812, 0.5189)
    q = Point(0.3111, 2.3111)
    print(e.calc(p, q))


def main():
    public, private = generate_keys()
    print(*public)
    e, order, p, y = public
    # print(private)

    while True:
        input()
        r = np.random.randint(10)  # Session key
        # r = 1
        alice_message = Point(*np.random.randint(0, order, (2,)))
        print(f"session key: {r}, alice_message: {alice_message}")
        c = (e.point_power(p, r), e.calc(alice_message, e.point_power(y,r)))
        print(f"coded: {c[0]} {c[1]}")

        # Decoding
        s = e.point_power(c[0], private)
        s = Point(s.x, -s.y)
        message = e.calc(s, c[1])
        message = Point(int(message.x), int(message.y))
        print(f"decoded: {message}")


if __name__ == '__main__':
    main()
