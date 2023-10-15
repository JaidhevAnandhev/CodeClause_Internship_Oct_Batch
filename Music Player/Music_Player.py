# Importing Libraries
import os
from tkinter import *
from tkinter import filedialog

import pygame
from pygame import mixer

# It helps to display the root window and manages all the other components of the tkinter application
root = Tk()

# Title of the window and it's design configurations
root.title("Music Player")
root.configure(background="#333333")
root.geometry("485x700+290+10")
root.resizable(False, False)

# mixer.init() is a function that starts the mixer in Pygame
mixer.init()

# Create a GIF animation in Tkinter
frameCnt = 40
frames = [PhotoImage(file="Music_sound_bgm (1).gif", height=450, width=600, format='gif -index %i' % i) for i in
          range(frameCnt)]


# Set frames for the GIF Animation and it is called after every 40ms
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)


label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)


# It asks for the folder location and if the file ends with (.mp3) extension then only those files are displayed
def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


lower_frame = Frame(root, bg="#FFFFFF", width=490, height=150)
lower_frame.place(x=0, y=400)

# Application icon is set
image_icon = PhotoImage(file="player.png")
root.iconphoto(False, image_icon)

# Background for the Menu is set
Menu = PhotoImage(file="download.png")
Label(root, image=Menu).place(x=0, y=500, width=485, height=200)
FrameMusic = Frame(root, bd=2, relief=RIDGE)
FrameMusic.place(x=0, y=585, width=485, height=100)


# Function to play the music
def PlayMusic():
    Playlist.get(ACTIVE)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


# Function to pause the music
def PauseMusic():
    # Paused Song
    pygame.mixer.music.pause()


# Button set to play the music
ButtonPlay = PhotoImage(file="play2.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height=40, width=40, command=PlayMusic).place(x=215, y=487)

# Button set to stop the music
ButtonStop = PhotoImage(file="stop2.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height=40, width=40, command=mixer.music.stop).place(x=140, y=487)

# Button set to pause the music
ButtonPause = PhotoImage(file="pause2.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height=40, width=40, command=PauseMusic).place(x=290, y=487)

#  Button to browse the folder or file location
Button(root, text="Browse Musics🔎", width=39, height=1, font=("magneto", 12, "bold"), fg="Black", bg="#EEEEEE",
       command=AddMusic).place(x=0, y=550)

Scroll = Scrollbar(FrameMusic)

# To list the songs in the playlist
Playlist = Listbox(FrameMusic, width=100, font=("Britannic Bold", 10), fg="grey", bg="#333333",
                   selectbackground="light green", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.xview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# It executes what we need to execute in the window
root.mainloop()
