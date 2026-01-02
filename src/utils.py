import json
import os

def save_results(image_name, extracted_lines, output_dir="results"):
    os.makedirs(output_dir, exist_ok=True)

    data = {
        "image": image_name,
        "extracted_lines": extracted_lines
    }

    output_path = os.path.join(output_dir, f"{image_name}.json")
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

    return output_path
