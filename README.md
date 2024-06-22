# Folder Compression and Decompression Tool

This Python script provides a simple GUI to select folders for compression into ZIP files. It's designed to be user-friendly, allowing users to compress folders quickly and decide whether to delete the original folders after compression.

## Features

- **GUI for Folder Selection**: Utilizes a graphical interface to select the folder you wish to compress.
- **Compression to ZIP Format**: Compresses the selected folder into a ZIP file.
- **Option to Delete Original Folder**: After compression, it prompts the user with the option to delete the original folder.

## Requirements

- Python 3.x
- Tkinter library (usually comes with Python)
- shutil library
- os library

## How to Use the compression tool

1. **Ensure Python is Installed**: This script requires Python. You can download it from [python.org](https://www.python.org/downloads/).

2. **Download the Script**: Download `compress_folder.py` to your local machine.

3. **Run the Script**: Open a terminal or command prompt, navigate to the directory where `compress_folder.py` is located, and run the script using the following command:

    ```bash
    python compress_folder.py
    ```

4. **Select Folder to Compress**: The script will open a file dialog. Navigate to the folder you wish to compress and select it.

5. **Compression**: The script will compress the selected folder into a ZIP file and save it in the `/Users/nephthalisalam/Documents/Compressed_Folders` directory.

6. **Option to Delete Original Folder**: After compression, a prompt will ask if you want to delete the original folder. Choose "Yes" to delete or "No" to keep it.

## Customization

- **Change Destination Folder**: To change the destination folder for the compressed files, modify the `destination_folder` variable in the `select_folder_and_compress` function.

## How to Use the decompression tool

1. **Ensure Python is Installed**: This script requires Python. You can download it from [python.org](https://www.python.org/downloads/).

2. **Download the Script**: Download `decompress_zip.py` to your local machine.

3. **Run the Script**: Open a terminal or command prompt, navigate to the directory where `decompress_zip.py` is located, and run the script using the following command:

    ```bash
    python decompress_zip.py
    ```

4. **Select ZIP File to Decompress**: The script will open a file dialog. Navigate to the ZIP file you wish to decompress and select it.

5. **Select Output Directory**: After selecting the ZIP file, you will be prompted to choose the directory where the decompressed files will be placed.

6. **Decompression**: The script will decompress the contents of the ZIP file into the specified output directory.

## Customization

- **Change Default Output Directory**: To change the default output directory for decompressed files, modify the `default_output_directory` variable in the `select_zip_and_decompress` function.

## Troubleshooting

- **Tkinter Not Found**: Ensure you have Python installed correctly and that Tkinter is included in your installation. Tkinter is included with most Python installations, but some minimal installations may not include it.

- **Permission Issues**: If the script cannot delete the original folder or save the compressed file, check your folder permissions.

## License

This script is provided "as is", without warranty of any kind. You are free to use, modify, and distribute it as you see fit.

## Acknowledgments

This script was created to simplify the process of compressing folders on my local machine. It's a basic tool, but it serves its purpose well. Feel free to contribute or suggest improvements.