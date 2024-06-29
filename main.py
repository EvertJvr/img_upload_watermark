from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import easygui
import shutil
import os
from PIL import Image

pad = 5

manager = Tk()
manager.geometry('300x500')
manager.title('Custom File Manager')


def window():
    value = easygui.fileopenbox()
    return value


def open_file():
    file1 = window()
    if os.path.exists(file1):
        file_name = file1.split('.')[0]

        asset_path = './assets/'
        water_img = 'confidential(bk-s)'

        background = Image.open(f'{file1}')
        foreground = Image.open(f'{asset_path}{water_img}.jpg')

        background.paste(foreground, box=(0, 0), mask=foreground.convert('RGBA'))
        background.save(f'{file_name}(WM1).jpg')
    else:
        mb.showinfo('failed!', "File not found !")


frame = Frame(manager)
frame.pack(pady=pad * 4)
Label(frame, text=" File Manager", bg="lightblue").pack()
frame1 = Frame(manager)
frame1.pack(pady=pad * 4)
Button(frame1, text="Upload", command=open_file, bd=1, cursor="hand2").pack(pady=pad * 2)
# Button(frame1, text="Open", command=file, bd=1, cursor="hand2").pack(pady=pad * 2)
# Button(frame1, text="Copy", command=copy_file, bd=1, cursor="hand2").pack(pady=pad * 2)
# Button(frame1, text="Delete", command=delete_file, bd=1, cursor="hand2").pack(pady=pad * 2)
# Button(frame1, text="Rename", command=rename_file, bd=1, cursor="hand2").pack(pady=pad * 2)
# frame2 = Frame(manager)
# frame2.pack(pady=pad * 3)
# Button(frame2, text="new Folder", command=new_folder, bd=1, cursor="hand2").pack(pady=pad * 2)
# Button(frame2, text="Remove a Folder", command=remove_folder, bd=1, cursor="hand2").pack(pady=pad * 2)
# Button(frame2, text="List all Files", command=list_files, bd=1, cursor="hand2").pack(pady=pad * 2)
manager.mainloop()
