from tkinter import *
from pygame import mixer

mixer.init()

root = Tk()
root.geometry('300x400')
root.title("bhuplayer")
root.iconbitmap('33a8d8c4 (1).bmp')


menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "file" ,menu = subMenu)
subMenu.add_command(label = "New Notebook")
subMenu.add_command(label = "open...")
subMenu.add_command(label = "save and checkpoint")


text = Label(root, text = "let's make some noise")
text.pack()


photo = PhotoImage("file =C:/Users/RUHIT/Documents/_MG_4605.jpg")


def play_button():
    mixer.music.load("C:/Users/RUHIT/Documents/Aashiq.mp3")
    mixer.music.play()


def stop_button():
    mixer.music.stop()
def set_vol(val):
    mixer.music.set_volume(int(val)/100)
button_photo = PhotoImage(file = 'play.png')
playBtn = Button(root, image=button_photo, command = play_button)
stopBtn = Button(root, text = "stop", command = stop_button)
playBtn.pack()
stopBtn.pack()


scale=Scale(root, from_=0, to=100, orient = HORIZONTAL, command_=set_vol)
scale.set(45)
scale.pack()


root.mainloop()
