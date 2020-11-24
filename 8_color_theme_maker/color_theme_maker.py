#Color Theme Maker
import tkinter
from tkinter import BOTH, IntVar, DISABLED, filedialog

#Define window
root = tkinter.Tk()
root.title('Color Theme Maker')
root.iconbitmap('color_wheel.ico')
root.geometry('450x500')
root.resizable(0,0)

#Define fonts and colors
#NONE:  Using system defaults

#Define functions
def get_red(slider_value):
    """Turn current slider value for red into a hex value and update color.
    The scale value is passed automatically when the scale is moved calling the get_red function."""
    global red_value

    #Turn the slider value into an int and hex value. Strip leading chars so only two remain
    red_value = hex(int(slider_value))
    red_value = red_value.lstrip("0x")

    #If hex value is single digit, lead with a 0 such that d becomes 0d
    while len(red_value) < 2:
        red_value = "0" + str(red_value)

    update_color()


def get_green(slider_value):
    """Turn current slider value for green into a hex value and update color.
    The scale value is passed automatically when the scale is moved calling the get_green function."""
    global green_value

    #Turn the slider value into an int and hex value. Strip leading chars so only two remain
    green_value = hex(int(slider_value))
    green_value = green_value.lstrip("0x")

    #If hex value is single digit, lead with a 0 such that d becomes 0d
    while len(green_value) < 2:
        green_value = "0" + str(green_value)
        
    update_color()


def get_blue(slider_value):
    """Turn current slider value for blue into a hex value and update color.
    The scale value is passed automatically when the scale is moved calling the get_blue function."""
    global blue_value

    #Turn the slider value into an int and hex value. Strip leading chars so only two remain
    blue_value = hex(int(slider_value))
    blue_value = blue_value.lstrip("0x")

    #If hex value is single digit, lead with a 0 such that d becomes 0d
    while len(blue_value) < 2:
        blue_value = "0" + str(blue_value)
        
    update_color()


def update_color():
    """UPdate the current color box based on the slider values.  Display tuple and hex values of the current color"""
    #Make the color box smaller than the original due to ipadx and ipday on the original color box
    color_box = tkinter.Label(input_frame, bg="#" + red_value + green_value + blue_value, height=6, width=15)
    color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10)

    #Display the tuple and hex value for the given color
    color_tuple.config(text='(' + str(red_slider.get()) + '),' + '(' + str(green_slider.get()) + '),' + '(' + str(blue_slider.get()) + ')')
    color_hex.config(text="#" + red_value + green_value + blue_value)


def set_color(r,g,b):
    """Set a given color"""
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)


def store_color():
    """Store the current color tuple value and display color"""
    global stored_colors

    #Get the current value of each slider and append 0's to keep formatting
    red = str(red_slider.get())
    while len(red) < 3:
        red = "0" + red
    
    green = str(green_slider.get())
    while len(green) < 3:
        green = "0" + green

    blue = str(blue_slider.get())
    while len(blue) < 3:
        blue = "0" + blue

    #Keep a reference of the current color
    stored_red = red_slider.get()
    stored_green = green_slider.get()
    stored_blue = blue_slider.get()

    #Create new widgets for the stored color.
    recall_button = tkinter.Button(output_frame, text="Recall Color", command=lambda:set_color(stored_red, stored_green, stored_blue))
    new_color_tuple = tkinter.Label(output_frame, text='(' + red + '),' + '(' + green + '),' + '(' + blue + ')') 
    new_color_hex = tkinter.Label(output_frame, text='#' + red_value + green_value + blue_value)
    new_color_black_box = tkinter.Label(output_frame, bg='black', width=3, height=1)
    new_color_box = tkinter.Label(output_frame, bg="#"+ red_value + green_value + blue_value, width=3, height=1) 

    #Put new widgets on the screen
    recall_button.grid(row=stored_color.get(), column=1, padx=20)
    new_color_tuple.grid(row=stored_color.get(), column=2, padx=20)
    new_color_hex.grid(row=stored_color.get(), column=3, padx=20)
    new_color_black_box.grid(row=stored_color.get(), column=4, pady=2, ipadx=5, ipady=5)
    new_color_box.grid(row=stored_color.get(), column=4)

    #Update the dict stored_colors with the new color tuple and hex values
    stored_colors[stored_color.get()] = [new_color_tuple.cget("text"), new_color_hex.cget("text")]

    #Move the radio button stored colors_ to the next value if available
    if stored_color.get() < 5:
        stored_color.set(stored_color.get() + 1)


def save_colors():
    """Output the chosen colors to a txt file."""
    #Get the directory where the user would like to save
    file_name = filedialog.asksaveasfilename(initialdir='./', title='Save Colors', filetypes=(('Text', '.txt'),('All Files', '*.*')))

    #open the new file as write
    with open(file_name, "w") as f:
        f.write("Color Theme Maker Output\n")
        for saved_entry in stored_colors.values():
            f.write(saved_entry[0] + "\n" + saved_entry[1] + "\n\n")
    

