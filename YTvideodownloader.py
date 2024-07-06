import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import ssl

# Set SSL context to ignore certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

def browse_path():
    download_path.set(filedialog.askdirectory())

def download_video():
    try:
        url = link.get()
        yt = YouTube(url)

        # Get available streams based on the selected resolution
        selected_res = resolution.get()
        if selected_res == "720p":
            stream = yt.streams.filter(progressive=True, res="720p").first()
        elif selected_res == "480p":
            stream = yt.streams.filter(progressive=True, res="480p").first()
        elif selected_res == "360p":
            stream = yt.streams.filter(progressive=True, res="360p").first()
        else:
            stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(download_path.get())
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Link input
tk.Label(root, text="YouTube Link:").grid(row=0, column=0, padx=10, pady=10)
link = tk.StringVar()
tk.Entry(root, textvariable=link, width=50).grid(row=0, column=1, padx=10, pady=10)

# Resolution options
tk.Label(root, text="Resolution:").grid(row=1, column=0, padx=10, pady=10)
resolution = tk.StringVar(value="720p")
tk.OptionMenu(root, resolution, "720p", "480p", "360p", "Highest Available").grid(row=1, column=1, padx=10, pady=10)

# Download path
tk.Label(root, text="Download Path:").grid(row=2, column=0, padx=10, pady=10)
download_path = tk.StringVar()
tk.Entry(root, textvariable=download_path, width=50).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_path).grid(row=2, column=2, padx=10, pady=10)

# Download button
tk.Button(root, text="Download", command=download_video).grid(row=3, column=1, pady=20)

# Start the GUI event loop
root.mainloop()
