import tkinter as tk
from tkinter import filedialog
import pyglet

def select_file():
    global player_state
    filename = filedialog.askopenfilename(title = "Select a file", filetypes = (("mp3 files", "*.mp3"), ("all files", "*.*")))
    source = pyglet.media.load(filename)
    player.queue(source)
    start_player()
    play_button.config(text="Stop", command=stop_player)

def start_player():
    global player_state
    player.play()
    player_state = "playing"
    play_button.config(text="Stop", command=stop_player)

def stop_player():
    global player_state
    player.pause()
    player_state = "paused"
    play_button.config(text="Play", command=start_player)

def volume_change(val):
    volume = float(val) / 100
    player.volume = volume

root = tk.Tk()
root.title("PyTune")
player_state = "paused"

path_label = tk.Label(root, text="File path:")
path_label.grid(row=0, column=0)

path_entry = tk.Entry(root)
path_entry.grid(row=0, column=1)

open_button = tk.Button(root, text="Open", command=select_file)
open_button.grid(row=0, column=2)

play_button = tk.Button(root, text="Play", command=start_player)
play_button.grid(row=1, column=0)

volume_button = tk.Button(root, text="Volume", command=lambda: volume_scale.set(player.volume*100))
volume_button.grid(row=1, column=1)

volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=volume_change)
volume_scale.set(50)
volume_scale.grid(row=2, column=0, columnspan=2, sticky="ew")

player = pyglet.media.Player()

root.mainloop()

