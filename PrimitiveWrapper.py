class PrimitiveWrapper:
    def __init__(self,val):
        self.val = val

    """Equality and hashing will be based on val.
    It is up to YOU to be careful with this
    """
    def __eq__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val == other.val
        return self.val == other

    def __hash__(self):
        return hash(self.val)

    """Basic Arithmetic"""

    def __add__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val + other.val
        return self.val + other