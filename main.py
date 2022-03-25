import instaloader
from tkinter import *

root = Tk()
root.geometry('1000x550')
root.resizable()
root.config(background='black')
root.bbox()
root.title("Sayantan's Insta Dp downloader")

Label(root, text='\nDownload any instagram dp', fg='white', bg='black', font='Centaur 70 ').pack()

u_name = StringVar()

Label(root, text='\nUsername:', fg='white', bg='black', font='Centaur 50 ').pack()
Entry(root, width=100, textvariable=u_name).pack()
Label(root, text='\n', fg='white', bg='black', font='Centaur 15').pack()


def downloader():
    ig = instaloader.Instaloader()
    dp = u_name.get()
    ig.download_profile(dp, profile_pic_only=True)
    Label(root, text='\nDOWNLOADED', fg='white', bg='black', font='Centaur 25').pack()


Button(root, text='DOWNLOAD', fg='white', font='Centaur 35 ', bg='deep pink', padx=2, command=downloader).pack()

mainloop()
