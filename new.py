import os
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIF opener
register_heif_opener()

def convert_heic_to_jpeg(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith('.heic'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.jpeg")

            try:
                # Open and convert HEIC to JPEG
                with Image.open(input_path) as img:
                    img.save(output_path, "JPEG", quality=90)
                print(f"Converted: {file_name} -> {output_path}")
            except Exception as e:
                print(f"Error converting {file_name}: {e}")

if __name__ == "__main__":
    # Define the input and output folder paths
    input_folder = "D:\multimedya\Arcahia.exe\ocak25"  # Replace with your HEIC folder path
    output_folder = "D:\multimedya\Arcahia.exe\ocak25_jpeg"  # Replace with your JPEG folder path

    # Call the conversion function
    convert_heic_to_jpeg(input_folder, output_folder)
