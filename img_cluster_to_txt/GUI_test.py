import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("IMG Clusters to txt")
window.geometry("400x400")

# Greeting
greeting = tk.Label(text="Welcome!")
greeting.grid(row=0, column=0)

# RADIO Button to select file or folder to be converted
MODES = [("File", "F"), ("Directory", "D")]

v = tk.StringVar()
v.set("L") # initialize

radio_btn_idx = 1
for text, mode in MODES:
    b = tk.Radiobutton(window, text=text, variable=v, value=mode)
    b.grid(row=radio_btn_idx, column=0)
    radio_btn_idx += 1


# Button to select input
input_btn = tk.Button(text="Select input {}".format("test"))

# button to select output


######
#
# HELPER FUNCTIONS
#
#####

def get_file_path():
    # Get the path to the file 
    path = filedialog.askopenfilename()
    print("path file: ", path)

def get_directory_path():
    # Get the path to a directory
    path = filedialog.askdirectory()
    print("path directory: ", path)



# show the window
window.mainloop()