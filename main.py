from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob


root=Tk()
root.title("Google Translator")
root.geometry("1080x400")

#icon
image_icon=PhotoImage(file="google.png")
root.iconphoto(False,image_icon)

root.configure(bg="white")
root.mainloop()
