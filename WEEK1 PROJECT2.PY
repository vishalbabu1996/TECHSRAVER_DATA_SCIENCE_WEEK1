import tkinter as tk
from tkinter import messagebox, filedialog
import pyqrcode
import png
from PIL import Image, ImageTk

def generate_qr():
    text = entry.get()
    if not text:
        messagebox.showerror("Error", "Please enter a URL or string")
        return
    qr_code = pyqrcode.create(text)
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_code.png(file_path, scale=8)
        img = Image.open(file_path)
        img = ImageTk.PhotoImage(img)
        qr_label.config(image=img)
        qr_label.image = img
        messagebox.showinfo("Success", f"QR Code saved as {file_path}")
window = tk.Tk()
window.title("QR Code Generator")
tk.Label(window, text="Enter URL or String:").pack(pady=10)
entry = tk.Entry(window, width=50)
entry.pack(pady=5)
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)
qr_label = tk.Label(window)
qr_label.pack(pady=10)
window.mainloop()