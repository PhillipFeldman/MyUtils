class PrimitiveWrapper:
    """A wrapper around a primitive val that overloads
    magic methods to simulate mutability of immutable types

    Params:
        val: the value, eg: 5, True, "hello"
        return_wrapper: Whether the result of operations should return a builtin type or a wrapper around it
                        Be careful with non-symmetric return_wrapper
    """
    def __init__(self,val,arithmetic_return_wrapper=False,conversion_return_wrapper=False
                 ,arithmetic_with_assignment_modifies=True):
        if type(val) == PrimitiveWrapper:
            val = val.val
        assert type(val) in (int,float,bool,str) # You don't need this class otherwise
        self.val = val
        self.arithmetic_return_wrapper = arithmetic_return_wrapper
        self.conversion_return_wrapper = conversion_return_wrapper
        self.arithmetic_with_assignment_modifies = arithmetic_with_assignment_modifies

    def arithmetic_wrap_or_not(self,val):
        if self.arithmetic_return_wrapper:
            return PrimitiveWrapper(val,self.arithmetic_return_wrapper,self.conversion_return_wrapper,self.arithmetic_with_assignment_modifies)
        else:
            return val

    def conversion_wrap_or_not(self,val):
        if self.conversion_return_wrapper:
            return PrimitiveWrapper(val,self.arithmetic_return_wrapper,self.conversion_return_wrapper,self.arithmetic_with_assignment_modifies)
        else:
            return val

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
        return self.conversion_wrap_or_not(int(self.val))
    def __float__(self):
        return self.conversion_wrap_or_not(float(self.val))

    """Basic Arithmetic; should return a primitive type"""

    def __add__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.arithmetic_wrap_or_not(self.val + other.val)
        return self.arithmetic_wrap_or_not(self.val + other)

    def __radd__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.arithmetic_wrap_or_not(self.val + other.val)
        return self.arithmetic_wrap_or_not(self.val + other)

    def __sub__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.arithmetic_wrap_or_not(self.val - other.val)
        return self.arithmetic_wrap_or_not(self.val - other)

    def __rsub__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.arithmetic_wrap_or_not(-( self.val - other.val))
        return self.arithmetic_wrap_or_not(-( self.val - other))

    def __mul__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.arithmetic_wrap_or_not(self.val * other.val)
        return self.arithmetic_wrap_or_not(self.val * other)

    def __rmul__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.arithmetic_wrap_or_not(self.val * other.val)
        return self.arithmetic_wrap_or_not(self.val * other)

    def __truediv__(self,other):
        if isinstance(other,PrimitiveWrapper):
            return self.arithmetic_wrap_or_not(self.val / other.val)
        return self.arithmetic_wrap_or_not(self.val / other)

    def __pow__(self, power, modulo=None):
        if isinstance(power,PrimitiveWrapper):
            return self.arithmetic_wrap_or_not(self.val.__pow__(power.val,modulo))
        return self.arithmetic_wrap_or_not(self.val.__pow__(power,modulo))


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
        return self.arithmetic_wrap_or_not(+self.val)

    def __neg__(self):
        return self.arithmetic_wrap_or_not(-self.val)


    """Arithmetic with assignment, will either modify or return new, depending"""
    def arithmetic_assignment_modify_or_not(self,val):
        if self.arithmetic_with_assignment_modifies:
            self.val=val
            return self
        else:
            return self.arithmetic_wrap_or_not(val)

    def __iadd__(self, other):
        if isinstance(other,PrimitiveWrapper):
            return self.arithmetic_assignment_modify_or_not(self.val + other.val)
        return self.arithmetic_assignment_modify_or_not(self.val + other)

