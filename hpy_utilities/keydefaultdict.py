from collections import defaultdict


class KeyDefaultDict(defaultdict):
    """
    Extended default dictionary which uses the key as an argument to the default factory.
    """
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret