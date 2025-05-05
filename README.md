# Prototype: Convert Photo or Text to a Simple 3D Model

This project demonstrates a simple AI-powered Python prototype that accepts either a **photo** (e.g., of a car) or a **text prompt** (e.g., "a small toy car") and generates a basic **3D model** in `.obj` or `.stl` format. The result can be visualized in 3D or used for 3D printing.

# Python Libraries Used
- trimesh : Create shapes: box, sphere, cylinder Load and export 3D model files: .obj, .stl
- pyrender : Creates an interactive 3D viewer window
- rembg : Removes background from an image 
- Pillow (PIL) : Open and handle images Resizing, cropping, or converting formats
- argparse
- os, sys, uuid, re
- numpy

 # Features

- Accepts text prompt or image as input
- Performs optional background removal for image input
- Uses open-source AI models to generate 3D geometry
- Exports 3D models as (.obj) or (.stl)
- Supports 3D visualization using (pyrender) and (trimesh)
- Python-based, open-source, and well-documented

# Thought Process

- Chose modular structure to keep text_to_3d, image_to_3d, and visualize clean and reusabl
- Used rembg and onnxruntime for background removal in images
- Chose trimesh and pyrender for 3D mesh handling and rendering
- Focused on minimal, reproducible prototype using open-source tooling

Demo Example

# To Run In Terminal 
# Run with a text prompt
python main.py --text "a futuristic car" --view

# Run with an image input
python main.py --image inputs/car.jpg --view


# We Seen This All Steps : 

1) main.py – Entry Point
2) generate.py – Core Utility
3) preprocess_image()
4) visualize.py – 3D Mesh Viewer
5) Output 
