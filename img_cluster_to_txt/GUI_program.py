import os
import tkinter as tk
from tkinter import filedialog
from img_cluster_to_txt import ClusterToTxt
from cmd_program import convert_one_img, convert_one_folder


######
#
# HELPER FUNCTIONS SART
#
#####
def get_file_path(button):
    # Get the path to the file
    path = filedialog.askopenfilename()

    if button == "input":
        input_path.set(path)
    elif button == "output":
        output_path.set(path)


    print("path file: ", path)

def get_directory_path(button):
    # Get the path to a directory
    path = filedialog.askdirectory()

    if button == "input":
        input_path.set(path)
    elif button == "output":
        output_path.set(path)

    print("path directory: ", path)

def selected_radio_btn():
    input_btn.configure(text="Select input {}".format(v.get()))
    if v.get() == "file":
        input_btn.configure(command=lambda: get_file_path("input"))
    else:
        input_btn.configure(command=lambda: get_directory_path("input"))

converter = ClusterToTxt()
def start_convertion(input_path, output_path):
    input_path, output_path = input_path.get(), output_path.get()
    if v.get() == "file":
        convert_one_img(converter, input_path, output_path, relative=False)
    else:
        convert_one_folder(converter, input_path, output_path, relative=False)



######
#
# HELPER FUNCTIONS END
#
#####

window = tk.Tk()
window.title("IMG Clusters to txt")
window.geometry("400x400")

current_row_idx = 0

# Greeting
greeting = tk.Label(text="Welcome!")
greeting.grid(row=current_row_idx, column=0, sticky="w")
current_row_idx += 1

# Label for radio buttons
radio_btn_label = tk.Label(text="What do you want to convert?")
radio_btn_label.grid(row=current_row_idx, column=0, sticky="w")
current_row_idx += 1

# RADIO Button to select file or folder to be converted
MODES = [("File", "file"), ("Directory", "directory")]

v = tk.StringVar() # variable to hold value of selected radio button
v.set("file") # initialize


for text, mode in MODES:
    b = tk.Radiobutton(window, text=text, variable=v, value=mode, command=selected_radio_btn)
    b.grid(row=current_row_idx, column=0, sticky="w")
    current_row_idx += 1


# Labels to show paths choicen
input_path = tk.StringVar()
output_path = tk.StringVar()


# Button to select input
input_btn = tk.Button(text="Select input {}".format("file"), command=lambda: get_file_path("input"))
input_btn.grid(row=current_row_idx, column= 0, sticky="w")
current_row_idx += 1
input_label = tk.Label(textvariable=input_path).grid(row=current_row_idx, column=0, sticky="w")
current_row_idx += 1


# button to select output
output_btn = tk.Button(text="Select output {}".format("directory"), command=lambda: get_directory_path("output"))
output_btn.grid(row=current_row_idx, column= 0, sticky="w")
current_row_idx += 1
output_label = tk.Label(textvariable=output_path).grid(row=current_row_idx, column=0, sticky="w")
current_row_idx += 1


for i in range(3):
    current_row_idx += 1

# button to start the converting
convert_btn = tk.Button(text="Start converting!", command= lambda: start_convertion(input_path, output_path))
convert_btn.grid(row=current_row_idx, column=0, sticky="w")

# label to change txt to DONE when done converting





# show the window
window.mainloop()
