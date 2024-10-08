from math import gcd

class Rational:
    def __init__(self, n, d):
        try:
            if d == 0:
                raise ZeroDivisionError

            self.n = n
            self.d = d
            self._reduction()
            self._sign()

        except ZeroDivisionError:
            print('Нельзя делить на 0')

    def _reduction(self):
        div = gcd(self.n,self.d)
        self.n //= div
        self.d //= div

    def _sign(self):
        if self.d < 0:
            self.n = -self.n
            self.d = -self.n

    def __str__(self):
        return f'{self.n} / {self.d}'

    def __add__(self, other):
        global new_n, new_d
        if isinstance(other, Rational):
            new_n = (self.n * other.d) + (other.n * self.d)
            new_d = self.d * other.d
        elif isinstance(other, int):
            new_n = self.n + other * self.d
            new_d = self.d

        return Rational(new_n, new_d)

    def __sub__(self, other):
        global new_d, new_n
        if isinstance(other, Rational):
            new_n = (self.n * other.d) - (other.n * self.d)
            new_d = self.d * other.d
        elif isinstance(other, int):
            new_n = self.n - other * self.d
            new_d = self.d

        return Rational(new_n,new_d)

    def __mul__(self, other):
        global new_n, new_d
        if isinstance(other, Rational):
            new_n = self.n * other.n
            new_d = self.d * other.d
        elif isinstance(other, int):
            new_n = self.n * other
            new_d = self.d

        return Rational(new_n,new_d)

    def __truediv__(self, other):
        global new_n, new_d
        if isinstance(other, Rational):
            new_n = self.n * other.d
            new_d = self.d * other.n
        elif isinstance(other,int):
            new_n = self.n
            new_d = self.d * other

        return Rational(new_n,new_d)

    def __pow__(self, power, modulo=None):
        return Rational(self.n ** power, self.d ** power)
