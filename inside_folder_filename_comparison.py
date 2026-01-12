import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def run_comparator():
    # Initialize tkinter and hide the main root window
    root = tk.Tk()
    root.withdraw()

    while True:
        # 1. Select the two folders
        messagebox.showinfo("Select Folders", "Please select the FIRST folder.")
        folder1 = filedialog.askdirectory(title="Select Folder 1")
        
        messagebox.showinfo("Select Folders", "Please select the SECOND folder.")
        folder2 = filedialog.askdirectory(title="Select Folder 2")

        if not folder1 or not folder2:
            messagebox.showwarning("Cancelled", "Folder selection was cancelled.")
        else:
            # 2. Read filenames from both folders
            files1 = set(os.listdir(folder1))
            files2 = set(os.listdir(folder2))

            # 3. Find common filenames
            common_files = files1.intersection(files2)

            if not common_files:
                messagebox.showinfo("Result", "No matching filenames found in both folders.")
            else:
                # 4. Ask which folder to delete from
                prompt_msg = (
                    f"Found {len(common_files)} matching files.\n\n"
                    f"Folder 1: {folder1}\n"
                    f"Folder 2: {folder2}\n\n"
                    "Type '1' to delete matches from Folder 1\n"
                    "Type '2' to delete matches from Folder 2\n"
                    "Type 'cancel' to skip deletion."
                )
                
                choice = simpledialog.askstring("Delete Choice", prompt_msg)

                if choice == '1' or choice == '2':
                    target_folder = folder1 if choice == '1' else folder2
                    
                    # Double confirmation for safety
                    confirm = messagebox.askyesno("Confirm Permanent Deletion", 
                                                f"Are you sure you want to PERMANENTLY delete these {len(common_files)} files from Folder {choice}?")
                    
                    if confirm:
                        deleted_count = 0
                        for filename in common_files:
                            file_path = os.path.join(target_folder, filename)
                            try:
                                if os.path.isfile(file_path):
                                    os.remove(file_path)
                                    deleted_count += 1
                            except Exception as e:
                                print(f"Error deleting {filename}: {e}")
                        
                        messagebox.showinfo("Success", f"Successfully deleted {deleted_count} files from Folder {choice}.")
                    else:
                        messagebox.showinfo("Cancelled", "Deletion cancelled by user.")
                else:
                    messagebox.showinfo("Skipped", "No files were deleted.")

        # 5. Continue or Exit prompt
        continue_run = messagebox.askyesno("Continue?", "Do you want to run the program again?")
        if not continue_run:
            messagebox.showinfo("Exit", "Closing the program. Goodbye!")
            break

    root.destroy()

if __name__ == "__main__":
    run_comparator()