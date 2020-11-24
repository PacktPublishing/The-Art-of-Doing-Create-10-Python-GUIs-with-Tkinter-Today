#Gravity Simulator
import tkinter
from tkinter import BOTH, HORIZONTAL, CURRENT, END
from matplotlib import pyplot

#Define window
root = tkinter.Tk()
root.title('Gravity Simulator')
root.iconbitmap('earth.ico')
root.geometry('500x650')
root.resizable(0,0)

#Define fonts and colors
#NONE use system defualts

#Define global variables
time = 0
data = {}
for i in range(1,5):
    data['data_%d' % i] = []

#Define functions
def move(event):
    """Drag the balls vertically on the canvas to set the position."""
    #If the current object clicked has the "BALL" tag, we should allow it to be moved.
    if "BALL" in main_canvas.gettags(CURRENT):
        #Record the x position of the ball and keep it the same.
        x1 = main_canvas.coords(CURRENT)[0]
        x2 = main_canvas.coords(CURRENT)[2]

        #Change the coords of the CURRENT object based on the event.y position of the mouse.  Recall the ball has size 10
        main_canvas.coords(CURRENT, x1, event.y, x2, event.y+10)
        
        #Attempt to not move the ball off the canvas.  CURRENT[3] is y2 coord
        #Above the top of the screen
        if main_canvas.coords(CURRENT)[3] < 15:
            main_canvas.coords(CURRENT, x1, 5, x2, 15)
        #Below the bottom of the screen
        elif main_canvas.coords(CURRENT)[3] > 415:
            main_canvas.coords(CURRENT, x1, 405, x2, 415)

    #Update the height label for each ball
    update_height()


def update_height():
    """Update the height labels for each ball."""
    for i in range(1,5):
        heights['height_%d' % i].config(text="Height: " + str(round(415 - main_canvas.coords(balls['ball_%d' % i])[3], 2)))


def step(t):
    """Advance the ball one 'step' based on time_slider value of t"""
    global time

    #loop through all 4 balls
    for i in range(1,5):
        #DO THE PHYSICS!  Negate a and v because canvas y values increase as you move down.
        a = -1*float(accelerations['a_%d' % i].get())
        v = -1*float(velocities['v_%d' % i].get())
        d = v*t + .5*a*t**2

        #Get the x coords for the current ball.  These remain constant
        x1 = main_canvas.coords(balls['ball_%d' % i])[0]
        x2 = main_canvas.coords(balls['ball_%d' % i])[2]

        #Move the given ball and create a dash line to mark the new position
        if main_canvas.coords(balls['ball_%d' % i])[3] + d <= 415:
            main_canvas.move(balls['ball_%d' % i], 0, d)
            y2 = main_canvas.coords(balls['ball_%d' % i])[3]
            #Draw dash line at bottom of ball
            main_canvas.create_line(x1, y2, x2, y2, tag="DASH")
        #The ball has hit the ground
        else:
            main_canvas.coords(balls['ball_%d' % i], x1, 405, x2, 415)

        #Do MORE PHYSICS
        vf = v + a*t
        #update velocity values for each ball
        velocities['v_%d' % i].delete(0, END)
        velocities['v_%d' % i].insert(0, str(round(-1*vf, 2)))

        #Add data for the step to the data dict
        data['data_%d' % i].append((time, 415 - main_canvas.coords(balls['ball_%d' % i])[3]))
    
    #Update heights for the given time interval
    update_height()

    #Update time
    time += t


def run():
    """RUn the entire sim until all balls are at the ground or above the screen."""
    #Balls may start on the ground or at the top of the screen so call step() at least once
    step(t_slider.get())

    #Run step() until ALL balls have hit the ground or left the screen based of the y2 coord [3]
    while 15 < main_canvas.coords(balls['ball_1'])[3] < 415 or 15 < main_canvas.coords(balls['ball_2'])[3] < 415 or 15 < main_canvas.coords(balls['ball_3'])[3] < 415 or 15 < main_canvas.coords(balls['ball_4'])[3] < 415:
        step(t_slider.get())


def graph():
    """Graph distance v time for 4 balls."""
    #Colors of the balls corresponds to colors of the graph
    colors = ['red', 'green', 'blue', 'yellow']

    for i in range(1,5):
        #Initialize x,y values
        x = []
        y = []
        #Add corresponding data to x,y values
        for data_list in data['data_%d' % i]:
            x.append(data_list[0])
            y.append(data_list[1])
        #Plot data in corresponding color
        pyplot.plot(x, y, color=colors[i-1])

    #Graph formatting
    pyplot.title('Distance Vs. Time')
    pyplot.xlabel('Time')
    pyplot.ylabel('Distance')
    pyplot.show()


