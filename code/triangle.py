import torch as tc


def generate_random_triangle(color=[1, 0, 0]):
    points = tc.rand([3, 3], dtype=tc.float32)
    color = tc.tensor([color], dtype=tc.float32)
    return tc.cat([points, color])  # first 3 points x 3D coordianates, last 3 is rgb


def generate_triangle(points, color=[1, 0, 0]):
    points += [color]
    return tc.tensor(points, dtype=tc.float32)


def get_normal(triangle):
    edge1 = tc.sub(triangle[0], triangle[2])
    edge2 = tc.sub(triangle[1], triangle[2])
    tri_normal = tc.cross(edge1, edge2)

    denorm = tc.pow(tc.sum(tc.pow(tri_normal, 2)), 0.5)
    return tc.div(tri_normal, denorm)


def flip_normal(triangle):
    return


def tri_to_emb(tri, dim=1000):
    return


def aggregrate_tri_arrays():
    return
