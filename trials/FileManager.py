from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import easygui
import shutil
import os

pad = 5

manager = Tk()
manager.geometry('300x500')
manager.title('Custom File Manager')


def window():
    value = easygui.fileopenbox()
    return value


def file():
    w1 = window()
    try:
        os.startfile(w1)

    except FileNotFoundError:
        mb.showinfo('failed!', "File not found!")


def copy_file():
    file1 = window()
    file2 = filedialog.askdirectory()
    shutil.copy(file1, file2)
    mb.showinfo('congrats', "File Copied")


def delete_file():
    file1 = window()
    if os.path.exists(file1):
        os.remove(file1)
    else:
        mb.showinfo('failed!', "File not found !")


def rename_file():
    file1 = window()
    path1 = os.path.dirname(file1)
    ext = os.path.splitext(file1)[1]
    print("Enter new name ")
    name = input()
    path = os.path.join(path1, name + ext)
    print(path)
    os.rename(file1, path)
    mb.showinfo('congrats', "File Renamed !")


def new_folder():
    folder1 = filedialog.askdirectory()
    print("Enter name")
    name = input()
    path = os.path.join(folder1, name)
    os.mkdir(path)
    mb.showinfo('congrats', "Folder created !")


def remove_folder():
    folder1 = filedialog.askdirectory()
    os.rmdir(folder1)
    mb.showinfo('congrats', "Folder Deleted !")


def list_files():
    flist = filedialog.askdirectory()
    sorts = sorted(os.listdir(flist))
    j = 0
    print("Files in ", flist, "are-")
    while j < len(sorts):
        print(sorts[j] + '\n')
        j += 1


frame = Frame(manager)
frame.pack(pady=pad * 4)
Label(frame, text=" File Manager", bg="lightblue").pack()
frame1 = Frame(manager)
frame1.pack(pady=pad * 4)
Button(frame1, text="Open", command=file, bd=1, cursor="hand2").pack(pady=pad * 2)
Button(frame1, text="Copy", command=copy_file, bd=1, cursor="hand2").pack(pady=pad * 2)
Button(frame1, text="Delete", command=delete_file, bd=1, cursor="hand2").pack(pady=pad * 2)
Button(frame1, text="Rename", command=rename_file, bd=1, cursor="hand2").pack(pady=pad * 2)
frame2 = Frame(manager)
frame2.pack(pady=pad * 3)
Button(frame2, text="new Folder", command=new_folder, bd=1, cursor="hand2").pack(pady=pad * 2)
Button(frame2, text="Remove a Folder", command=remove_folder, bd=1, cursor="hand2").pack(pady=pad * 2)
Button(frame2, text="List all Files", command=list_files, bd=1, cursor="hand2").pack(pady=pad * 2)
manager.mainloop()
