import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

def decompress_file(compressed_file_path, destination_folder):
    try:
        shutil.unpack_archive(compressed_file_path, destination_folder)
        messagebox.showinfo("Success", f"File decompressed successfully to {destination_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decompress file: {str(e)}")

def select_file_and_decompress():
    root = tk.Tk()
    root.withdraw()

    compressed_file_path = filedialog.askopenfilename(title="Select Compressed Folder", filetypes=(("zip files", "*.zip"), ("all files", "*.*")))
    if not compressed_file_path:
        messagebox.showinfo("Cancelled", "Operation Cancelled")
        return

    destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    if not destination_folder:
        messagebox.showinfo("Cancelled", "Operation Cancelled")
        return

    destination_folder = os.path.join(destination_folder, os.path.basename(compressed_file_path).split(".")[0])

    decompress_file(compressed_file_path, destination_folder)

    if messagebox.askyesno("Delete Original", "Do you want to delete the original compressed file?"):
        os.remove(compressed_file_path)
        messagebox.showinfo("Deleted", "Original compressed file has been deleted.")

    root.destroy()

if __name__ == "__main__":
    select_file_and_decompress()