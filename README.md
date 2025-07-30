# 🎧 PDF to Audio Converter (GUI)

Convert any PDF document into spoken audio (MP3) using a sleek Python GUI!  
Just select the PDF, choose the page range, pick a voice (male/female), and let it talk! 🎙️🎧

---

## 🚀 Features

- 📄 Select any PDF file  
- 📚 Extract specific page range  
- 🎙️ Choose between Male/Female voice  
- ⚙️ Adjust speech rate and volume  
- 💾 Save audio as `.mp3`  
- 🧠 Beginner-friendly GUI using `tkinter`

---

## 🛠️ Tech Stack

- `PyPDF2` – for reading PDF content  
- `pyttsx3` – for offline text-to-speech  
- `tkinter` – for GUI components  
- `os` – for file handling

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/chiragdhawan07/pdf-to-audio-gui.git
cd pdf-to-audio-gui
```

2. Install dependencies:

```bash
pip install pyttsx3 PyPDF2
```
> 💡 Note: tkinter comes pre-installed with most Python distributions.
If you're using WSL (Windows Subsystem for Linux) or encounter ModuleNotFoundError: No module named 'tkinter', install it using:
```bash
sudo apt update && sudo apt install python3-tk -y
```
> ✅ Recommended: Run this script directly on Windows (via Command Prompt or PowerShell) for easiest setup.
---

## ▶️ How to Run

```bash
python pdf_to_audio_gui.py
```

Then use the GUI to:  
1. Select a PDF file  
2. Choose start & end pages  
3. Set voice, speed, and volume  
4. Click **"Convert to Audio"**  
5. Your `.mp3` file will be saved!

---

## 📂 Output Example

> ✅ output.mp3 saved successfully!

---

## 🤖 Author

🛠️ Powered by Python, built with passion — by [**Chirag Dhawan**](https://github.com/chiragdhawan07)

---

## ⭐ Show Some Love

If you found this useful, don’t forget to ⭐ the repo and follow for more fun Python tools!

