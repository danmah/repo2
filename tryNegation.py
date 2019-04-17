import operator


class ReversibleString(object):
    def __init__(self, s):
        self.s = s

    def __invert__(self):
        return ReversibleString(self.s[::-1])

    def __str__(self):
        return self.s


s = ReversibleString('The brown fox lazy over the bed.')
print(~s)
print(~~s)
