import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

def compress_folder(folder_to_compress, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    archive_name = os.path.join(destination_folder, os.path.basename(folder_to_compress))
    shutil.make_archive(archive_name, 'zip', folder_to_compress)
    return f"Folder compressed successfully into {archive_name}.zip"

def select_folder_and_compress():
    root = tk.Tk()
    root.withdraw() 
    folder_to_compress = filedialog.askdirectory(title="Select Folder to Compress")

    if folder_to_compress:
        try:
            destination_folder = "/Users/nephthalisalam/Documents/Compressed_Folders"
            result_message = compress_folder(folder_to_compress, destination_folder)
            messagebox.showinfo("Success", result_message)

            if messagebox.askyesno("Delete Original", "Do you want to delete the original folder after compressing?"):
                shutil.rmtree(folder_to_compress)
                messagebox.showinfo("Deleted", "Original folder has been deleted.")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showinfo("Cancelled", "Operation Cancelled")
    root.destroy()

if __name__ == "__main__":
    select_folder_and_compress()