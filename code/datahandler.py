from conf import *
import xml.etree.ElementTree as ET


def create_daes_from_obj_folder():  # check for already created daes!
    objs = os.listdir(cf.obj_path)
    objs = list(filter(lambda x: x.__contains__('.obj'), objs))
    objs = [from_obj_file_to_dae(x,cf.dae_ref) for x in objs]

    return


def from_obj_file_to_dae(ofile, daefile):
    points, norms, faces = obj.process_obj_file(ofile)
    if max([len(f) for f in faces]) > 3:
        print(ofile + ' contains at least 1 face with more than 3 sides, not processing further.')
    else:
        ptag = [[ff.split('//') for ff in f] for f in faces]
        ptag = sum(sum(ptag, []), [])
        counts = len(faces)
        ptag = ' '.join(ptag)
        # <input semantic="VERTEX" source="#Obj-mesh-vertices" offset="0"/>
        # <input semantic="NORMAL" source="#Obj-mesh-normals" offset="1"/>

        flatten_points = sum(points, [])
        count_points = len(points)

        flatten_norms = sum(norms, [])
        count_norms = len(norms)

        dae_obj = ET.parse(daefile).getroot()
        asd = dae_obj[5][0][0][0][0].text.split(' ')
    return


class obj:
    @staticmethod
    def get_objs():
        objs = os.listdir(cf.obj_path)
        objs = list(filter(lambda x: x.__contains__('.obj'), objs))
        objs = [obj.process_obj_file(x, True) for x in objs]
        return objs

    @staticmethod
    def process_obj_file(b, return_face=False):
        v = []
        vn = []
        f = []

        _h = lambda x: [float(y) for y in x]
        with open(cf.obj_path + '/' + b, 'r') as file:
            d = file.readlines()
        for l in d:
            l = l.replace('\n', '')
            l = l.split(' ')
            if l[0] == 'vn':
                vn.append(_h(l[1:]))
            elif l[0] == 'v':
                v.append(_h(l[1:]))
            elif l[0] == 'f':
                f.append(l[1:])
        if return_face:
            faces = []
            for ff in f:
                npoints = [x.split('//')[0] for x in ff]
                points = [v[int(n) - 1] for n in npoints]
                norm = vn[int(ff[0].split('//')[-1]) - 1]
                faces.append([points, norm])
            return faces
        else:
            return [v, vn, f]


class dae:
    @staticmethod
    def parse_dae_from_file(fdae):
        dae = ET.parse(fdae).getroot()

        return

    @staticmethod
    def create_dae_from_obj(objo):
        return
