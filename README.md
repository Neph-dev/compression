# A little bit about compression:

**Definition:** Data compression is the process of reducing the size of a data file. It’s achieved by encoding the information in a way that takes up less space than the original representation.

**Compression techniques:**

1. **Lossless compression**: this method allows the original data to be perfectly reconstructed from the compressed data. Common examples include ZIP, PNG and GIF.

2. **Lossy compression:** This method sacrifices some amount of data fidelity in exchange for higher compression rates. The original data cannot be perfectly reconstructed, but the approximation is usually close enough for the intended purpose. Common examples include JPEG, MP3 and MPEG videos.

**Detailed Aspects of compression:**

**Lossless compression**

Lossless compression techniques exploit statistical redundancy in the data to reduce its size. Here are some common methods:

1. **Run-Length Encoding (RLE):** This method replaces sequences of repeating characters or data elements with a single data value and a count. For example, “AAAAAA” might be encoded as “6A”.

2. **Huffman Coding:** This method uses variable-length codes for encoding symbols. Symbols that occur more frequently are assigned shorter codes, while less frequent symbols gets longer codes. It relies on building a binary tree based on the frequencies of the symbols.

3. **Lempel-Ziv-Welch (LZW):** This algorithm build a dictionary of strings encountered in the data. It replaces occurrences of these strings with references to the dictionary, effectively compressing the data.

4. **Deflate:** This is a combination of LZ77 (a variant of LZW) and Huffman coding. it is used in formats like ZIP and PNG.

**Lossy compression**

Lossy compression techniques remove some data to achieve higher compression rate, focusing on removing parts of the data that are less likely to be notices by human perception. Here are some common methods:

1. **Transform coding (e.g., Discrete Cosine Transform in JPEG):** This method transforms data into a different domain (such as the frequency domain), where it can be more efficiently compressed. JPEG, for example, transforms image data into the frequency domain, quantizes the less important frequencies more coarsely, and the compresses the the result.

2. **Quantization:** This process reduces the precision of the data, making it less accurate but smaller in size. In images, for instance, slight variations in color that are imperceptible to the human eye can be quantized to the same value.

3. **Wavelet compression**: this method uses wavelet transforms to convert data into a different format that can be more efficiently compressed. It’s used in JPEG 2000 and modern images compression formats.


**In-Depth Example: Huffman Coding**

To illustrate how one of these methods works in more detail, let’s look at Huffman coding:

1. **Frequency analysis:** Analyze the frequency of each symbol in the data.

2. **Tree building:** Create a binary tree where each leaf node represents a symbol. The tree is built by repeatedly merging the two least frequent nodes until only one node remains. This node becomes the root of the tree.

3. **Code assignment:** Traverse the tree from the root to assign binary codes to each symbol. Moving left assigns a ‘0’ and moving right a ‘1’.

4. **Encoding:** Replace each symbol in the original data with its corresponding binary code from the tree.

For example, given the data “ABBCCCDDDDEEEEE”:

- Frequency analysis: A=1, B=2, C=3, D=4, E=5
- Build the tree:
    - Combine A (1) and B (2) to form AB (3)
    - Combine AB (3) and C (3) to form ABC (6)
    - Combine D (4) and E (5) to form DE (9)
    - combine ABC (6) and DE (9) to for the root (15)
- Assign codes:
    - E: 0
    - D: 10
    - C: 110
    - B: 1110
    - A: 1111
- Encode the data: “ABBCCCDDDDEEEEE” become ”1111111011101101101101010100000000”.

**Summary**

Data compression involves reducing the size of data by exploiting redundancies or removing less critical information. Lossless compression retains all original data, while lossy compression achieves higher compression by discarding some data. Various techniques like Huffman coding, LZW, and transform coding are employed depending on the type and requirement of the data.

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
