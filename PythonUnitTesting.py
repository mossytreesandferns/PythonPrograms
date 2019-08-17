"""This is the Module Code"""


import math
# Triangles

def hypotenuse(a,b):
    if a < 0 or b < 0:
        raise ValueError("The input cannot be negative")
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

print(hypotenuse(3,4))
print(hypotenuse(4,5))
print(hypotenuse(1,3))   

def area_tri(b,h):
    if h < 0 or b < 0:
        raise ValueError("The input cannot be negative")
    area = .5*b*h
    return area
print(area_tri(5,4))
print(area_tri(3,5))
print(area_tri(5,7))    

# Circles
from math import pi
def circumference(r):
    if r < 0:
        raise ValueError("The input cannot be negative")
    circumference = 2*pi*r
    return circumference
print(circumference(3))
print(circumference(4))    
print(circumference(5))

def area_circ(r):
    if r < 0:
        raise ValueError("The input cannot be negative")
    area = pi*r**2
    return area 
print(area_circ(3))
print(area_circ(4))    
print(area_circ(5))  


"""This is the Testing Code (Module and testing code should be in separate files"""

import unittest
import PythonGeometryFormulas

class TestPythonGeometryFormulas(unittest.TestCase):
    def test_hypotenuse(self):
        self.assertEqual(PythonGeometryFormulas.hypotenuse(3,4),5)
        self.assertAlmostEqual(PythonGeometryFormulas.hypotenuse(4,5),6.4031242374328485)
        self.assertAlmostEqual(PythonGeometryFormulas.hypotenuse(1,3),3.1622776601683795)

    def test_area_tri(self): 
        self.assertEqual(PythonGeometryFormulas.area_tri(3,4),6)
        self.assertEqual(PythonGeometryFormulas.area_tri(3,5),7.5)
        self.assertEqual(PythonGeometryFormulas.area_tri(5,7),17.5)

    def test_circumference(self):
        self.assertAlmostEqual(PythonGeometryFormulas.circumference(3),18.84955592153876)
        self.assertAlmostEqual(PythonGeometryFormulas.circumference(4),25.132741228718345)
        self.assertAlmostEqual(PythonGeometryFormulas.circumference(5),31.41592653589793)

    def test_area_circ(self):   
        self.assertAlmostEqual(PythonGeometryFormulas.area_circ(3),28.27433388230813)
        self.assertAlmostEqual(PythonGeometryFormulas.area_circ(4),50.26548245743669)
        self.assertAlmostEqual(PythonGeometryFormulas.area_circ(5),78.53981633974483)
        
        self.assertRaises(ValueError,PythonGeometryFormulas.area_circ,-2)
        with self.assertRaises(ValueError):
            PythonGeometryFormulas.area_circ(-2)


if __name__ == '__main__':
    unittest.main()