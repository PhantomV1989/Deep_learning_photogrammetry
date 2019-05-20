import triangle as tri
from conf import *
from render import *

rtri = [tri.generate_random_triangle() for x in range(100)]

rend = renderer()
rend.get_triangles_from_DAE()
# color = rend.lambertian_reflectance(a)
# asd = 5
