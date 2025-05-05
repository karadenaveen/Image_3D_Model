import trimesh
import os

def generate_3d_from_text(prompt: str) -> str:
    prompt = prompt.lower()
    
    model_path = None
    if "car" in prompt:
        model_path = r'C:\Users\NAVEENKUMAR\Documents\VS_Code_Projects\3D_Create_Project\6e48z1kc7r40-bugatti\bugatti\bugatti.obj'
    elif "ball" in prompt or "sphere" in prompt:
        model_path = "assets/models/ball.obj"
    elif "chair" in prompt:
        model_path = "assets/models/chair.obj"
    elif "cube" in prompt:
        return trimesh.creation.box(extents=(1, 1, 1)).export("output/generated_model.obj")

   
    if model_path and os.path.exists(model_path):
        mesh = trimesh.load(model_path)
        os.makedirs("output", exist_ok=True)
        output_path = "output/generated_model.obj"
        mesh.export(output_path)
        print(f"Loaded model saved to: {output_path}")
        return output_path
    else:
        mesh = trimesh.creation.box(extents=(1, 1, 1))
        os.makedirs("output", exist_ok=True)
        output_path = "output/generated_model.obj"
        mesh.export(output_path)
        print("Fallback to cube. 3D model saved to:", output_path)
        return output_path
