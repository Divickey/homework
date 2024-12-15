from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("500x1000")
root.title("bibliotheek")

title = Label(root, text="library", font= font.Font(font = 12), fg="light gray")
title.grid(row = 0, column = 1)

inputtitle = Label(root, text="add a book : ")
inputtitle.grid(row = 2, column = 1)

bookinput = Entry(root)
bookinput.grid(row=2, column = 2)

inputconfirm = Button(root, text="confirm", fg="black", bg="light green")
inputconfirm.grid(row = 2, column=3)

root.mainloop()