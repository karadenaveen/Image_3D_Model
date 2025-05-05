import argparse
from utils.generate import generate_3d_from_text, generate_3d_from_image, preprocess_image
from utils.visualize import view_model
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, help="Text prompt to generate 3D")
    parser.add_argument('--image', type=str, help="Image path to convert to 3D")
    parser.add_argument('--view', action="store_true", help="Visualize 3D model")
    args = parser.parse_args()

    os.makedirs("output", exist_ok=True)

    if args.text:
        print("[INFO] Generating from text...")
        model_path = generate_3d_from_text(args.text)
    elif args.image:
        print("[INFO] Preprocessing image...")
        cleaned = preprocess_image(args.image)
        print("[INFO] Generating from image...")
        model_path = generate_3d_from_image(cleaned)
    else:
        print("Provide either --text or --image")
        return

    print(f"[INFO] Model saved at {model_path}")

    if args.view:
        view_model(model_path)

if __name__ == "__main__":
    main()

