

class PairSeq:
    """
        >>> xs = PairSeq({0:1, 1:2})
        >>> xs.get_by_key(0)
        1
        >>> xs.get_by_key(4)
        Traceback (most recent call last):
          ...
        KeyError
        >>> xs = PairSeq({0:1, 1:2, 4:4})
        >>> xs.get_by_key(4)
        4
        >>> xs.get_by_key(3)
        Traceback (most recent call last):
          ...
        KeyError
        >>> xs.get_by_key(3, 0)
        0

    """

    def __init__(self, d):
        self.xs = tuple(sorted(d.items(), key=lambda x: x[0]))

    def get_by_nth(self, n):
        return self.xs[n]

    def get_by_key(self, k, default=None):
        '''does binary search'''
        hi = len(self.xs)
        lo = 0
        while hi > lo:
            mi = (hi + lo)/2
            if self.xs[mi][0] < k:
                lo = mi + 1
            elif self.xs[mi][0] == k:
                return self.xs[mi][1]
            elif k < self.xs[mi][0]:
                hi = mi
            else:
                assert False
        if default is not None:
            return default
        raise KeyError

    def first(self):
        return self.xs[0][1]

    def last(self):
        return self.xs[-1][1]

    def items(self):
        return self.xs


class ZPoly:
    """
        >>> z1 = ZPoly({0:1})
        >>> z1
        1*x^0
        >>> z2 = ZPoly({0:1, 1:2, 2:3})
        >>> z2
        1*x^0 + 2*x^1 + 3*x^2
        >>> z3 = ZPoly({1:1, 2:2})
        >>> z3
        1*x^1 + 2*x^2
        >>> z1 + z2
        2*x^0 + 2*x^1 + 3*x^2
        >>> z1 * z2
        1*x^0 + 2*x^1 + 3*x^2
        >>> z2 * z3
        1*x^1 + 4*x^2 + 7*x^3 + 6*x^4
        >>> ZPoly.divmod(z2, z1)
        1*x^0 + 2*x^1 + 3*x^2

    """
    def __init__(self, termdict):
        assert isinstance(termdict, dict)
        self._imp = PairSeq(termdict)
        self._max = max([key for key in termdict])

    def max(self):
        return self._imp.last()

    def min(self):
        return self._imp.first()

    def add(self, other):
        m = max(self.max(), other.max())
        t = {}
        for n in range(0, m+1):
            x = self._imp.get_by_key(n, 0) + other._imp.get_by_key(n, 0)
            if x:
                t[n] = x
        return ZPoly(t)

    def mul(self, other):
        t = {}
        for sk, sv in self._imp.items():
            for ok, ov in other._imp.items():
                k = sk + ok
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

    def _fit(self, other):
        pass


    @staticmethod
    def divmod(numerator, denominator):
        return numerator


class RPoly:
    def __init__(self, numerator, denominator):
        pass



if __name__ ==  "__main__":
    import doctest
    doctest.testmod()

