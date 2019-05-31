import tkinter as tk
import time
import subprocess
def update_timertime():
    if (timerstate == True):
        global timer
        # Every time this function is called, 
        # we will increment 1 centisecond (1/100 of a second)
        timer[1] -= 1
        if timer[1]==0 and timer[0]==0:
        	subprocess.call(['xdg-open','/home/chadalavada/Desktop/python-mini/voltage.mp3'])
        	exittimer()
        # Every 60 seconds is equal to 1 min
        if (timer[1] == 0):
            timer[0] -= 1
            timer[1] = 60
        # We create our time string here
        timeString = pattern.format(timer[0], timer[1])
        # Update the timeText Label box with the current time
        timeText.configure(text=timeString)
        # Call the update_timertime() function after 1 centisecond
    root.after(1000, update_timertime)

# To start the kitchen timer
def timerstart():
    global timerstate
    timerstate = True


def exittimer():
    root.destroy()

# Simple status flag
# False mean the timer is not running
# True means the timer is running (counting)
def funtimer():
	global timerstate
	timerstate = False
	global root
	root = tk.Tk()
	root.wm_title('Stop Watch')
	timermin=int(input("Enter no.of min: "))
	timersec=int(input("Enter no.of sec: "))
	global timer
	# Our time structure [min, sec, centsec]
	timer = [timermin, timersec]
	global pattern
	# The format is padding all the 
	pattern = '{0:02d}:{1:02d}'
	global timeText
	# Create a timeText Label (a text box)
	timeText = tk.Label(root, text=str(timermin)+':'+str(timersec), font=("Helvetica", 150))
	timeText.pack()

	startButton = tk.Button(root, text='Start', command=timerstart)
	startButton.pack()


	quitButton = tk.Button(root, text='Quit', command=exit)
	quitButton.pack()

	update_timertime()
	root.mainloop()
funtimer()
