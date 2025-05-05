import trimesh

def visualize_3d(model_path):
    mesh = trimesh.load(model_path)
    mesh.show()

import trimesh

mesh = trimesh.load(r'C:\Users\NAVEENKUMAR\Documents\VS_Code_Projects\3D_Create_Project\6e48z1kc7r40-bugatti\bugatti\bugatti.obj')
mesh.show()

# utils/visualize.py
import trimesh
import pyrender

def view_model(model_path):
    mesh = trimesh.load(model_path)
    if isinstance(mesh, trimesh.Scene):
        mesh = mesh.dump(concatenate=True)
    pyrender_mesh = pyrender.Mesh.from_trimesh(mesh)
    scene = pyrender.Scene()
    scene.add(pyrender_mesh)
    pyrender.Viewer(scene, use_raymond_lighting=True, background_color=[1, 1, 1, 1])


