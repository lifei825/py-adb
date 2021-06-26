class Params(dict):
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, x):
        if isinstance(self.get(x), dict):
            Params.cache = x
            return Params(**self.get(x))
        else:
            return self.get(x)


if __name__ == '__main__':
    a = {"aa": "bb", "cc": {"c": "22", "yy": {"aaa": "22yy"}}}
    A = Params(a)
    print(A.aa, A.cc.yy.aaa)
