

class ZPoly:
    """
        >>> z1 = ZPoly({0:1})
        >>> z1
        1*x^0
        >>> z2 = ZPoly({0:1, 1:2, 2:3})
        >>> z2
        1*x^0 + 2*x^1 + 3*x^2
        >>> z1 + z2
        2*x^0 + 2*x^1 + 3*x^2
        >>> z1 * z2
        1*x^0 + 2*x^1 + 3*x^2
    """
    def __init__(self, termdict):
        assert isinstance(termdict, dict)
        self._imp = termdict
        self._max = max([key for key in termdict])

    def add(self, other):
        m = max(self._max, other._max)
        t = {}
        for n in range(0, m+1):
            x = self._imp.get(n, 0) + other._imp.get(n, 0)
            if x:
                t[n] = x
        return ZPoly(t)

    def mul(self, other):
        t = {}
        for sk, sv in self._imp.items():
            for ok, ov in other._imp.items():
                k = sk+ok
                v = t.get(k, 0) + sv * ov
                if v:
                    t[k] = v
        return ZPoly(t)

    def __repr__(self):
        return ' + '.join(["%d*x^%d"%(value, key) for key, value in self._imp.items()])

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    @staticmethod
    def divmod(numerator, denominator):
        pass


class RPoly:
    pass


if __name__ ==  "__main__":
    import doctest
    doctest.testmod()
