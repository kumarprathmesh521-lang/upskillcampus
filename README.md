🗂️ File Organizer
✨ A simple Python tool to keep your folders clean and organized

Have you ever opened your Downloads folder and felt overwhelmed by the mess of files — images, PDFs, videos, and random stuff everywhere?
The File Organizer is here to fix that. It’s a lightweight Python app that automatically sorts your files into neat, categorized folders — saving you time and frustration.

🚀 What It Does

Scans any folder you choose

Detects file types automatically

Creates folders like Images, Documents, Videos, etc.

Moves files into the right folders — safely and quickly

Keeps your directory clean and structured

Works offline — your files never leave your computer

💡 Why I Built This

I often had dozens of files cluttering my Downloads folder — documents mixed with screenshots, ZIP files, and videos.
Manually sorting them every week was annoying, so I decided to automate it.
This project started as a small experiment in file handling and grew into a tool I now use regularly.

🧩 How It Works

You select a folder (like Downloads or Desktop).

The program scans all files in that folder.

It groups files by type (like .jpg, .pdf, .mp4, etc.).

If a folder doesn’t exist, it creates one.

Files are moved neatly into their respective folders.

You end up with a clean, organized directory!

⚙️ Installation

Make sure you have Python 3 installed on your system.

# Clone this repository
git clone https://github.com/yourusername/file-organizer.git

# Move into the project folder
cd file-organizer

# Run the script
python file_organizer.py


Once you run it, a small GUI window will appear — just pick the folder you want to clean up and click Organize Files.
That’s it. The program does the rest.

📁 Example

Before:

Downloads/
├── photo1.jpg
├── report.pdf
├── video.mp4
├── notes.txt


After:

Downloads/
├── Images/
│   └── photo1.jpg
├── Documents/
│   └── report.pdf
├── Videos/
│   └── video.mp4
├── Text/
│   └── notes.txt


Your messy folder becomes a clean, well-sorted one in seconds. 🧹

🧠 Built With

Python 3

os – for directory navigation

shutil – for moving files safely

tkinter – for a simple graphical interface

time – for logging and timing operations

🌱 Future Improvements

There’s a lot more I want to add in the future:

Detect and remove duplicate files

Option to undo file moves

Real-time background organizing

Cloud storage and network folder support

Machine learning–based smart file classification

🧑‍💻 Author

Kumar Prathmesh
