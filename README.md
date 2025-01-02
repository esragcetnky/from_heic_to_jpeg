# HEIC to JPEG Batch Converter

This project provides a Python script to batch convert HEIC image files to JPEG format using the `Pillow` and `pillow-heif` libraries. It allows for easy conversion of multiple HEIC files stored in a specified folder to high-quality JPEG images in an output folder.

## Features
- Batch processing of HEIC files.
- High-quality JPEG output.
- Simple and easy-to-use script.
- Automatically handles folder creation for output files.

## Requirements

### Python Version
- Python 3.7 or higher

### Python Libraries
- `Pillow`
- `pillow-heif`

Install the required libraries using pip:
```bash
pip install pillow pillow-heif
```

## Usage

### 1. Clone or Download the Repository
Download the script file to your local machine.

### 2. Prepare Input and Output Folders
- Create a folder containing your `.heic` files (e.g., `input_folder`).
- Specify or create a folder for the converted `.jpeg` files (e.g., `output_folder`).

### 3. Update the Script
Open the script and replace the following placeholders with the paths to your folders:
```python
input_folder = "path_to_input_folder"  # Replace with your HEIC folder path
output_folder = "path_to_output_folder"  # Replace with your JPEG folder path
```

### 4. Run the Script
Run the script in your terminal or command prompt:
```bash
python convert_heic_to_jpeg.py
```

The script will process all `.heic` files in the input folder and save the converted `.jpeg` files in the output folder.

## Example
If your HEIC files are in a folder `C:/images/heic_files` and you want to save the JPEG files to `C:/images/jpeg_files`, update the script as follows:
```python
input_folder = "C:/images/heic_files"
output_folder = "C:/images/jpeg_files"
```
Run the script, and the JPEG files will appear in `C:/images/jpeg_files`.

## Error Handling
The script will skip files that cannot be processed and display an error message for each problematic file. Ensure that the input folder contains valid `.heic` files.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contributions
Contributions are welcome! Feel free to submit a pull request or report issues in the repository.

---

For any questions or assistance, please contact [Your Name/Email].

