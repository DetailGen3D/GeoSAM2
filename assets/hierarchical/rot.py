import trimesh
from glob import glob
from tqdm import tqdm
import numpy as np

rot_mat = np.array([
    [1,0,0,0],
    [0,0,1,0],
    [0,-1,0,0],
    [0,0,0,1]
])

mesh_list = glob("/Users/dengken/Documents/Vast/PartDiff/web/GeoSAM2/assets/hierarchical/*/*.glb")

for mesh_path in tqdm(mesh_list):
    mesh = trimesh.load(mesh_path, force='mesh')
    mesh.apply_transform(rot_mat)
    mesh.export(mesh_path)
    # import pdb;pdb.set_trace()  # Debugging line to pause execution and inspect variables
    # pass