from PIL import Image
from conf import *
from triangle import *
import xml.etree.ElementTree as ET
import numpy as np

'''
Camera will always be at pointing with vector (0,0,-1), pointing downwards
'''


# im = Image.fromarray(A)
# im.save("your_file.jpeg")

class renderer:
    def __init__(self, dae_path):
        self.dae_path = dae_path
        self.dae = ET.parse(self.dae_path).getroot()
        return

    def get_triangles_from_DAE(self):
        raw = self.dae[5][0][0][0][0].text.split(' ')
        raw = np.asarray([float(x) for x in raw])
        return raw.reshape([-1, 3])

    def get_transformation_from_DAE(self):
        self.dae[7][0][5][0].text.split(' ')
        return

    @staticmethod
    def triangles_to_DAE():
        s = ''
        return

    @staticmethod
    def generate_canvas(dim):
        dim += [4]  # first 3 is rgb, last is for depth
        return tc.zeros(dim)

    @staticmethod
    def add_triangles_to_canvas(triangles, canvas):
        '''
        :param triangles: an array of triangles
        :param canvas: canvas ojb, can by empty or populated
        :return: newly populated canvas
        '''

        # rasterize

        return

    @staticmethod
    def train_cumulative_renderer():
        return

    @staticmethod
    def lambertian_reflectance(triangle, light_direction=tc.tensor([0.0, 0.0, 1.0], dtype=tc.float32),
                               light_intensity=1):
        '''
        i = (L.N)CI

        i = reflected intensity
        L = normalized light-direction vector, pointing from the surface to the light source
        N = surface's normal vector
        C = is the color
        I = is the intensity of the incoming light

        :param triangle: triangle object
        :return: rgb
        '''
        tri_normal = get_normal(triangle)
        power = tc.dot(tri_normal, light_direction)

        return tc.mul(tc.mul(triangle[3], power), light_intensity)


def tri_embed_to_canvas():
    return


def tri_array_to_dae(tri_array):
    return
