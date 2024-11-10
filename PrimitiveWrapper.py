class PrimitiveWrapper:
    """A wrapper around a primitive val that overloads
    magic methods to simulate mutability of immutable types"""
    def __init__(self,val):
        assert type(val) in (int,float,bool,str) # You don't need this class otherwise
        self.val = val

    """Equality, slicing, and hashing will be based on val at time of check.
    It is up to YOU to be careful with this.
    """
    def __eq__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val == other.val
        return self.val == other

    def __hash__(self):
        return hash(self.val)

    def __index__(self):
        return self.val


    """Representations"""
    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f'PrimitiveWrapper: {self.val}'



    """Type conversion"""

    def __int__(self):
        return int(self.val)
    def __float__(self):
        return float(self.val)

    """Basic Arithmetic; should return a primitive type"""

    def __add__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val + other.val
        return self.val + other

    def __radd__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val + other.val
        return self.val + other

    def __sub__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val - other.val
        return self.val - other

    def __rsub__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return -( self.val - other.val)
        return -( self.val - other)

    def __mul__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val * other.val
        return self.val * other

    def __rmul__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val * other.val
        return self.val * other

    def __truediv__(self,other):
        if isinstance(other,PrimitiveWrapper):
            return self.val / other.val
        return self.val / other

    def __pow__(self, power, modulo=None):
        if isinstance(power,PrimitiveWrapper):
            return self.val.__pow__(power.val,modulo)
        return self.val.__pow__(power,modulo)


    """Comparison operators"""
    def __lt__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val < other.val
        return self.val < other

    def __gt__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val > other.val
        return self.val > other

    def __ge__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val >= other.val
        return self.val >= other

    def __le__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.val <= other.val
        return self.val <= other


    """Unary Operators"""

    def __pos__(self):
        return +self.val

    def __neg__(self):
        return -self.val
