from PIL import Image
from tkinter import filedialog
import tkinter as tk


# create a Tkinter root window
root = tk.Tk()
root.withdraw()


# use file dialog box to allow the user to select the target image
target_path = filedialog.askopenfilename(
    title="Insert your victim", filetypes=[("JPEG files", "*.jpg")]
)


# use file dialog box to allow the user to select the good guy image
good_guy_path = filedialog.askopenfilename(
    title="Select good guy image", filetypes=[("JPEG files", "*.jpg")]
)


# open the target image and resize it to 50x50 pixels
target_image = Image.open(target_path)
target_image = target_image.resize((50, 50))


# open the good guy image and resize it to 50x50 pixels
good_guy_image = Image.open(good_guy_path)
good_guy_image = good_guy_image.resize((50, 50))