def reset():
    """Erase all "DASH" tags from canvas, set balls back to ground, and resent entry fields."""
    global time

    time = 0
    main_canvas.delete("DASH")

    #Clear each ball...
    for i in range(1,5):
        #Clear and set the velocity and accelerations
        velocities['v_%d' % i].delete(0, END)
        velocities['v_%d' % i].insert(0, '0')
        accelerations['a_%d' % i].delete(0, END)
        accelerations['a_%d' % i].insert(0, '0')

        #Reset ball to starting position
        main_canvas.coords(balls['ball_%d' % i], 45+(i-1)*100, 405, 55+(i-1)*100, 415)

        #Clear data
        data['data_%d' % i].clear()
    
    update_height()
    t_slider.set(1)


#Define layout
#Create frames
canvas_frame = tkinter.Frame(root)
input_frame = tkinter.Frame(root)
canvas_frame.pack(pady=10)
input_frame.pack(fill=BOTH, expand=True)

#Canvas frame layout
main_canvas = tkinter.Canvas(canvas_frame, width=400, height=415, bg='white')
main_canvas.grid(row=0, column=0, padx=5, pady=5)

line_0 = main_canvas.create_line(2,0,2,415)
line_1 = main_canvas.create_line(100,0,100,415)
line_2 = main_canvas.create_line(200,0,200,415)
line_3 = main_canvas.create_line(300,0,300,415)
line_4 = main_canvas.create_line(400,0,400,415)

balls = {}
balls['ball_1'] = main_canvas.create_oval(45, 405, 55, 415, fill='red', tag="BALL")
balls['ball_2'] = main_canvas.create_oval(145, 405, 155, 415, fill='green', tag="BALL")
balls['ball_3'] = main_canvas.create_oval(245, 405, 255, 415, fill='blue', tag="BALL")
balls['ball_4'] = main_canvas.create_oval(345, 405, 355, 415, fill='yellow', tag="BALL")

#Input frame layout
#Row labels
tkinter.Label(input_frame, text='d').grid(row=0, column=0)
tkinter.Label(input_frame, text='vi').grid(row=1, column=0)
tkinter.Label(input_frame, text='a').grid(row=2, column=0, ipadx=22)
tkinter.Label(input_frame, text='t').grid(row=3, column=0)

#Heights/Distance labels
heights = {}
for i in range(1,5):
    heights['height_%d' % i] = tkinter.Label(input_frame, text="Height: " + str(415 - main_canvas.coords(balls['ball_%d' % i])[3]))
    heights['height_%d' % i].grid(row=0, column=i)

#Velocity entry boxes
velocities = {}
for i in range(1,5):
    velocities['v_%d' % i] = tkinter.Entry(input_frame, width=15)
    velocities['v_%d' % i].grid(row=1, column=i, padx=1)
    velocities['v_%d' % i].insert(0, '0')

#Acceleration entry boxes
accelerations = {}
for i in range(1,5):
    accelerations['a_%d' % i] = tkinter.Entry(input_frame, width=15)
    accelerations['a_%d' % i].grid(row=2, column=i, padx=1)
    accelerations['a_%d' % i].insert(0, '0')

#Time slider
t_slider = tkinter.Scale(input_frame, from_=0, to=1, tickinterval=.1, resolution=.01, orient=HORIZONTAL)
t_slider.grid(row=3, column=1, columnspan=4, sticky='WE') 
t_slider.set(1)

#Buttons
step_button = tkinter.Button(input_frame, text="Step", command=lambda:step(t_slider.get()))
run_button = tkinter.Button(input_frame, text="Run", command=run)
graph_button = tkinter.Button(input_frame, text="Graph", command=graph)
reset_button = tkinter.Button(input_frame, text="Reset", command=reset)
quit_button = tkinter.Button(input_frame, text="Quit", command=root.destroy)

step_button.grid(row=4, column=1, pady=(10,0), sticky="WE")
run_button.grid(row=4, column=2, pady=(10,0), sticky="WE")
graph_button.grid(row=4, column=3, pady=(10,0), sticky="WE")
reset_button.grid(row=4, column=4, pady=(10,0), sticky="WE")
quit_button.grid(row=5, column=1, columnspan=4, sticky="WE")

#Make each ball 'dragable' in the vertical direction
root.bind('<B1-Motion>', move)

#Run root window's main loop
root.mainloop()