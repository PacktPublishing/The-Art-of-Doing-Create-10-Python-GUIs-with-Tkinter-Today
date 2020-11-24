#Images
import tkinter
from PIL import ImageTk, Image

#Define window
root = tkinter.Tk()
root.title('Image Basics!')
root.iconbitmap('thinking.ico')
root.geometry('700x700')

#Define functions
def make_image():
    '''print an image'''
    global cat_image

    #Using PIL for jpg
    cat_image = ImageTk.PhotoImage(Image.open('cat.jpg'))
    cat_label = tkinter.Label(root, image=cat_image)
    cat_label.pack()


#Basics...works for png
my_image = tkinter.PhotoImage(file='shield.png')
my_label = tkinter.Label(root, image=my_image)
my_label.pack()

my_button = tkinter.Button(root, image=my_image)
my_button.pack()

#Not for jpeg
#cat_image = tkinter.PhotoImage(file='cat.jpg')
#cat_label = tkinter.Label(root, image=cat_image)
#cat_label.pack()

make_image()

#Run root window's main loop
root.mainloop()