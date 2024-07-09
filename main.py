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

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold", bg="white", width=18,bd=5,relief=GROOVE)

label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)


combo2=ttk.Combobox(root,values=languageV, font="RobotV 14",state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="ENGLISH",font="segoe 30 bold", bg="white", width=18,bd=5,relief=GROOVE)

label2.place(x=620,y=50)


root.configure(bg="white")
root.mainloop()