#Define Layout
input_frame = tkinter.LabelFrame(root, padx=5, pady=5)
output_frame = tkinter.LabelFrame(root, padx=5, pady=5)
input_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
output_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

#Setting up the input frame.
#Create the labels, sliders, and buttons for each color RGB
red_label = tkinter.Label(input_frame, text="R")
red_slider = tkinter.Scale(input_frame, from_=0, to=255, command=get_red)
red_button = tkinter.Button(input_frame, text="Red", command=lambda:set_color(255,0,0))
green_label = tkinter.Label(input_frame, text="G")
green_slider = tkinter.Scale(input_frame, from_=0, to=255, command=get_green)
green_button = tkinter.Button(input_frame, text="Green", command=lambda:set_color(0,255,0))
blue_label = tkinter.Label(input_frame, text="B")
blue_slider = tkinter.Scale(input_frame, from_=0, to=255, command=get_blue)
blue_button = tkinter.Button(input_frame, text="Blue", command=lambda:set_color(0,0,255))

#Create buttons for each complimentary color
yellow_button = tkinter.Button(input_frame, text="Yellow", command=lambda:set_color(255,255,0))
cyan_button = tkinter.Button(input_frame, text="Cyan", command=lambda:set_color(0,255,255))
magenta_button = tkinter.Button(input_frame, text="Magenta", command=lambda:set_color(255,0,255))

#Create utility buttons
store_button = tkinter.Button(input_frame, text="Store Color", command=store_color)
save_button = tkinter.Button(input_frame, text="Save", command=save_colors)
quit_button = tkinter.Button(input_frame, text="Quit", command=root.destroy)

#Put labels, sliders, and buttons on to the frame....Use ipadx with rbg buttons to define column width, then use sticky on others
red_label.grid(row=0, column=0, sticky='W')
red_slider.grid(row=1, column=0, sticky='W')
red_button.grid(row=2, column=0, padx=1, pady=1, ipadx=20)
green_label.grid(row=0, column=1, sticky='W')
green_slider.grid(row=1, column=1, sticky='W')
green_button.grid(row=2, column=1, padx=1, pady=1, ipadx=15)
blue_label.grid(row=0, column=2, sticky='W')
blue_slider.grid(row=1, column=2, sticky='W')
blue_button.grid(row=2, column=2, padx=1, pady=1, ipadx=18)
yellow_button.grid(row=3, column=0, padx=1, pady=1, sticky="WE")
cyan_button.grid(row=3, column=1, padx=1, pady=1, sticky="WE")
magenta_button.grid(row=3, column=2, padx=1, pady=1, sticky="WE")
store_button.grid(row=4, column=0, columnspan=3, padx=1, pady=1, sticky="WE")
save_button.grid(row=4, column=3, padx=1, pady=1, sticky="WE")
quit_button.grid(row=4, column=4, padx=1, pady=1, sticky="WE")

#Create the color box and color labels
color_box = tkinter.Label(input_frame, bg='black', height=6, width=15)
color_tuple = tkinter.Label(input_frame, text='(0), (0), (0)')
color_hex = tkinter.Label(input_frame, text='#000000')

#Put the color box and labels on the frame. 
color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10, ipadx=10, ipady=10)
color_tuple.grid(row=2, column=3, columnspan=2)
color_hex.grid(row=3, column=3, columnspan=2)

#Setting up the output frame
#Initialize a dictionary to hold all stored colors
stored_colors = {}
stored_color = IntVar()

#Create radio buttons to select stored colors and populate each row with placeholder values
for i in range(6):
    radio = tkinter.Radiobutton(output_frame, variable=stored_color, value=i)
    radio.grid(row=i, column=0, sticky='W')

    recall_button = tkinter.Button(output_frame, text="Recall Color", state=DISABLED)
    new_color_tuple = tkinter.Label(output_frame, text="(255), (255), (255)")
    new_color_hex = tkinter.Label(output_frame, text="#ffffff")
    new_color_black_box = tkinter.Label(output_frame, bg="black", width=3, height=1)
    new_color_box = tkinter.Label(output_frame, bg='white', width=3, height=1)

    recall_button.grid(row=i, column=1, padx=20)
    new_color_tuple.grid(row=i, column=2, padx=20)
    new_color_hex.grid(row=i, column=3, padx=20)
    new_color_black_box.grid(row=i, column=4, pady=2, ipadx=5, ipady=5)
    new_color_box.grid(row=i, column=4)

    #.cget() returns the value of a specific option.  Store the text value of the tuple label and hex label
    stored_colors[stored_color.get()] = [new_color_tuple.cget('text'), new_color_hex.cget('text')]

#Initialize the starting values for the color box display
red_value = "00"
green_value = "00"
blue_value = "00"

#Run the root window's main loop
root.mainloop()