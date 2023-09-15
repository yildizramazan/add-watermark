import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

global image
global image_with_watermark
def open_image():
    global image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((500, 500))
        img_label.image = ImageTk.PhotoImage(image)
        img_label.config(image=img_label.image)
        add_watermark_button.config(state="normal")

def add_watermark():
    global image
    global image_with_watermark
    watermark_file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if watermark_file_path:
        watermark = Image.open(watermark_file_path)
        watermark.thumbnail((400,400))
        image_with_watermark = image.copy()
        position = (0,0)
        image_with_watermark.paste(watermark, position, watermark)
        image_with_watermark.save("watermarked_image.png")
        download_button.config(state="normal")

def download_image():
    global image_with_watermark
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        image_with_watermark.save(file_path)


window = tk.Tk()
window.title("Image Watermarking App")

open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()

img_label = tk.Label(window)
img_label.pack()

add_watermark_button = tk.Button(window, text="Add Watermark", command=add_watermark, state="disabled")
add_watermark_button.pack()

download_button = tk.Button(window, text="Download Watermarked Image", command=download_image, state="disabled")
download_button.pack()

window.mainloop()
