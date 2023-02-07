import tkinter as tk
from tkinter import filedialog
import pyglet

# function to select a file and start playing it
def select_file():
    # global variable to keep track of player state
    global player_state
    # open a file dialog to select a file
    filename = filedialog.askopenfilename(title = "Select a file", filetypes = (("mp3 files", "*.mp3"), ("all files", "*.*")))
    # load the selected file using pyglet
    source = pyglet.media.load(filename)
    player.queue(source)
    # start playing the file
    start_player()
    # update the play button text and command
    play_button.config(text="Stop", command=stop_player)

# function to start playing the audio file
def start_player():
    # global variable to keep track of player state
    global player_state
    player.play()
    player_state = "playing"
    # update the play button text and command
    play_button.config(text="Stop", command=stop_player)

# function to stop playing the audio file
def stop_player():
    # global variable to keep track of player state
    global player_state
    player.pause()
    player_state = "paused"
    # update the play button text and command
    play_button.config(text="Play", command=start_player)

# function to change the volume
def volume_change(val):
    # calculate the volume as a float value between 0 and 1
    volume = float(val) / 100
    player.volume = volume



# create the main window
root = tk.Tk()
root.title("PyTune")
root.iconbitmap("icon.ico")

# global variable to keep track of player state
player_state = "paused"

# create labels, entry fields, and buttons
path_label = tk.Label(root, text="File path:")
path_label.grid(row=0, column=0)

path_entry = tk.Entry(root)
path_entry.grid(row=0, column=1)

open_button = tk.Button(root, text="Open", command=select_file)
open_button.grid(row=0, column=2)

# add a label to display the image
image_label = tk.Label(root, text="Image Preview:")
image_label.grid(row=1, column=0)

# create a default image
image = tk.PhotoImage()

# create a label to display the image
img_preview = tk.Label(root, image=image)
img_preview.grid(row=2, column=0, columnspan=2)

play_button = tk.Button(root, text="Play", command=start_player)
play_button.grid(row=1, column=0)

# add a function to open an image file
def select_image():
    filename = filedialog.askopenfilename(title="Select an image", filetypes=(("image files", "*.jpg;*.png"), ("all files", "*.*")))
    img = tk.PhotoImage(file=filename)
    img_preview.config(image=img)
    img_preview.image = img

# add a button to select an image
image_button = tk.Button(root, text="Select Image", command=select_image)
image_button.grid(row=3, column=1)

volume_button = tk.Button(root, text="Volume", command=lambda: volume_scale.set(player.volume*100))
volume_button.grid(row=1, column=1)

volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=volume_change)
volume_scale.set(50)
volume_scale.grid(row=2, column=0, columnspan=2, sticky="ew")

# create the player
player = pyglet.media.Player()

# start the main event loop
root.mainloop()
