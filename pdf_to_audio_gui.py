import PyPDF2
import pyttsx3
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Extract text from selected pages
def extract_text(pdf_path, start, end):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)

            start = max(0, start - 1)
            end = min(end, total_pages)

            text = ''
            for i in range(start, end):
                page = reader.pages[i]
                text += page.extract_text() or ""
            return text
    except Exception as e:
        messagebox.showerror("Error Reading PDF", str(e))
        return ""

# Convert text to audio
def convert_to_audio():
    pdf_path = file_path_var.get()
    if not os.path.isfile(pdf_path):
        messagebox.showerror("Invalid File", "Please select a valid PDF file.")
        return

    try:
        start = int(start_page_var.get())
        end = int(end_page_var.get())
    except:
        messagebox.showerror("Invalid Input", "Please enter valid page numbers.")
        return

    voice_id = voice_var.get()
    rate = rate_slider.get()
    volume = volume_slider.get()
    output_file = output_filename_var.get() or "output.mp3"

    status_var.set("🔄 Converting, please wait...")

    text = extract_text(pdf_path, start, end)
    if not text.strip():
        status_var.set("⚠️ No text found in selected pages.")
        return

    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_id].id)
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        status_var.set(f"✅ Saved as: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_var.set("❌ Conversion failed.")

# File picker
def browse_file():
    path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if path:
        file_path_var.set(path)

# ----- GUI SETUP -----
root = tk.Tk()
root.title("PDF to Audio Converter")
root.geometry("500x450")
root.resizable(False, False)

file_path_var = tk.StringVar()
start_page_var = tk.StringVar(value="1")
end_page_var = tk.StringVar(value="1")
voice_var = tk.IntVar(value=0)
output_filename_var = tk.StringVar(value="output.mp3")
status_var = tk.StringVar()

tk.Label(root, text="📄 Select PDF File").pack(pady=5)
tk.Entry(root, textvariable=file_path_var, width=50).pack()
tk.Button(root, text="Browse", command=browse_file).pack()

frame_range = tk.Frame(root)
frame_range.pack(pady=10)
tk.Label(frame_range, text="Start Page:").grid(row=0, column=0)
tk.Entry(frame_range, textvariable=start_page_var, width=5).grid(row=0, column=1)
tk.Label(frame_range, text="End Page:").grid(row=0, column=2)
tk.Entry(frame_range, textvariable=end_page_var, width=5).grid(row=0, column=3)

tk.Label(root, text="🎙️ Voice:").pack()
tk.Radiobutton(root, text="Male", variable=voice_var, value=0).pack()
tk.Radiobutton(root, text="Female", variable=voice_var, value=1).pack()

tk.Label(root, text="⚙️ Speed (Rate)").pack()
rate_slider = tk.Scale(root, from_=100, to=250, orient="horizontal")
rate_slider.set(150)
rate_slider.pack()

tk.Label(root, text="🔊 Volume").pack()
volume_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.1, orient="horizontal")
volume_slider.set(1.0)
volume_slider.pack()

tk.Label(root, text="💾 Output Filename (.mp3)").pack(pady=5)
tk.Entry(root, textvariable=output_filename_var, width=30).pack()

tk.Button(root, text="🚀 Convert to Audio", command=convert_to_audio).pack(pady=15)

tk.Label(root, textvariable=status_var, fg="blue").pack(pady=5)

root.mainloop()
