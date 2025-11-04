import os
import shutil
from tkinter import Tk, filedialog, Label, Button, Frame, messagebox, Text, Scrollbar, END, RIGHT, Y

# ---------------------------- File Categories ----------------------------
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Music': ['.mp3', '.wav', '.aac', '.ogg'],
    'Compressed': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Programs': ['.py', '.exe', '.js', '.html', '.css', '.cpp', '.c', '.java']
}

# ---------------------------- Core Logic ----------------------------
def organize_files(folder_path):
    if not folder_path:
        messagebox.showwarning("⚠️ Warning", "Please select a folder first!")
        return

    files = os.listdir(folder_path)
    if len(files) == 0:
        messagebox.showinfo("ℹ️ Info", "The selected folder is empty.")
        return

    display_box.delete(1.0, END)  # Clear previous log
    category_count = {key: 0 for key in FILE_CATEGORIES.keys()}
    category_count['Others'] = 0
    organized_count = 0

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)
            file_type = "Others"
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if extension.lower() in extensions:
                    file_type = category
                    category_path = os.path.join(folder_path, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, file))
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(folder_path, 'Others')
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, file))

            category_count[file_type] += 1
            organized_count += 1
            display_box.insert(END, f"✅ {file_type} → {file}\n")
            display_box.see(END)
            root.update()  # Refresh GUI live

    # ---------------------------- Summary ----------------------------
    display_box.insert(END, "\n" + "-"*55 + "\n")
    display_box.insert(END, "📊 SUMMARY REPORT\n")
    display_box.insert(END, "-"*55 + "\n")
    for cat, count in category_count.items():
        display_box.insert(END, f"{cat}: {count} files\n")
    display_box.insert(END, "-"*55 + "\n")
    display_box.insert(END, f"Total Organized: {organized_count} files ✅\n")
    display_box.see(END)
    messagebox.showinfo("✅ Done", f"Successfully organized {organized_count} files!\nCheck summary below.")

# ---------------------------- Folder Selection ----------------------------
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_label.config(text=f"📁 Selected Folder: {folder_selected}", fg="#333")
        organize_files(folder_selected)

# ---------------------------- GUI SETUP ----------------------------
root = Tk()
root.title("✨ Smart File Organizer")

# ---- Make window adaptive ----
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
root.geometry(f"{window_width}x{window_height}+100+50")
root.resizable(True, True)
root.config(bg="#E6F4F1")

# Header
header = Label(root, text="📂 Smart File Organizer", font=("Segoe UI", 18, "bold"),
               bg="#007B83", fg="white", pady=10)
header.pack(fill="x")

# Main frame
frame = Frame(root, bg="#E6F4F1")
frame.pack(pady=15)

Label(frame, text="Organize your messy folders instantly!", font=("Segoe UI", 12),
      bg="#E6F4F1", fg="#333").pack(pady=5)

Button(frame, text="Select Folder to Organize", command=select_folder,
       font=("Segoe UI", 12, "bold"), bg="#007B83", fg="white",
       activebackground="#005C61", activeforeground="white",
       padx=20, pady=10, relief="flat", borderwidth=0).pack(pady=10)

folder_label = Label(frame, text="No folder selected yet", font=("Segoe UI", 10),
                     bg="#E6F4F1", fg="#666")
folder_label.pack(pady=5)

# Output Log Area
Label(root, text="Activity Log:", font=("Segoe UI", 11, "bold"),
      bg="#E6F4F1", fg="#333").pack()

text_frame = Frame(root, bg="#E6F4F1")
text_frame.pack(pady=5, expand=True)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)

display_box = Text(text_frame, height=18, width=90, font=("Consolas", 10),
                   yscrollcommand=scrollbar.set, bg="white", fg="#222", wrap="word")
display_box.pack(expand=True, fill="both")

scrollbar.config(command=display_box.yview)

# Footer
footer = Label(root, text="✨ Developed by Kumar Prathmesh | Python Project 🐍",
               font=("Segoe UI", 10, "italic"), bg="#E6F4F1", fg="#555")
footer.pack(side="bottom", pady=10)

root.mainloop()

