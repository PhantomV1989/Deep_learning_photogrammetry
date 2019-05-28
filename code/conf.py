import os


class conf():
    def __init__(self):
        dir = os.getcwd()
        self.dir = dir
        self.output_path = handle_path(self._up(dir) + '/data')
        self.obj_path = self.output_path + '/obj'
        self.dae_path = self.output_path + '/daes'
        self.dae_ref = self.dae_path + '/reference.dae'
        return

    @staticmethod
    def _up(dir):
        t = dir.split('/')
        t.pop()
        return '/'.join(t)


def handle_path(p):
    if not os.path.exists(p):
        os.mkdir(p)
    return p


cf = conf()
