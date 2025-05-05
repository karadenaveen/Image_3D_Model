# Prototype: Convert Photo or Text to a Simple 3D Model

This project demonstrates a simple AI-powered Python prototype that accepts either a **photo** (e.g., of a car) or a **text prompt** (e.g., "a small toy car") and generates a basic **3D model** in `.obj` or `.stl` format. The result can be visualized in 3D or used for 3D printing.

 # Features

- Accepts text prompt or image as input
- Performs optional background removal for image input
- Uses open-source AI models to generate 3D geometry
- Exports 3D models as (.obj) or (.stl)
- Supports 3D visualization using (pyrender) and (trimesh)
- Python-based, open-source, and well-documented

Demo Example

# To Run In Terminal 
# Run with a text prompt
python main.py --text "a futuristic car" --view

# Run with an image input
python main.py --image inputs/car.jpg --view
