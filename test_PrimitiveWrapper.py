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

    def test_arithmetic(self):
        x = PrimitiveWrapper(5)
        y = PrimitiveWrapper(6)
        z = 7
        self.assertEqual(y-x,z-y)
        self.assertEqual(y - x, 1)
        self.assertEqual(x*y,30)
        self.assertEqual(x+y,11)
        self.assertTrue(x<y)
        self.assertTrue(x <= z)
