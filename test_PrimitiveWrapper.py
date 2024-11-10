import unittest
from PrimitiveWrapper import PrimitiveWrapper


class Test_pw_int(unittest.TestCase):

    def test_hashing_eq(self):
        x = PrimitiveWrapper(5)
        y = PrimitiveWrapper(5)
        z = 5
        s = set()
        s.add(x)
        self.assertIn(x, s)
        self.assertIn(y, s)
        self.assertIn(z, s)
        self.assertEqual(x,y)
        self.assertEqual(x,z)
        x.val+=1
        self.assertNotIn(x,s)
        self.assertNotEqual(x,y)

    def test_arrays(self):
        x = PrimitiveWrapper(-1)
        arr = ['hello','world']
        self.assertEqual(arr[x],arr[-1])
        x.val +=1
        self.assertEqual(arr[x],arr[0])

    def test_type_conversion(self):
        x = PrimitiveWrapper(10)
        y = int(x)
        self.assertEqual(y,10)
        self.assertFalse(isinstance(y,PrimitiveWrapper))

    def test_arithmetic(self):
        x = PrimitiveWrapper(5)
        y = PrimitiveWrapper(6)
        z = 7
        w = PrimitiveWrapper(3)
        self.assertEqual(y-x,z-y)
        self.assertEqual(y - x, 1)
        self.assertEqual(x*y,30)
        self.assertEqual(x+y,11)
        self.assertTrue(x<y)
        self.assertTrue(x <= z)
        self.assertEqual(y/w,2)
        self.assertEqual(x/y,5/6)
        self.assertEqual(x**y,5**6)
