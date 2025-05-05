import os
from PIL import Image
from rembg import remove

def preprocess_image(image_path, save_path="output/processed.png"):
    image = Image.open(image_path).convert("RGBA")
    image = remove(image)
    image.save(save_path)
    return save_path

def generate_3d_from_text(prompt, save_path="output/generated.obj"):
    with open(save_path, "w") as f:
        f.write("# dummy OBJ file for: " + prompt)
    return save_path

def generate_3d_from_image(image_path, save_path="output/from_photo.obj"):
    with open(save_path, "w") as f:
        f.write("# dummy OBJ file for photo-based 3D reconstruction")
    return save_path


