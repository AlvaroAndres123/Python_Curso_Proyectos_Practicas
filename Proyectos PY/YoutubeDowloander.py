from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()
root.config(bd=15)
root.title("Descargador de Videos")

imagen = PhotoImage(file="gato.png")
foto = Label(root, image=imagen, bd = 0)
foto.grid(row= 0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_command(Label="Salir", command=root.destroy)

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download() 
    except:
     print("Hubo un error descargado el video")
    print("Esta descarga esta completa")

link = input("Pon tu link aqui !! URL: ")
Download(link)