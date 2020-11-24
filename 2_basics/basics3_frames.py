#Frames
import tkinter
from tkinter import BOTH

#Define window
root = tkinter.Tk()
root.title('Frame Basics!')
root.iconbitmap('thinking.ico')
root.geometry('500x500')

#Example of why to use frames
#name_label = tkinter.Label(root, text='Enter your name')
#name_label.pack()
#name_button = tkinter.Button(root, text="Submit your name")
#name_button.grid(row=0, column=1)

#Define frames
pack_frame = tkinter.Frame(root, bg='red')
grid_frame_1 = tkinter.Frame(root, bg='blue')
grid_frame_2 = tkinter.LabelFrame(root, text='Grid system rules!', borderwidth=5)

#Pack frames onto root
pack_frame.pack(fill=BOTH, expand=True)
grid_frame_1.pack(fill='x', expand=True)
grid_frame_2.pack(fill=BOTH, expand=True, padx=10, pady=10)

#pack frame
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()
tkinter.Label(pack_frame, text='text').pack()

#Grid 1 layout
tkinter.Label(grid_frame_1, text='text').grid(row=0, column=0)
tkinter.Label(grid_frame_1, text='text').grid(row=1, column=1)
tkinter.Label(grid_frame_1, text='text').grid(row=2, column=2)
#tkinter.Label(grid_frame_1, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').grid(row=3, column=0)

#Grid 2 layout
tkinter.Label(grid_frame_2, text='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').grid(row=0, column=0)

#run root window's main loop
root.mainloop()